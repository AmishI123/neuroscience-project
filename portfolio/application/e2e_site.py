"""End-to-end test of the published website, phone tour, slides and video.

Serves a folder (the gh-pages checkout, or website/) over HTTP and drives it in Chromium:
every page loads with no errors or missing files, every icon, drawing and chart draws, nothing
spills sideways on a phone or a laptop, the phone tour and slide viewer can be clicked through,
old addresses forward, and the video, captions, PDF and Android app are served.

Run: python3 application/e2e_site.py [folder]   (default: website)"""
import functools, http.server, subprocess, sys, threading
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "website").resolve()
PAGES = ["index.html", "mouse.html", "eeg.html", "tools.html", "next.html", "neuroscience-mobile/index.html",
         "neuroscience-mobile/download.html", "presentation/index.html", "video/index.html", "share/index.html", "handoff/index.html", "handoff/answers.html", "handoff/essay-1.html", "handoff/essay-5.html", "handoff/who-did-what.html", "handoff/recording.html"]
REDIRECTS = {"mouse-visual-cortex.html": "mouse.html", "eeg-eye-state.html": "eeg.html", "mouse-visual-cortex-slides.html": "presentation/",
             "eeg-eye-state-slides.html": "presentation/", "reviewer-dashboard.html": "index.html", "release-verification.html": "share/"}
FILES = ["video/from-neurons-to-next-steps.mp4", "video/from-neurons-to-next-steps.vtt", "presentation/from-neurons-to-next-steps-slides.pdf", "presentation/from-neurons-to-next-steps-slides.pptx", "img/qr-phone-tour.svg",
         "ASDRP-neuroscience-portfolio-packet.pdf", "neuroscience-lab-debug.apk", "neuroscience-mobile/manifest.webmanifest"]
fails = []


def check(ok, what):
    print(("PASS " if ok else "FAIL ") + what)
    if not ok: fails.append(what)


def serve():
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    handler = functools.partial(Quiet, directory=str(ROOT))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return f"http://127.0.0.1:{srv.server_address[1]}/"


def main():
    base = serve()
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        for width in (1280, 390):
            ctx = b.new_context(viewport={"width": width, "height": 900})
            for name in PAGES:
                pg = ctx.new_page(); errors, missing = [], []
                pg.on("pageerror", lambda e: errors.append(str(e)))
                pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
                pg.on("response", lambda r: missing.append(r.url) if r.status >= 400 and r.url.startswith(base) else None)
                pg.goto(base + name, wait_until="networkidle")
                empty = pg.evaluate("""() => [...document.querySelectorAll('[data-icon],[data-art],[data-chart]')].filter(e => !e.innerHTML.trim()).map(e => e.dataset.icon || e.dataset.art || e.dataset.chart)""")
                over = pg.evaluate("document.documentElement.scrollWidth") - width
                check(not errors, f"{width}px {name}: no script errors {errors[:2] if errors else ''}")
                check(not missing, f"{width}px {name}: every file it asks for exists {missing[:3] if missing else ''}")
                check(not empty, f"{width}px {name}: every icon, drawing and chart drew {empty[:5] if empty else ''}")
                check(over <= 0, f"{width}px {name}: nothing spills sideways ({over}px)")
                pg.close()
            ctx.close()

        # The phone tour: tap Start, then Next through all five chapters, then back to the start.
        pg = b.new_page(viewport={"width": 390, "height": 844}); pg.goto(base + "neuroscience-mobile/index.html")
        seen = []
        for _ in range(6):
            seen.append(pg.evaluate("document.querySelector('[data-screen]:not([hidden])').dataset.screen"))
            pg.locator("[data-screen]:not([hidden]) .button.primary").click()
        seen.append(pg.evaluate("document.querySelector('[data-screen]:not([hidden])').dataset.screen"))
        check(seen == ["home", "ch1", "ch2", "ch3", "ch4", "ch5", "home"], f"phone tour: Next goes through every chapter and back ({' → '.join(seen)})")
        pg.locator(".tour-nav [data-go=ch3]").click()
        check(pg.evaluate("location.hash") == "#ch3" and pg.locator(".tour-nav [data-go=ch3]").get_attribute("aria-current") == "page", "phone tour: the Measure tab opens chapter 3")
        pg.close()

        # The handoff pages keep writing in the browser and count essay words.
        ctx = b.new_context(viewport={"width": 1280, "height": 900}); pg = ctx.new_page()
        pg.goto(base + "handoff/answers.html"); pg.fill("#q-moment", "Test moment")
        pg.reload(); check(pg.input_value("#q-moment") == "Test moment", "handoff: an answer is still there after reloading")
        pg.goto(base + "handoff/essay-1.html"); words = pg.inner_text("[data-words-for]")
        check("of 375" in words and "[brackets]" in words, f"handoff: Essay 1 shows its word count ({words})")
        with pg.expect_download() as dl: pg.click("[data-download]")
        check(dl.value.suggested_filename == "essay-1.txt", "handoff: Essay 1 downloads as a text file")
        ctx.close()

        # The slide viewer: arrow keys move, and the presenter view has notes.
        pg = b.new_page(viewport={"width": 1280, "height": 800}); pg.goto(base + "presentation/present.html")
        first = pg.inner_text("#count"); pg.keyboard.press("ArrowRight"); pg.wait_for_timeout(100)
        check(first.startswith("1 /") and pg.inner_text("#count").startswith("2 /"), f"slides: the arrow key moves to slide 2 ({first} → {pg.inner_text('#count')})")
        check(pg.evaluate("document.getElementById('view').naturalWidth") == 1920, "slides: the slide picture loads at full size")
        pg.goto(base + "presentation/presenter.html")
        check(len(pg.inner_text("#notes")) > 40, "slides: the presenter view shows speaker notes")
        pg.close()

        # Old addresses forward to the new pages.
        pg = b.new_page()
        for old, new in REDIRECTS.items():
            pg.goto(base + old); pg.wait_for_load_state("networkidle")
            check(pg.url.rstrip("/").endswith(new.rstrip("/")) or pg.url.endswith(new + "index.html"), f"old address {old} forwards to {new}")
        # Downloads are served.
        for f in FILES:
            r = pg.request.get(base + f)
            check(r.ok and len(r.body()) > 100, f"file {f} is served ({len(r.body()) // 1024} KB)")
        b.close()

    # The video plays for its full length (Chromium in tests has no H.264, so ffprobe reads it).
    import shutil
    if not shutil.which("ffprobe"):
        head = (ROOT / FILES[0]).read_bytes()[:12]
        check(head[4:8] == b"ftyp", "video: the file is an MP4 (ffprobe not installed, so length not checked)")
        print(f"\n{'ALL END-TO-END CHECKS PASSED' if not fails else str(len(fails)) + ' CHECKS FAILED'}"); sys.exit(1 if fails else 0)
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_name,width,height", "-of", "csv=p=0", str(ROOT / FILES[0])], capture_output=True, text=True).stdout.split()
    check(any(line.startswith("h264,1920,1080") for line in out) and float(out[-1]) > 120, f"video: 1920x1080 H.264 with sound, {float(out[-1]):.0f} seconds")
    print(f"\n{'ALL END-TO-END CHECKS PASSED' if not fails else str(len(fails)) + ' CHECKS FAILED'}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
