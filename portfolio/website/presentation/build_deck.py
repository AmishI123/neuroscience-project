"""Builds the slide deck for From neurons to next steps from the same words, charts and drawings as the
website. Each slide is a 1200x675 page in the website's own styles, shown at 1.6x (1920x1080).

Run: python3 website/presentation/build_deck.py
Writes presentation/src/*.html, slides/*.jpg, slides.html, present.html, presenter.html and the PDF."""
import html, json, sys
from pathlib import Path

P = Path(__file__).resolve().parent
W = P.parent
sys.path.insert(0, str(W)); sys.path.insert(0, str(P))
import build_pages as B  # noqa: E402  (rebuilding the pages first keeps the deck and site in step)
import viewers  # noqa: E402

PDF = "from-neurons-to-next-steps-slides.pdf"
SLIDES = []


def slide(key, alt, body, notes, cls=""):
    SLIDES.append({"key": key, "alt": alt, "body": body, "notes": notes, "cls": cls})


def head(eyebrow, title, sub="", art=""):
    a = f'<div class="hj-art" data-art="{art}"></div>' if art else ""
    s = f'<p class="hj-sub">{sub}</p>' if sub else ""
    return f'<div class="lm-head"><div class="hj-heading"><p class="eyebrow">{eyebrow}</p><h1>{title}</h1>{s}</div>{a}</div>'


def answer(text):
    return f'<section class="landing-problems answer"><p class="lp-energy">{text}</p></section>'


def cards(items, cls=""):
    return f'<section class="landing-problems {cls}"><ol>' + "".join(f'<li><p class="lp-k">{k}</p><h3>{h}</h3><p class="lp-pain">{a}</p>{f"<p class=lp-fix>{b}</p>" if b else ""}</li>' for k, h, a, b in items) + '</ol></section>'


# 1 -------------------------------------------------------------------------------------------
slide("cover", "From neurons to next steps: an ASDRP neuroscience portfolio by Amishi Mehta, with the four-card collage.", f"""
<div class="landing-hero"><div class="landing-hero-text">
<p class="landing-kicker">An ASDRP neuroscience portfolio · Amishi Mehta</p>
<h1>From neurons to next steps</h1>
<p class="landing-lede">It started at Pragnya, where Amishi volunteers with neurodivergent children: one child was dancing while another covered their ears in the same room. <b>Does what a brain is doing change what it takes in?</b> And if it does, how should we design for it?</p>
<p class="landing-try-note">Public data only. Predicting something is not the same as knowing its cause. Plans are marked as plans.</p>
</div>{B.LANDING_ART}</div>""",
      "This is one question, followed from real life into the lab and back out again. I’ll show two studies with public brain recordings, then the two apps their findings shaped, and where the work goes next.")
# 1b
slide("found", "What we found, in three sentences: in mice, brain cells reacted differently to the same picture depending on alertness; a brain-wave headset could not reliably tell even eyes open from closed; so a helpful app asks how you feel and shows one small step at a time.", f"""
{head('What we found', 'In three sentences.')}
{cards([
    ('1 · The mouse study', 'In mice, brain cells reacted differently to the very same picture depending on how alert the mouse was.', 'Adding how alert each mouse was made our predictions of its brain cells <b>25–33% better</b>, in all three mice.', ''),
    ('2 · The brain-wave study', 'A brain-wave headset on a person could not reliably tell even whether their eyes were open or closed.', 'A computer spotted closed eyes for one stretch, then within two minutes was <b>no better than a coin flip</b>.', ''),
    ('3 · The app', 'So a helpful app should not try to read your brain: it should ask how you feel and show one small step at a time.', 'Next Step asks <b>“How much energy do you have today?”</b> and on a low day shows only the next step.', ''),
], 'found3')}""",
      "Here is the whole answer in three sentences. One: In mice, brain cells reacted differently to the very same picture depending on how alert the mouse was. Two: A brain-wave headset on a person could not reliably tell even whether their eyes were open or closed. Three: So a helpful app should not try to read your brain: it should ask how you feel and show one small step at a time. The rest of this talk shows the evidence for each one.")
