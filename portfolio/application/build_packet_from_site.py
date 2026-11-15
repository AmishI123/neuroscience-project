"""Builds the reviewer PDF packet from the portfolio website itself, so the PDF has the same design,
illustrations, charts and numbers as the pages. Needs Playwright (python -m pip install playwright).
Run: python3 application/build_packet_from_site.py"""
import http.server
import threading
from functools import partial
from pathlib import Path

from playwright.sync_api import sync_playwright
from pypdf import PdfWriter

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "application" / "ASDRP-neuroscience-portfolio-packet.pdf"
PAGES = ["index", "mouse", "eeg", "tools", "next"]

handler = partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT / "website"))
server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{server.server_port}"
parts = []
with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page(viewport={"width": 1280, "height": 900})
    for name in PAGES:
        page.goto(f"{base}/{name}.html", wait_until="networkidle")
        page.wait_for_timeout(300)
        height = page.evaluate("document.documentElement.scrollHeight")
        part = ROOT / "application" / f".packet-{name}.pdf"
        # One tall page per web page, at the width the site was designed for.
        page.pdf(path=str(part), width="1280px", height=f"{height + 2}px", print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        parts.append(part)
    browser.close()
server.shutdown()
writer = PdfWriter()
for part in parts:
    writer.append(str(part))
    part.unlink()
writer.add_metadata({"/Title": "Brain & Behaviour · ASDRP neuroscience portfolio", "/Subject": "Two neuroscience studies, their checks, and tools for people"})
with OUT.open("wb") as handle:
    writer.write(handle)
(ROOT / "website" / OUT.name).write_bytes(OUT.read_bytes())
print("wrote", OUT.relative_to(ROOT), "and website/" + OUT.name)
