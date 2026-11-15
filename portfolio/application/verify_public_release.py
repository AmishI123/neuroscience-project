"""Verify that the public Site exposes the current reviewer release."""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://amishi123.github.io/neuroscience-project"
ROUTES = ("/", "/mouse.html", "/eeg.html", "/tools.html", "/next.html", "/assets/results.js", "/assets/theme-atlas.css", "/release-verification.html", "/mouse-visual-cortex.html", "/eeg-eye-state.html", "/neuroscience-mobile/", "/mouse-visual-cortex-slides.html", "/eeg-eye-state-slides.html", "/presentation/", "/presentation/present.html", "/video/", "/video/from-neurons-to-next-steps.mp4", "/neuroscience-mobile/download.html", "/share/", "/presentation/from-neurons-to-next-steps-slides.pptx")
SOURCE_URLS = (
    "https://github.com/AmishI123/neuroscience-project/tree/main/portfolio",
    "https://github.com/AmishI123/neuroscience-project",
    "https://github.com/AmishI123/neuroscience-project/blob/main/results/per_mouse_metrics.csv",
    "https://github.com/AmishI123/neuroscience-project/tree/main/portfolio/projects/eeg-eye-state",
)


def fetch(path: str) -> tuple[int, bytes]:
    request = Request(BASE + path, headers={"User-Agent": "ASDRP-release-verifier/1.0"})
    with urlopen(request, timeout=30) as response:
        return response.status, response.read()


def main() -> None:
    failures: list[str] = []
    for path in ROUTES:
        try:
            status, body = fetch(path)
            if status != 200 or not body:
                failures.append(f"{path}: HTTP {status} or empty body")
            else:
                print(f"OK public route {path}: HTTP {status}")
        except Exception as error:  # noqa: BLE001
            failures.append(f"{path}: {error}")

    for url in SOURCE_URLS:
        try:
            request = Request(url, headers={"User-Agent": "ASDRP-release-verifier/1.0"})
            with urlopen(request, timeout=30) as response:
                if response.status != 200:
                    failures.append(f"source link {url}: HTTP {response.status}")
                else:
                    print(f"OK source link: {url}")
        except Exception as error:  # noqa: BLE001
            failures.append(f"source link {url}: {error}")

    try:
        status, remote_pdf = fetch("/ASDRP-neuroscience-portfolio-packet.pdf")
        local_pdf = ROOT / "application" / "ASDRP-neuroscience-portfolio-packet.pdf"
        local_digest = hashlib.sha256(local_pdf.read_bytes()).hexdigest()
        remote_digest = hashlib.sha256(remote_pdf).hexdigest()
        if status != 200 or local_digest != remote_digest:
            failures.append(f"PDF hash mismatch: local={local_digest} public={remote_digest}")
        else:
            print(f"OK public PDF SHA-256 {remote_digest}")
    except Exception as error:  # noqa: BLE001
        failures.append(f"PDF: {error}")

    if failures:
        print("PUBLIC RELEASE VERIFICATION FAILED", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        raise SystemExit(1)
    print("PUBLIC RELEASE VERIFICATION PASSED")


if __name__ == "__main__":
    main()