# 2
slide("loop", "The loop: real life, understand, measure, design, test, and back to real life.", f"""
{head('The whole story on one page', 'One loop, five chapters.', 'It starts in real life and ends back there. Each chapter answers the question the last one raised.')}
<div class="loop-figure"><div class="loop-wide" data-art="loop"></div></div>""",
      "Here is the whole talk. Real life raised a question. A mouse study helps us understand it. An EEG study asks whether we can measure it in a person. The answers shape the design of two apps. And the last step tests the apps back in real life.")
# 3
slide("ch1", "Chapter 1, real life: same words, different moment.", f"""
{head('Chapter 1 · Real life', 'Same words, different moment.', 'It started at Pragnya, where one child was dancing while another covered their ears in the same room. A step that is easy when you are calm can be lost when you are tired, rushed or overloaded.', 'note')}
{answer('<b>The question:</b> is that the brain itself changing what it takes in? <span>To find out, look inside a brain while its state changes.</span>')}""",
      "This is where it started: at Pragnya, where one child was dancing while another covered their ears in the same room. That made us ask whether how alert or tired a brain is changes what gets in.")
# 4
slide("ch2-how", "Chapter 2: how the mouse study works, in four steps.", f"""
{head('Chapter 2 · Understand · Mouse study', 'Does how alert a mouse is change how its brain sees?', 'Mice watched pictures while thousands of brain cells were recorded in the part of the brain that handles seeing.', 'mouseStudy')}
{B.grid([
    ('photo', 'Step 1', 'What the mouse saw', 'Each picture shrunk to a short summary of its light and dark patterns.'),
    ('eye', 'Step 2', 'What state it was in', 'Pupil size (wider usually means more alert) and running speed.'),
    ('chart-dots', 'Step 3', 'Two simple guessers', 'A sees only the picture. B sees the picture plus pupil and running.'),
])}""",
      "Scientists shared recordings of thousands of brain cells from mice watching pictures. We built two simple guessers. Guesser A only knows the picture. Guesser B also knows how wide the pupils were and how fast the mouse was running. Both are tested on pictures they have never seen.")
# 5
slide("ch2-result", "Chapter 2 result: guesser B beats guesser A in all three mice.", f"""
{head('Chapter 2 · The result', 'Every mouse is easier to predict once we know its state.')}
{answer('<b>A quarter to a third better (25–33%), in all three mice,</b> on pictures the model had never seen. <span>This shows state and seeing are linked. It does not yet show which causes which.</span>')}
{B.chart('mouse-scores', 'Score on unseen pictures', 'Guesser A against guesser B.', '0 means no match, 1 would be perfect. Brain cells are noisy, so scores are low. What matters is the jump from A to B.', 'Average over every recorded brain cell.')}""",
      "In every mouse, guesser B wins. The scores look small because single brain cells are noisy, so the thing to look at is the jump from A to B: a quarter to a third better. That is a link, not proof of cause.")
# 5b
slide("ch2-inside", "Inside the first mouse: it is the pupil, not the running, and 90% of brain cells gain.", f"""
{head('Chapter 2 · Inside the first mouse', 'It is the pupil, not the running.')}
<div class="tour-nums inside-nums"><p><b>90%</b><span>of brain cells guessed better once state was added</span></p><p><b>5×</b><span>bigger gain for cells that follow pupil size</span></p><p><b>0.05 → 0.40</b><span>one cell, from noise to a pattern</span></p></div>
{B.chart('mouse1-ablation', 'From Amishi’s saved results', 'Adding pupil gives almost the whole gain.', 'Running barely moved the score. This mouse ran on only about 5% of trials.', 'First mouse only, unseen pictures.')}""",
      "Looking inside the first mouse, from Amishi’s own analysis. Adding running barely changed anything; pupil size, a sign of how alert the mouse is, gave almost the whole gain. Nine in ten brain cells were guessed better, and the cells that follow alertness gained about five times as much as the rest.")
