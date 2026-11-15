"""Small, dependency-free handoff audit for the ASDRP portfolio."""

from pathlib import Path
import hashlib
import json
import re


ROOT = Path(__file__).resolve().parents[1]


def require(path: str) -> None:
    target = ROOT / path
    if not target.is_file() or target.stat().st_size == 0:
        raise SystemExit(f"MISSING: {path}")
    print(f"OK file {path}")


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def contains(path: str, pattern: str) -> None:
    if not re.search(pattern, text(path), re.IGNORECASE):
        raise SystemExit(f"MISSING text /{pattern}/ in {path}")
    print(f"OK text {path}: /{pattern}/")


def main() -> None:
    required = [
        "application/ASDRP-neuroscience-portfolio-packet.pdf",
        "application/contribution-ledger.md",
        "application/reproducibility-checklist.md",
        "communication/projects/mouse-visual-cortex/index.html",
        "communication/projects/mouse-visual-cortex/slides.html",
        "communication/projects/neuroscience-mobile/index.html",
        "communication/projects/neuroscience-mobile/releases/neuroscience-lab-debug.apk",
        "communication/projects/neuroscience-mobile/native/dist/index.html",
        "website/presentation/index.html",
        "website/presentation/from-neurons-to-next-steps-slides.pdf",
        "website/video/from-neurons-to-next-steps.mp4",
        "website/video/from-neurons-to-next-steps.vtt",
        "communication/video/renders/mouse-research-storyboard.mp4",
        "communication/video/renders/mouse-research-storyboard.vtt",
        "communication/video/renders/eeg-research-storyboard.mp4",
        "communication/video/renders/eeg-research-storyboard.vtt",
        "communication/video/renders/portfolio-research-storyboard.mp4",
        "communication/video/renders/portfolio-research-storyboard.vtt",
        "website/index.html",
        "website/mouse.html",
        "website/eeg.html",
        "website/tools.html",
        "website/next.html",
        "website/assets/results.js",
        "website/assets/theme-atlas.css",
        "website/reviewer-dashboard.html",
        "website/eeg-label-shuffle-control.html",
        "website/mouse-leave-one-out.html",
        "website/eeg-purge-gap.html",
        "projects/eeg-eye-state/results/metrics.json",
        "projects/eeg-eye-state/REPRODUCIBILITY_RUN.md",
        "../results/per_mouse_replication_summary.json",
        "../results/shuffled_behavior_controls.json",
    ]
    # The website's numbers must be the committed results: rebuild them and compare.
    site_results = text("website/assets/results.js")
    eeg = json.loads(text("projects/eeg-eye-state/results/metrics.json"))
    for value in (eeg["models"][0]["test_roc_auc"], eeg["artifact_sensitivity"]["final_holdout"][0]["test_roc_auc"], eeg["blocked_cross_validation"][0]["summary"]["mean_test_roc_auc"]):
        if f"{round(value, 3)}" not in site_results:
            raise SystemExit(f"WEBSITE number out of date: {round(value, 3)} (run python3 website/build_results.py)")
    print("OK website numbers match the committed EEG results")
    for page in ("index", "mouse", "eeg", "tools", "next"):
        if "gargibhatia" in text(f"website/{page}.html") or "github.com/mehtama1234/neuro-divergent" in text(f"website/{page}.html"):
            raise SystemExit(f"WEBSITE {page}.html links to the old host or a private repository")
    print("OK website pages link only to public places")

    for path in required:
        require(path)

    csv = (ROOT.parent / "results/per_mouse_metrics.csv").read_text(encoding="utf-8")
    rows = [line for line in csv.splitlines() if line.strip()]
    if len(rows) != 4:
        raise SystemExit(f"EXPECTED 3 mouse rows plus header, found {len(rows)} lines")
    print("OK metrics: three mouse rows")
    for path in (
        "communication/projects/mouse-visual-cortex/index.html",
        "communication/projects/mouse-visual-cortex/slides.html",
        "communication/projects/mouse-visual-cortex/video-script.md",
        "application/reviewer-packet.html",
    ):
        contains(path, r"0\.143")
        contains(path, r"0\.191")
        contains(path, r"three")

    for path in ("website/neuroscience-mobile/index.html", "communication/projects/neuroscience-mobile/index.html"):
        contains(path, r"25–33%")
        contains(path, r"three mice")
        contains(path, r"0\.478")
    print("OK phone tour tells the same story as the site")

    legacy_packet = text("application/reviewer-packet-v1.html")
    if re.search(r"one-mouse|one mouse|replication pending", legacy_packet, re.IGNORECASE):
        raise SystemExit("STALE one-mouse claim in reviewer packet archive")
    print("OK archived reviewer packet scope: three-mouse")

    reproducibility = (ROOT.parent / "docs/REPRODUCIBILITY_RUN.md").read_text(encoding="utf-8")
    if re.search(r"two-mouse|two mice|both animals|beyond two", reproducibility, re.IGNORECASE):
        raise SystemExit("STALE replication scope in flagship reproducibility record")
    print("OK flagship reproducibility scope: three-mouse")
    eeg_metrics = json.loads((ROOT / "projects/eeg-eye-state/results/metrics.json").read_text(encoding="utf-8"))
    blocked = eeg_metrics.get("blocked_cross_validation", [])
    if len(blocked) != 2 or any(item.get("fold_count") != 5 for item in blocked):
        raise SystemExit("EXPECTED five blocked EEG folds for both models")
    print("OK EEG expansion: five forward-chaining folds per model")
    shuffled_eeg = eeg_metrics.get("blocked_label_shuffle_control", [])
    if len(shuffled_eeg) != 2 or any(item.get("permutations") != 20 for item in shuffled_eeg):
        raise SystemExit("EXPECTED 20 label-shuffle controls for both EEG models")
    print("OK EEG negative control: 20 label shuffles per model")
    gap = eeg_metrics.get("blocked_gap_sensitivity", [])
    if len(gap) != 2 or any(item.get("fold_count") != 5 or item.get("gap_samples") != 90 for item in gap):
        raise SystemExit("EXPECTED five-fold EEG sensitivity with a 90-sample purge gap")
    print("OK EEG sensitivity: five forward folds with 90-sample purge gap")
    controls = json.loads((ROOT.parent / "results/shuffled_behavior_controls.json").read_text(encoding="utf-8"))
    if len(controls) != 3 or any(row.get("permutations") != 20 for row in controls):
        raise SystemExit("EXPECTED 20 behavior-shuffle controls for three mice")
    print("OK mouse negative control: 20 behavior shuffles per animal")
    mouse_summary = json.loads((ROOT.parent / "results/per_mouse_replication_summary.json").read_text(encoding="utf-8"))
    leave_one_out = mouse_summary.get("leave_one_animal_out_mean_gain", [])
    if len(leave_one_out) != 3 or any(row.get("mean_absolute_gain", 0) <= 0 for row in leave_one_out):
        raise SystemExit("EXPECTED positive leave-one-animal-out gains for three mice")
    print("OK mouse stability: positive leave-one-animal-out gains")
    rel = mouse_summary["relative_gain_percent_summary"]
    headline = f"{round(rel['min'])}–{round(rel['max'])}%"
    for path in ("website/index.html", "website/mouse.html", "website/neuroscience-mobile/index.html"):
        contains(path, headline)
    print(f"OK headline gain {headline} matches the flagship summary")
    for row in mouse_summary["animals"]:
        if f'"gain": {round(row["absolute_gain"], 4)}' not in text("website/build_results.py"):
            raise SystemExit(f"MOUSE gain for {row['mouse'][:11]} differs from the flagship summary")
    print("OK per-mouse gains match the flagship summary")
    bands = json.loads(text("projects/eeg-eye-state/results/bands.json"))
    for kind, shown in (("all four bands", "0.566"), ("raw readings", "0.481"), ("alpha only", "0.442")):
        if f"{bands['with_gap'][kind]['mean']:.3f}" != shown:
            raise SystemExit(f"EXPERIMENT 2 {kind} mean changed: rerun and update the pages")
        contains("website/eeg.html", shown)
    if bands["holds_up_better"]:
        raise SystemExit("EXPERIMENT 2 now holds up: the pages say it did not")
    contains("website/next.html", "2 · Done")
    print("OK experiment 2 numbers and verdict match results/bands.json")

    apk = ROOT / "communication/projects/neuroscience-mobile/releases/neuroscience-lab-debug.apk"
    digest = hashlib.sha256(apk.read_bytes()).hexdigest()
    expected = (ROOT / "communication/projects/neuroscience-mobile/releases/SHA256.txt").read_text().split()[0]
    if digest != expected:
        raise SystemExit(f"APK SHA mismatch: {digest}")
    print(f"OK APK SHA-256 {digest}")
    print("PORTFOLIO AUDIT PASSED")


if __name__ == "__main__":
    main()
