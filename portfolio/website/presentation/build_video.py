"""Makes the narrated video for From neurons to next steps from the deck: each slide is shown while
its narration plays. The narration is the slide's speaker notes, read by a computer voice (Kokoro).

Run after build_deck.py:  python3 website/presentation/build_video.py <folder with kokoro-v1.0.onnx and voices-v1.0.bin>
Writes website/video/from-neurons-to-next-steps.mp4 and .vtt. A recording at website/video/voice/NN.wav (or .m4a, .mp3)
replaces the computer voice for slide NN; see application/recording-script.md."""
import json, subprocess, sys, tempfile
from pathlib import Path

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

P = Path(__file__).resolve().parent
W = P.parent
OUT = W / "video"
sys.path.insert(0, str(P))
import build_deck as D  # noqa: E402

# The talk notes are written for a person presenting; the video says the same thing without "I".
SPOKEN = {
    "cover": "From neurons to next steps. This started at Pragnya, where Amishi volunteers with neurodivergent children, and follows one question from real life into the lab and back out again: two studies with public brain recordings, the two apps their findings shaped, and where the work goes next.",
    "loop": "Here is the whole story. Real life raised a question. A mouse study helps us understand it. An EEG study asks whether we can measure it in a person. The answers shape the design of two apps. And the last step tests the apps back in real life.",
    "close": "So, the loop. Real life raised the question. In mice, how alert the brain was changed how it reacted to the same picture. A brain-wave headset could not reliably tell even whether a person’s eyes were closed. So the apps ask how someone feels, and show one small step at a time. Everything in this video is on the website, with the phone tour, the slides and both apps linked from it.",
}


def stamp(t):
    h, m = int(t // 3600), int(t % 3600 // 60)
    return f"{h:02d}:{m:02d}:{t % 60:06.3f}"


def main(tts):
    k = Kokoro(f"{tts}/kokoro-v1.0.onnx", f"{tts}/voices-v1.0.bin")
    OUT.mkdir(exist_ok=True)
    files = sorted((P / "slides").glob("*.jpg"))
    assert len(files) == len(D.SLIDES), "run build_deck.py first"
    tmp = Path(tempfile.mkdtemp())
    clips, cues, t = [], [], 0.0
    for i, (img, s) in enumerate(zip(files, D.SLIDES)):
        text = SPOKEN.get(s["key"], s["notes"])
        own = next((f for f in sorted((OUT / "voice").glob(f"{i + 1:02d}.*")) if f.suffix in (".wav", ".m4a", ".mp3")), None) if (OUT / "voice").is_dir() else None
        if own:  # Amishi's own recording for this slide (see application/recording-script.md)
            decoded = tmp / f"own{i:02d}.wav"
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(own), "-ac", "1", "-ar", "24000", str(decoded)], check=True)
            a, sr = sf.read(decoded, dtype="float32")
        else:
            a, sr = k.create(text, voice="af_bella", speed=0.94, lang="en-us")
        idx = np.where(np.abs(a) > 0.01)[0]
        a = a[max(0, idx[0] - int(.03 * sr)): idx[-1] + int(.08 * sr)]
        lead, tail = 0.5, 0.9
        a = np.concatenate([np.zeros(int(lead * sr)), a, np.zeros(int(tail * sr))]).astype(np.float32)
        wav = tmp / f"{i:02d}.wav"; sf.write(wav, a, sr)
        dur = len(a) / sr
        cues.append((t + lead, t + dur - tail, text)); t += dur
        clip = tmp / f"{i:02d}.mp4"
        # A slow push-in on each slide, so the picture is never completely still.
        frames = int(dur * 30)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", str(img), "-i", str(wav),
                        "-filter_complex", f"[0:v]scale=3840:-1,zoompan=z='min(1+0.0004*on,1.04)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s=1920x1080:fps=30,format=yuv420p[v]",
                        "-map", "[v]", "-map", "1:a", "-c:v", "libx264", "-preset", "medium", "-crf", "22", "-c:a", "aac", "-b:a", "128k", "-t", f"{dur:.3f}", str(clip)], check=True)
        clips.append(clip)
        print(f"{i + 1:2d} {s['key']:12s} {dur:5.1f}s")
    lst = tmp / "list.txt"; lst.write_text("".join(f"file '{c}'\n" for c in clips))
    mp4 = OUT / "from-neurons-to-next-steps.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", "-movflags", "+faststart", str(mp4)], check=True)
    (OUT / "from-neurons-to-next-steps.vtt").write_text("WEBVTT\n\n" + "\n".join(f"{n}\n{stamp(a)} --> {stamp(b)}\n{txt}\n" for n, (a, b, txt) in enumerate(cues, 1)))
    json.dump({"seconds": round(t, 1), "slides": len(clips)}, open(OUT / "video.json", "w"))
    print("video", round(t, 1), "s →", mp4)


if __name__ == "__main__":
    main(sys.argv[1])