# 6
slide("ch2-checks", "Chapter 2 checks: mix up the state, leave one mouse out, pupil or running.", f"""
{head('Chapter 2 · Trying to break it', 'Three checks that could have made the gain disappear.', 'It survived all three.', 'controls')}
{B.grid([
    ('arrows-shuffle', 'Mix up the state', 'The gain disappears', 'Pupil and running from the wrong moments add nothing. It needs the state at that moment.'),
    ('users', 'Leave one mouse out', 'Still there', 'Take any one mouse away and the other two still show the gain.'),
    ('eye', 'Pupil or running?', 'Pupil helps every mouse', 'Running helps some mice more than others.'),
])}
{B.bridge('What chapter 2 tells us:', 'the same picture lands differently depending on the mouse’s state. Can a brain-wave headset measure that in a person?', '#', 'Chapter 3')}""",
      "We tried to break it. When we gave guesser B the wrong moments’ state, the gain disappeared. Leaving out any one mouse kept the gain. So how alert the mouse is really matters inside its brain. Next question: can a headset measure that in a person?")
# 7
slide("ch3-how", "Chapter 3: how the EEG study works.", f"""
{head('Chapter 3 · Measure · EEG study', 'Can sensors on the head tell when someone’s eyes are closed?', 'EEG is a cap of small sensors that pick up the brain’s electrical activity through the scalp. Closing your eyes is one of the clearest changes it can see.', 'eegHero')}
{B.grid([
    ('activity', 'The recording', 'One person, two minutes', '14 sensors, about 128 readings a second, each moment marked open or closed.'),
    ('timeline', 'Learn, then test', 'Earlier, then later', 'Learn from the first part, test on what comes after, like a real app would.'),
    ('target', 'The score', '0.5 is a coin flip', '1.0 is always right. Below 0.5 is worse than guessing.'),
])}""",
      "Now a person. EEG is a cap of sensors on the head. Closing your eyes is one of the easiest changes for it to see. If a simple model cannot read even that reliably, quieter states like tiredness will be harder. We always learn from earlier and test on later.")
# 8
slide("ch3-result", "Chapter 3 result: good on one stretch, a coin flip over time.", f"""
{head('Chapter 3 · The result', 'On one stretch, yes. Over time, no.')}
{answer('On the last part of the recording the model scored <b>0.625</b> (0.728 once four glitchy readings were trimmed). Across five stretches it averaged <b>0.478: about a coin flip.</b>')}
{B.chart('eeg-scale', 'How to read the score', 'Where the results sit between guessing and always right.', 'Near 0.5 is no better than flipping a coin. Below 0.5 means the pattern it learned has flipped.', 'The score is called AUC.')}""",
      "On one stretch it worked reasonably well. But when we tested it on five stretches across the recording, it averaged a coin flip.")
# 9
slide("ch3-drift", "Chapter 3: scores on five stretches scatter around a coin flip.", f"""
{head('Chapter 3 · Over time', 'Within two minutes, the signal drifts.')}
{B.chart('eeg-folds', 'Five stretches in time', 'Across the recording, it drifts to a coin flip.', 'Some stretches fall well below 0.5: the pattern learned earlier had flipped by later on. Trimming glitchy readings and leaving a gap do not fix it.', 'Mixing up the answers gives 0.499, so the method itself does not invent a pattern.')}
""",
      "Each dot is one stretch. They land on both sides of a coin flip, and some are worse than guessing. Within two minutes, the signal drifted.")
# 9b
slide("ch3-bands", "Experiment 2: brain-wave rhythms help on average but still dip below a coin flip.", f"""
{head('Chapter 3 · Experiment 2', 'Would brain-wave rhythms hold steady?', 'So the apps ask the person: even brain-wave rhythms are not steady enough to build on.')}
{answer('Planned before running. All four rhythms averaged <b>0.566</b> against 0.481 for raw readings, but two of five stretches still fell just below a coin flip. <b>By the rule set beforehand, it did not hold up.</b>')}
{B.chart('eeg-bands', 'Five stretches, one-second gap', 'Better on average, still not reliable.', 'Alpha alone did worse (0.442). Mixing up the answers gave 0.500, as it should.', 'Plan and code in the repository.')}
""",
      "So we asked a follow-up and wrote the plan down before running it: would the strength of brain-wave rhythms, like alpha, hold steady where raw readings did not? They helped on average, but two of five stretches still fell below a coin flip. By the rule we set beforehand, it did not hold up. So a tool should not try to guess how someone is doing from a sensor.")
