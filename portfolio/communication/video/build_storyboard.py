"""Render silent, captioned research storyboard videos from verified facts.

These are visual review artifacts, not narrated final submissions. The applicant's
own narration and captions should replace or accompany them before application use.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "communication" / "video" / "renders"
FFMPEG = "/home/mehta/.local/lib/python3.12/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
W, H, FPS, SECONDS = 1280, 720, 30, 4
CREAM, PAPER, INK, MUTED, RUST, GREEN = "#F3ECE1", "#FAF6EF", "#2B2622", "#5A5047", "#9A4A22", "#216B4C"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"


SLIDES = {
    "mouse": [
        ("ASDRP / MOUSE VISUAL CORTEX", "Can behavior help us predict the brain?", "A visual-cortex encoding-model study using real mouse recordings."),
        ("THE DATA", "Three mice. Thousands of neurons.", "Natural-image stimuli, pupil size, running speed, and neural responses."),
        ("THE COMPARISON", "Two models. One held-out test.", "Stimulus only versus stimulus plus behavior, with training-only preprocessing."),
        ("THE RESULT", "0.126 → 0.158 | 0.154 → 0.203 | 0.143 → 0.191", "Mean held-out correlation rises when behavior is added in all three evaluated mice."),
        ("THE ABLATION", "Pupil improves all three.", "Running contributes differently across animals; the result is predictive, not causal."),
        ("THE LIMIT", "Three animals are not a population.", "The next scientific step is replication beyond three animals with population-level uncertainty."),
    ],
    "eeg": [
        ("ASDRP / EEG EYE STATE", "Can short-term history decode a neural state?", "A time-aware classification study using a public 14-channel EEG recording."),
        ("THE DATA", "14 channels. 14,980 samples.", "One continuous recording with a manually annotated open-eye / closed-eye label."),
        ("THE EVALUATION", "Time order matters.", "70% train, 15% validation, 15% final test. No random row split."),
        ("THE BASELINE", "Test ROC AUC: 0.625", "Pointwise standardized EEG with class-balanced logistic regression."),
        ("THE EXTENSION", "Test ROC AUC: 0.530", "Causal temporal context did not generalize on the final held-out block."),
        ("THE EXPANSION", "Five blocked folds stay near chance.", "Mean ROC AUC: 0.478 pointwise versus 0.488 with context; fold variation is wide."),
        ("THE TIMESCALE TEST", "90 samples led the sweep.", "Mean blocked-fold ROC AUC: 0.491 at 3 samples, 0.488 at 9, 0.548 at 30, and 0.567 at 90."),
        ("THE LIMIT", "Negative results count.", "More recordings and multiple time scales are needed before generalization claims."),
    ],
    "portfolio": [
        ("ASDRP / NEUROSCIENCE PORTFOLIO", "Study the brain. Build for people.", "A connected research and communication portfolio with reproducible evidence."),
        ("FLAGSHIP", "Behavior improves prediction across three mice.", "Held-out correlation rises 0.126 → 0.158, 0.154 → 0.203, and 0.143 → 0.191."),
        ("COMPLEMENTARY STUDY", "EEG results stay honest.", "The pointwise model reaches 0.625 final-block ROC AUC; causal context reaches 0.530."),
        ("DEEPER ANALYSIS", "Controls and timescales matter.", "Behavior shuffles erase the mouse gain; EEG blocked folds and window sweeps expose variability."),
        ("TRANSLATION", "Research should be inspectable and usable.", "Neurocomms and Neurodivergent patterns inform accessible mobile, HTML, presentation, and video artifacts."),
        ("REPRODUCIBILITY", "Every claim has a trail.", "Reports, code, manifests, metrics, figures, captions, an Android build, and a release audit are public."),
        ("NEXT", "Keep testing without overstating.", "Add animals, recordings, hierarchical uncertainty, applicant narration, and personal application details."),
    ],
}


def font(path: str, size: int):
    return ImageFont.truetype(path, size)


def frame(kicker: str, title: str, body: str, index: int, total: int) -> bytes:
    image = Image.new("RGB", (W, H), CREAM)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, W, 18), fill=RUST)
    draw.text((72, 66), kicker, font=font(FONT, 22), fill=RUST)
    draw.text((72, 160), title, font=font(SERIF, 62), fill=INK, spacing=8)
    draw.multiline_text((72, 330), body, font=font(FONT, 29), fill=MUTED, spacing=12)
    draw.line((72, 590, W - 72, 590), fill=INK, width=2)
    draw.text((72, 620), "ASDRP neuroscience portfolio", font=font(FONT, 18), fill=MUTED)
    draw.text((W - 190, 620), f"{index:02d} / {total:02d}", font=font(FONT, 18), fill=RUST)
    return image.tobytes()


def render(name: str) -> Path:
    slides = SLIDES[name]
    OUT.mkdir(parents=True, exist_ok=True)
    destination = OUT / f"{name}-research-storyboard.mp4"
    command = [FFMPEG, "-y", "-f", "rawvideo", "-vcodec", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(destination)]
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    assert process.stdin is not None
    for index, (kicker, title, body) in enumerate(slides, 1):
        raw = frame(kicker, title, body, index, len(slides))
        for _ in range(FPS * SECONDS):
            process.stdin.write(raw)
    process.stdin.close()
    error = process.stderr.read().decode("utf-8", errors="replace")
    code = process.wait()
    if code:
        raise RuntimeError(error[-2000:])
    captions = ["WEBVTT\n\n"]
    for index, (kicker, title, body) in enumerate(slides):
        start = index * SECONDS
        end = (index + 1) * SECONDS
        captions.append(f"{start // 3600:02d}:{(start % 3600) // 60:02d}:{start % 60:02d}.000 --> {end // 3600:02d}:{(end % 3600) // 60:02d}:{end % 60:02d}.000\n{kicker}\n{title}\n{body}\n\n")
    (OUT / f"{name}-research-storyboard.vtt").write_text("".join(captions), encoding="utf-8")
    print(destination)
    return destination


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("project", choices=sorted(SLIDES))
    render(parser.parse_args().project)
