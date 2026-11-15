"""Mux an applicant-recorded WAV into a verified storyboard MP4."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FFMPEG = "/home/mehta/.local/lib/python3.12/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", choices=("mouse", "eeg"))
    parser.add_argument("narration", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    source = ROOT / "communication/video/renders" / f"{args.project}-research-storyboard.mp4"
    if not source.is_file():
        raise SystemExit(f"Missing storyboard: {source}")
    if not args.narration.is_file():
        raise SystemExit(f"Missing narration WAV: {args.narration}")
    destination = args.output or (ROOT / "communication/video/renders" / f"{args.project}-research-final.mp4")
    if destination.exists():
        raise SystemExit(f"Refusing to overwrite existing file: {destination}")
    command = [
        FFMPEG, "-y", "-i", str(source), "-i", str(args.narration),
        "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac",
        "-b:a", "128k", "-shortest", "-movflags", "+faststart", str(destination),
    ]
    subprocess.run(command, check=True)
    print(destination)


if __name__ == "__main__":
    main()