# 10
slide("ch4-rules", "Chapter 4: four findings become four design rules.", f"""
{head('Chapter 4 · Design · Human–computer interaction', 'From findings to features.')}
{cards([
    ('From chapter 2', 'Show less when energy is low.', '<b>Found:</b> the same picture lands differently depending on how alert the brain is.', '<b>In the apps:</b> “How much energy do you have today?” On “A little”, just the next step.'),
    ('From chapter 3', 'Ask, don’t guess.', '<b>Found:</b> a headset read closed eyes on one stretch, then drifted, even with brain-wave rhythms.', '<b>In the apps:</b> the person says how they are. Nothing happens until they tap.'),
    ('From chapter 3', 'Expect change halfway.', '<b>Found:</b> within two minutes the brain-wave pattern for closed eyes changed.', '<b>In the apps:</b> Save &amp; pause, a note of where you stopped, break reminders.'),
    ('From real life', 'When stuck, make it smaller.', '<b>Seen:</b> a task too big all at once is where people stop.', '<b>In the apps:</b> “I’m stuck” makes the step smaller and keeps your place.'),
], 'rules')}""",
      "This is where the science turns into design. Each finding gives a rule, and each rule is a real feature in the apps.", "dense")
# 11
slide("ch4-screens", "Chapter 4: the rules on real screens in Next Step and Helper Jobs.", f"""
{head('Chapter 4 · On real screens', 'Two apps, built for real life.', 'Next Step, by Amishi Mehta, for schoolwork. Helper Jobs, a family project that gives neurodivergent adults one picture step at a time while they help at Pragnya’s Sunday outings for kids.')}
<ol class="landing-demo deck-shots">
{B.shot('../img/next-step-energy.jpg', 'Next Step energy check.', 'Show less when energy is low', 'The plan shrinks to one step.')}
{B.shot('../img/next-step-stuck.jpg', 'Next Step pause and I’m stuck.', 'Pause, and make it smaller', 'Your place is kept.')}
{B.shot('../img/helper-jobs-phone.jpg', 'Helper Jobs picture step.', 'One picture step, read aloud', 'With a Help button.')}
</ol>""",
      "Here they are. Next Step asks about energy and shrinks the plan. Save and pause and I’m stuck make it easy to stop and come back. Helper Jobs gives one picture step at a time, read aloud, with a Help button that reaches a volunteer.")
# 12
slide("ch5", "Chapter 5: the road ahead in four steps.", f"""
{head('Chapter 5 · Test, then go further', 'Where this goes next.')}
{cards([(k, h, a, b) for k, h, a, b in B.ROADMAP])}""",
      "Next, with an ASDRP mentor, we run the three remaining data experiments and write the first paper, on why the EEG drifts. Then design studies with the people the apps are for. Longer term, the joined-up question: do apps that adjust to how you feel help people learn?", "dense")
# 13
slide("close", "The loop, who did what, and where to see everything.", f"""
{head('Thank you', 'From neurons to next steps.')}
{answer('<b>The loop:</b> real life raised the question; the mouse showed that state changes what a brain takes in; the EEG showed that state is hard to read from outside; so the apps ask how someone is doing and keep each step small. <span>Three mice and one person are a start, not a rule for everyone.</span>')}
<div class="landing-facts"><div class="landing-fact"><h2>See it all</h2><p>Website: amishi123.github.io/neuroscience-project<br>Phone tour, slides, Next Step and Helper Jobs are all linked from there.</p></div><div class="landing-fact"><h2>Who did what</h2><p>The studies were done by Amishi with her father. Software tools, including AI assistants, helped build the site and the apps. Every number comes from saved results.</p></div></div>""",
      "To sum up the loop. Everything I showed is on the website, with the phone tour, these slides and both apps linked from it. Thank you.")

