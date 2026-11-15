"""Makes the QR codes on the share page (website/img/qr-*.svg). Needs `pip install qrcode`.
Run again only if a link changes: python3 website/make_qr.py"""
from pathlib import Path
import qrcode, qrcode.image.svg

SITE = "https://amishi123.github.io/neuroscience-project/"
LINKS = {"website": SITE, "phone-tour": SITE + "neuroscience-mobile/", "video": SITE + "video/", "slides": SITE + "presentation/"}
out = Path(__file__).resolve().parent / "img"
for name, url in LINKS.items():
    img = qrcode.make(url, image_factory=qrcode.image.svg.SvgPathImage, box_size=10, border=2)
    svg = img.to_string(encoding="unicode").replace('fill="#000000"', 'fill="#2B2622"')
    (out / f"qr-{name}.svg").write_text(svg)
    print("wrote", f"img/qr-{name}.svg", url)