DECK_CSS = """html,body{margin:0;width:1000px;height:563px;overflow:hidden;background:var(--bg,#F3ECE1)}main#app{margin:0!important;padding:0!important;max-width:none!important;width:1000px}
.deck-slide{width:1000px;height:563px;max-width:none!important;margin:0!important;border:0!important;box-sizing:border-box;padding:30px 44px 38px;display:flex;flex-direction:column;justify-content:center;gap:4px;position:relative;overflow:hidden}
.deck-slide .landing-hero{gap:30px}.deck-slide h1{font-size:44px;line-height:1.08;margin:0 0 10px}.deck-slide .landing-hero h1{font-size:60px}
.deck-slide .hj-sub{font-size:17px;max-width:640px}.deck-slide .lm-head{margin-bottom:12px;align-items:center}.deck-slide .hj-art{max-width:250px}
.deck-slide .landing-problems{margin:6px 0}.deck-slide .lm-grid{margin-top:8px}.deck-slide .lm-grid li{padding:14px 16px}.deck-slide .lm-grid p{font-size:14px}
.deck-slide .chart-card{margin:8px 0 0}.deck-slide .landing-problems.answer.bridge{margin-top:14px}
.deck-slide .loop-figure{margin-top:10px}.deck-slide .landing-problems li{padding:14px 16px}.deck-slide .landing-problems .lp-pain,.deck-slide .landing-problems .lp-fix{font-size:14px}
.deck-shots{grid-template-columns:repeat(3,1fr)!important}.deck-shots img{max-height:330px;width:auto!important;max-width:100%;object-fit:contain}
.deck-foot{position:absolute;left:44px;right:44px;bottom:12px;display:flex;justify-content:space-between;font:600 11px/1 system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.deck-slide .family-links{display:none}
.deck-slide h1{font-size:34px!important}.deck-slide .landing-hero h1{font-size:54px!important}.deck-slide .hj-sub{font-size:15px}
.deck-slide .chart-card{grid-template-columns:1.3fr 1fr;padding:12px 16px;gap:18px;align-items:center}.deck-slide .chart-card svg.chart{max-height:215px;width:100%}.deck-slide .chart-card h3{font-size:19px}.deck-slide .chart-card p{font-size:13px}
.deck-slide .lp-energy{font-size:14px;padding:12px 16px}.deck-slide .deck-shots img{max-height:225px}.deck-slide .deck-shots strong{font-size:15px}.deck-slide .deck-shots span{font-size:12px}
.deck-slide.dense .landing-problems .lp-pain,.deck-slide.dense .landing-problems .lp-fix{font-size:12px;line-height:1.35}.deck-slide.dense .landing-problems h3{font-size:16px}
.deck-slide .lm-grid h3{font-size:17px}
.deck-slide .found3 ol{grid-template-columns:repeat(3,minmax(0,1fr))!important}.deck-slide .found3 h3{font-size:19px}.deck-slide .found3 .lp-pain{font-size:14px}.deck-slide .found3 .lp-pain b{color:var(--ink)}"""


def slide_html(i, s):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Slide {i}</title>
<link rel="stylesheet" href="../../assets/base.css"><link rel="stylesheet" href="../../assets/experience.css"><link rel="stylesheet" href="../../assets/theme-atlas.css"><link rel="stylesheet" href="../../assets/styles.css"><link rel="stylesheet" href="../../assets/charts.css">
<style>{DECK_CSS}</style></head><body><main id="app"><section class="screen active landing deck-slide {s['cls']}">{s['body'].replace('src="../img/', 'src="../../img/')}
<p class="deck-foot"><span>From neurons to next steps</span><span>{i} / {len(SLIDES)}</span></p></section></main>
<script src="../../assets/icons.js"></script><script src="../../assets/icons-extra.js"></script><script src="../../assets/art.js"></script><script src="../../assets/science-art.js"></script>
<script src="../../assets/results.js"></script><script src="../../assets/charts.js"></script><script src="../../assets/site.js"></script></body></html>"""


PPTX = "from-neurons-to-next-steps-slides.pptx"


def build_pptx(files):
    """A PowerPoint copy: each slide is the rendered picture, with its speaker notes, so it opens the
    same in PowerPoint, Keynote and Google Slides."""
    from pptx import Presentation
    from pptx.util import Emu
    deck = Presentation(); deck.slide_width, deck.slide_height = Emu(12192000), Emu(6858000)
    deck.core_properties.title = "From neurons to next steps"; deck.core_properties.author = "Amishi Mehta"
    for name, s in zip(files, SLIDES):
        sl = deck.slides.add_slide(deck.slide_layouts[6])
        pic = sl.shapes.add_picture(str(P / "slides" / f"{name}.jpg"), 0, 0, deck.slide_width, deck.slide_height)
        pic.name = s["alt"][:250]
        pic._element.nvPicPr.cNvPr.set("descr", s["alt"])
        sl.notes_slide.notes_text_frame.text = s["notes"]
    deck.save(P / PPTX)


def main():
    from playwright.sync_api import sync_playwright
    from PIL import Image
    src = P / "src"; out = P / "slides"; src.mkdir(exist_ok=True); out.mkdir(exist_ok=True)
    for old in out.glob("*.jpg"): old.unlink()
    for old in src.glob("*.html"): old.unlink()
    files = []
    for i, s in enumerate(SLIDES, 1):
        name = f"{i:02d}-{s['key']}"
        (src / f"{name}.html").write_text(slide_html(i, s)); files.append(name)
    with sync_playwright() as pw:
        b = pw.chromium.launch(args=["--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": 1000, "height": 563}, device_scale_factor=1.92)
        for name in files:
            pg.goto((src / f"{name}.html").as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(200)
            over = pg.evaluate("""() => { const s = document.querySelector('.deck-slide'); return s.scrollHeight > s.clientHeight + 1 || s.scrollWidth > s.clientWidth + 1 }""")
            if over: print("OVERFLOW", name)
            pg.screenshot(path=str(out / f"{name}.png"))
            Image.open(out / f"{name}.png").convert("RGB").save(out / f"{name}.jpg", quality=88, optimize=True); (out / f"{name}.png").unlink()
        b.close()
    imgs = [Image.open(out / f"{n}.jpg").convert("RGB") for n in files]
    imgs[0].save(P / PDF, save_all=True, append_images=imgs[1:], resolution=144)
    build_pptx(files)
    items = [{"src": f"slides/{n}.jpg", "alt": s["alt"], "notes": s["notes"]} for n, s in zip(files, SLIDES)]
    (P / "present.html").write_text(viewers.page("Slides · From neurons to next steps", "Slide", items, "./", "All slides", True, PDF))
    (P / "presenter.html").write_text(viewers.presenter(items))
    figs = "".join(f'<li><a href="present.html#{i}"><img src="slides/{n}.jpg" alt="Slide {i}: {html.escape(s["alt"])}" loading="{"eager" if i < 3 else "lazy"}" width="1920" height="1080" style="width:100%;height:auto;border:1px solid var(--line);border-radius:var(--radius-card)"></a><strong>{i} · {html.escape(s["alt"].split(":")[0])}</strong><span>{html.escape(s["alt"].split(":", 1)[-1].strip())}</span></li>' for i, (n, s) in enumerate(zip(files, SLIDES), 1))
    B.page("presentation/index.html", "Slides · From neurons to next steps", f"The {len(SLIDES)} slides for From neurons to next steps, with speaker notes.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{B.heading(('../index.html', 'All chapters'), 'The slides', f'<span id="page-title">The same story, in {len(SLIDES)} slides.</span>', 'Built from the same words, charts and drawings as the website. Present full screen, open the presenter view with speaker notes, or download the PDF.', 'loop')}
      <div class="landing-actions"><a class="button primary" href="present.html">Present <span aria-hidden="true">→</span></a><a class="button secondary" href="presenter.html">Presenter view with notes</a><a class="button secondary" href="{PDF}" download>Download PDF</a><a class="button secondary" href="{PPTX}" download>Download PowerPoint</a><a class="button secondary" href="../video/">Watch the video</a></div>
      <h2 class="landing-subhead">All {len(SLIDES)} slides</h2><ol class="landing-demo deck-list" aria-label="All slides" tabindex="0">{figs}</ol>
    </section>""", base="../")
    print("deck:", len(SLIDES), "slides")


if __name__ == "__main__":
    main()
