"""Builds the portfolio pages with the exact Helper Jobs / Next Step stylesheets, icons, illustrations and
markup (website/assets/base.css, experience.css, theme-atlas.css, styles.css, icons.js, art.js are copied
unchanged from neurocomms/helper-jobs). Only the charts are new (charts.css, charts.js).
Old page names redirect to the new ones. Run: python3 website/build_pages.py"""
from pathlib import Path

W = Path(__file__).resolve().parent
REPO = "https://github.com/AmishI123/neuroscience-project/tree/main/portfolio"
REPO_BLOB = "https://github.com/AmishI123/neuroscience-project/blob/main/portfolio/"
REPO_TREE = "https://github.com/AmishI123/neuroscience-project/tree/main/portfolio/"
FLAGSHIP = "https://github.com/AmishI123/neuroscience-project"
NEXT_STEP = "https://next-step-live.onrender.com/"
HELPER_JOBS = "https://helper-jobs.onrender.com"
SITE = "https://amishi123.github.io/neuroscience-project/"
N_SLIDES = len(list((Path(__file__).resolve().parent / "presentation/slides").glob("*.jpg")))


def ic(name):
    return f'<span class="lm-icon" data-icon="{name}"></span>'


def page(name, title, description, body, base="", extra_js="", manifest="", og_extra=""):
    url = SITE + str(Path(name)).replace("../communication/projects/neuroscience-mobile/", "neuroscience-mobile/").removesuffix("index.html")
    og = f"""<meta property="og:type" content="website" />
  <meta property="og:site_name" content="From neurons to next steps" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{SITE}presentation/slides/01-cover.jpg" />
  <meta property="og:image:width" content="1920" />
  <meta property="og:image:height" content="1080" />
  <meta property="og:image:alt" content="From neurons to next steps: an ASDRP neuroscience portfolio by Amishi Mehta." />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="canonical" href="{url}" />
  {og_extra}"""
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#F3ECE1" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  {og}
  {manifest}<link rel="icon" href="{base}assets/icon.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="{base}assets/base.css" />
  <link rel="stylesheet" href="{base}assets/experience.css" />
  <link rel="stylesheet" href="{base}assets/theme-atlas.css" />
  <link rel="stylesheet" href="{base}assets/styles.css" />
  <link rel="stylesheet" href="{base}assets/charts.css" />
</head>
<body>
  <aside class="public-demo-banner" aria-label="About this portfolio">ASDRP application portfolio · Public data only · Every number comes from saved results</aside>
  <a class="skip-link" href="#app">Skip to the page</a>
  <header>
    <a class="brand" href="{base}index.html"><span class="mark" aria-hidden="true">n.</span> From neurons to next steps</a>
    <span class="header-status"><span class="badge">Public data only</span><span class="badge">Future plans clearly marked</span></span>
    <a class="header-link" href="{REPO}">Source code</a>
  </header>
  <main id="app" tabindex="-1">
{body}
    <nav class="landing-note family-links" aria-label="Everything in this portfolio"><b>Everything in this portfolio:</b><a href="{SITE}share/">Share and demo</a><a href="{SITE}">The website</a><a href="{SITE}neuroscience-mobile/">Phone tour</a><a href="{SITE}presentation/">Slides</a><a href="{SITE}video/">Video</a><a href="{NEXT_STEP}">Next Step app</a><a href="{HELPER_JOBS}">Helper Jobs app</a><a href="{REPO}">Source code</a></nav>
  </main>
  <script src="{base}assets/icons.js"></script><script src="{base}assets/icons-extra.js"></script><script src="{base}assets/art.js"></script><script src="{base}assets/science-art.js"></script>
  <script src="{base}assets/results.js"></script><script src="{base}assets/charts.js"></script><script src="{base}assets/site.js"></script>{extra_js}
</body>
</html>
"""
    (W / name).parent.mkdir(parents=True, exist_ok=True)
    (W / name).write_text(html)


def heading(back, eyebrow, title, sub, art):
    return f"""    <div class="lm-head"><div class="hj-heading"><a class="back-button" href="{back[0]}">← <span>{back[1]}</span></a><p class="eyebrow">{eyebrow}</p><h1>{title}</h1><p class="hj-sub">{sub}</p></div><div class="hj-art" data-art="{art}"></div></div>"""


def chart(cid, kicker, title, text, note):
    return f'<div class="chart-card"><div data-chart="{cid}"></div><div><p class="lm-k">{kicker}</p><h3>{title}</h3><p>{text}</p><p class="chart-note">{note}</p></div></div>'


def grid(items):
    return '<ul class="lm-grid">' + "".join(f'<li><div class="lm-top">{ic(i)}<p class="lm-k">{k}</p></div><h3>{h}</h3><p>{p}</p></li>' for i, k, h, p in items) + "</ul>"


def shot(src, alt, cap, sub, width='100%'):
    return f'<li><img src="{src}" alt="{alt}" loading="lazy" style="width:{width};border:1px solid var(--line);border-radius:var(--radius-card)"><strong>{cap}</strong><span>{sub}</span></li>'


def phone(app, kicker, title, middle, cap, sub):
    return f'<li><div class="phone" aria-hidden="true"><div class="ph-bar"><span>{app}</span><em class="ph-picture-tag">Result</em></div><div class="ph-body"><p class="ph-k">{kicker}</p><p class="ph-title">{title}</p>{middle}</div></div><strong>{cap}</strong><span>{sub}</span></li>'


def bridge(label, text, href, link):
    return f'<section class="landing-problems answer bridge"><p class="lp-energy"><b>{label}</b> {text} <a href="{href}">{link} →</a></p></section>'


def nav(prev, nxt):
    home = '' if 'index.html' in (prev[0], nxt[0]) else '<a href="index.html">All chapters</a>'
    return f'<p class="landing-note"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a>{home}</p>'


# ---------------- landing ----------------
LANDING_ART = """<svg class="landing-art" viewBox="0 0 440 400" aria-hidden="true" focusable="false">
          <path class="la-line" d="M210 96 C 228 100, 222 120, 236 122"/><path class="la-line" d="M318 170 C 300 214, 250 204, 214 232"/><path class="la-line" d="M216 304 C 226 304, 228 302, 238 302"/>
          <g class="la-card" transform="translate(14 18) rotate(-2)"><rect width="196" height="104"/><rect class="la-top" width="196" height="5"/><text class="la-kick" x="14" y="26">1 · REAL LIFE</text><text class="la-title" x="14" y="56">Same room?</text><text class="la-small" x="14" y="80">One child dances, one</text><text class="la-small" x="14" y="94">covers their ears. Why?</text></g>
          <g class="la-card" transform="translate(234 66) rotate(2)"><rect width="192" height="104"/><text class="la-kick" x="14" y="24">2 · UNDERSTAND</text><text class="la-title" x="14" y="52">Picture + state</text><rect class="la-note" x="14" y="64" width="164" height="28"/><text class="la-k2" x="24" y="82">BETTER IN ALL 3 MICE</text></g>
          <g class="la-card la-ink" transform="translate(18 214) rotate(1.5)"><rect width="196" height="116"/><text class="la-kick" x="14" y="24">3 · MEASURE</text><text class="la-title" x="14" y="52">Eyes closed?</text><text class="la-k2" x="14" y="74">5 BLOCKS IN TIME</text><text class="la-body" x="14" y="94">The signal drifts.</text></g>
          <g class="la-card" transform="translate(238 236) rotate(-2)"><rect width="190" height="132"/><text class="la-kick" x="14" y="24">4 · DESIGN, THEN TEST</text><circle cx="30" cy="54" r="14"/><path class="la-tick" d="M24.5 54l3.5 3.5 7-7"/><text class="la-title" x="52" y="60">Ask, don’t guess</text><rect class="la-pill" x="14" y="88" width="72" height="22" rx="11"/><text class="la-pt" x="50" y="103" text-anchor="middle">Next Step</text><rect class="la-pill" x="92" y="88" width="82" height="22" rx="11"/><text class="la-pt" x="133" y="103" text-anchor="middle">Helper Jobs</text></g>
        </svg>"""

page("index.html", "From neurons to next steps · an ASDRP neuroscience portfolio",
     "In mice, brain cells reacted differently to the same picture depending on how alert the mouse was; a brain-wave headset could not reliably tell even whether eyes were open or closed; so a helpful app asks how you feel and shows one small step at a time. Two studies and two apps by Amishi Mehta.", f"""    <section id="home" class="screen active landing" aria-labelledby="home-title">
      <div class="landing-hero">
        <div class="landing-hero-text">
          <p class="landing-kicker">An ASDRP neuroscience portfolio · Amishi Mehta</p>
          <h1 id="home-title">From neurons to next steps</h1>
          <p class="landing-lede">It started at Pragnya, where Amishi volunteers with neurodivergent children: in one session, one child was dancing while another covered their ears in the same room. <b>Is that the brain’s state?</b> Two studies with public brain recordings and two apps later, here is what we found, in three sentences.</p>
          <p class="landing-lede" style="font-size:1rem">Amishi wants to understand what physically changes in neurons when a brain’s state shifts, on the way to a career as a nurse anesthetist.</p>
          <div class="landing-actions">
            <a class="button primary" href="#found">What we found <span aria-hidden="true">→</span></a>
            <a class="button secondary" href="#story">The whole story</a>
          </div>
          <p class="landing-try-note">Also as <a href="presentation/">slides</a>, a <a href="video/">short video</a> and a <a href="neuroscience-mobile/">phone tour</a>, all on <a href="share/">one page to share</a>. Public data only. Predicting something is not the same as knowing its cause.</p>
        </div>
        {LANDING_ART}
      </div>

      <section class="landing-problems" id="found" aria-labelledby="found-title">
        <h2 class="landing-subhead" id="found-title">What we found, in three sentences</h2>
        <p class="lp-lead">The question: does how alert you are change what your brain takes in, and can a device measure it? Each answer links to its evidence.</p>
        <ol aria-label="Three findings" tabindex="0">
          <li><p class="lp-k">1 · The mouse study</p><h3>In mice, brain cells reacted differently to the very same picture depending on how alert the mouse was.</h3><p class="lp-pain">We used public recordings of thousands of brain cells in three mice. Adding how alert each mouse was (its pupil size and running speed) made our predictions of the cells <b>25–33% better</b>, in all three.</p><p class="lp-fix"><a href="mouse.html">The mouse study →</a></p></li>
          <li><p class="lp-k">2 · The brain-wave study</p><h3>A brain-wave headset on a person could not reliably tell even whether their eyes were open or closed.</h3><p class="lp-pain">We used a public recording of one person. A computer learned to spot closed eyes from the brain waves, but within two minutes it was <b>no better than flipping a coin</b>, even with a smarter method.</p><p class="lp-fix"><a href="eeg.html">The EEG study →</a></p></li>
          <li><p class="lp-k">3 · The app</p><h3>So a helpful app should not try to read your brain: it should ask how you feel and show one small step at a time.</h3><p class="lp-pain">Next Step, Amishi’s app for students, asks <b>“How much energy do you have today?”</b> On a low day it shows only the next step, so nothing has to guess.</p><p class="lp-fix"><a href="tools.html">The design →</a></p></li>
        </ol>
        <p class="lp-energy"><b>What comes next:</b> test whether that actually helps the people the apps are for, and take the science further with an ASDRP mentor. <a href="next.html">The plan →</a></p>
      </section>

      <section class="landing-more" id="vision" aria-labelledby="vision-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="vision-title">The big picture</h2><p class="lp-lead">Instructions, apps and classrooms often assume a brain is always ready to take things in. It is not.</p><p class="vision-sub">So this work asks three questions in order: how much does a brain’s state (how alert, tired or calm it is) change what it takes in, can a device measure that state, and how do we build tools that work either way? Then it checks whether those tools actually help.</p></div><div class="hj-art" data-art="family"></div></div>
        {grid([
            ('brain', 'Understand', 'How much does alertness change what the brain takes in?', 'A mouse study and a brain-wave (EEG) study. Each was tested on recordings the computer had not seen, and checked in ways that could have proved it wrong.'),
            ('heart-handshake', 'Design', 'Tools that work on good days and bad days', 'Ask how someone is doing instead of guessing, show one step at a time, and make pausing easy.'),
            ('users', 'Help', 'With the people they are for', 'Next Step for students and Helper Jobs for Pragnya’s Sunday outings, tested with the people who use them next.'),
        ])}
        <p class="vision-sub"><b>Where it leads:</b> a research path that uses brain science to design apps that work for real people.</p>
      </section>

      <section class="landing-problems" id="story" aria-labelledby="landing-problems-title">
        <h2 class="landing-subhead" id="landing-problems-title">One loop, five chapters</h2>
        <p class="lp-lead">It starts in real life and ends back there. Each chapter answers the question the last one raised.</p>
        <div class="loop-figure"><div class="loop-wide" data-art="loop"></div><div class="loop-tall" data-art="loopTall"></div></div>
        <ol aria-label="Five chapters" tabindex="0">
          <li><p class="lp-k">1 · Real life</p><h3>Same words, different moment.</h3><p class="lp-pain">It started at Pragnya, where one child was dancing while another covered their ears in the same room. A step that is easy when you are calm can be lost when you are tired, rushed or overloaded. Is that the brain’s state?</p><p class="lp-fix"><b>To find out:</b> look inside a brain while its state changes.</p></li>
          <li><p class="lp-k">2 · Understand</p><h3>How alert a mouse is changes how its brain responds to what it sees.</h3><p class="lp-pain">Mice watched pictures while thousands of brain cells were recorded. We guessed what each cell would do from the picture alone, then from the picture plus how alert and active the mouse was.</p><p class="lp-fix"><b>Found:</b> knowing the mouse’s state made our guesses 25–33% better, in all three mice. <a href="mouse.html">Read chapter 2 →</a></p></li>
          <li><p class="lp-k">3 · Measure</p><h3>Can a brain-wave headset tell when a person’s eyes are closed?</h3><p class="lp-pain">A cap of 14 sensors on one person’s head for two minutes (EEG). Closing your eyes is one of the clearest changes it picks up. Can a simple model tell when?</p><p class="lp-fix"><b>Found:</b> on one stretch it scored 0.625 (0.5 is a coin flip, 1 is always right). Across the whole recording it fell to 0.478, about a coin flip. A smarter method using brain-wave rhythms scored 0.566, but still fell below a coin flip on some stretches. <a href="eeg.html">Read chapter 3 →</a></p></li>
          <li><p class="lp-k">4 · Design</p><h3>From findings to features.</h3><p class="lp-pain">If alertness matters but a headset cannot reliably measure it, an app should ask, not guess. It should show less on a low-energy day, and make pausing and coming back easy.</p><p class="lp-fix"><b>Built into:</b> Next Step, by Amishi Mehta, for schoolwork, and Helper Jobs, a family project that gives neurodivergent adults one picture step at a time while they help at Pragnya’s Sunday outings for kids. <a href="tools.html">Read chapter 4 →</a></p></li>
          <li><p class="lp-k">5 · Test, then go further</p><h3>Where this goes next.</h3><p class="lp-pain">One follow-up experiment is done. Next: three more experiments on the same public data, testing the apps with Pragnya volunteers and families, and write-ups others can check.</p><p class="lp-fix"><b>The aim:</b> a research path that uses brain science to design apps that work for real people. <a href="next.html">Read chapter 5 →</a></p></li>
        </ol>
        <p class="lp-energy"><b>In short:</b> how alert you are changes what your brain takes in, a headset could not reliably measure it, so a good app asks and keeps steps small. <span>Three mice and one person are a start, not a rule for everyone.</span></p>
        <div class="lp-how"><p class="lp-how-short"><b>What this does not show yet:</b> whether the pattern holds in more animals and more people, what causes it, or whether the apps help. Each of those is an experiment in chapter 5.</p></div>
      </section>

      <section class="landing-more" id="checks" aria-labelledby="landing-more-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="landing-more-title">How we tried to break each result</h2><p class="lp-lead">Nothing in the story counts until it has survived a check that could have made it disappear.</p></div><div class="hj-art" data-art="controls"></div></div>
        {grid([
            ('arrows-shuffle', 'Mix up the answers', 'It should fail, and it does', 'If we scramble which moments were eyes-closed, the model drops to a coin flip. If we scramble the mouse’s state, the gain disappears. So the results come from the recordings, not from chance.'),
            ('timeline', 'Never peek at the future', 'Learn from earlier, test on later', 'The model only ever learns from the past and is tested on what comes after, the way a real app would have to work.'),
            ('route-2', 'Leave a gap', 'No help from next-door moments', 'Moments right next to each other look alike. We leave a gap between what the model learns from and what it is tested on.'),
            ('users', 'Leave one mouse out', 'No single mouse carries it', 'Take any one mouse away and the other two still show the gain.'),
            ('filter', 'Look for glitches', 'Four found and trimmed', 'Four sensor readings were glitches, up to 180 times bigger than normal. Trimming them helped one test, but the computer still lost track over time.'),
            ('code', 'Every number traced', 'Rebuilt from saved results', 'Every chart is drawn from the saved results files, and the EEG study reruns with one command.'),
        ])}
      </section>


      <div class="landing-facts">
        <div class="landing-fact"><h2>Who did what</h2><p>Amishi did most of the work on the studies, with advice and guidance from her father, who helped shape the questions, review the code and fix problems. Software tools, including AI assistants, helped build this website and the apps. The <a href="{REPO_BLOB}application/contribution-ledger.md">contribution ledger</a> lists each part.</p></div>
        <div class="landing-fact landing-fact-not"><h2>What it is not</h2><p>It is not a medical study and it does not diagnose anyone. Three mice and one person cannot speak for everyone, and being able to predict something is not the same as knowing what causes it.</p></div>
      </div>
      <p class="landing-note">Data: Sensorium 2022 (Willeke et al., 2022) and UCI EEG Eye State (Roesler, 2013). <a href="mouse.html">Mouse study</a><a href="eeg.html">EEG study</a><a href="tools.html">Design</a><a href="next.html">What’s next</a></p>
    </section>""")

# ---------------- mouse ----------------
page("mouse.html", "Understand · mouse study · From neurons to next steps",
     "Chapter 2: knowing how alert and active a mouse was made its brain’s response to pictures 25–33% easier to predict, in all three mice.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'All chapters'), 'Chapter 2 · Understand · Mouse study', '<span id="page-title">Does how alert a mouse is change how its brain responds to what it sees?</span>', 'Mice watched pictures while scientists recorded thousands of brain cells in the part of the brain that handles seeing. We tried to guess what each cell would do, first from the picture alone, then from the picture plus two signs of the mouse’s state: how wide its pupils were and how fast it was running. If state did not matter, the extra signs would not help.', 'mouseHero')}
      <section class="landing-problems answer"><p class="lp-energy"><b>It mattered, in all three mice.</b> Knowing the mouse’s state made our guesses a quarter to a third better (25–33%), on pictures the model had never seen. <span>This shows state and seeing are linked. It does not yet show which causes which.</span></p></section>

      <section class="landing-more" aria-labelledby="how-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="how-title">How we tested it</h2><p class="lp-lead">Two guessers, the same pictures, and a fair test on pictures neither had seen.</p></div><div class="hj-art" data-art="mouseStudy"></div></div>
        {grid([
            ('photo', 'Step 1', 'What the mouse saw', 'Each picture is shrunk to a short summary of its light and dark patterns, so a simple model can use it.'),
            ('eye', 'Step 2', 'What state it was in', 'Pupil size (wider usually means more alert) and running speed, recorded at the same moment as the brain cells.'),
            ('chart-dots', 'Step 3', 'Two simple guessers', 'Guesser A sees only the picture. Guesser B sees the picture plus pupil and running. Both are the simplest kind of model: each clue gets a weight, and the weights are added up.'),
            ('target', 'Step 4', 'A fair test', 'Both guess how each brain cell responds to pictures they have never seen. We score how closely each guess follows the real cell.'),
            ('books', 'The data', 'A public dataset', 'Sensorium 2022: recordings of thousands of brain cells from mice watching pictures, shared by scientists for anyone to study.'),
            ('users', 'Being fair', 'Each mouse counts once', 'The many brain cells in one mouse are not counted as many mice.'),
        ])}
      </section>

      <h2 class="landing-subhead">The results</h2>
      {chart('mouse-scale', 'How to read the score', 'How closely the guess follows the real brain cell.', '0 means the guess and the cell have nothing in common; 1 would be a perfect match. Brain cells are noisy, so even good guesses score low. What matters is the jump from A to B.', 'The score is a correlation, averaged over every recorded brain cell.')}
      {chart('mouse-scores', 'Result', 'Every mouse is easier to predict once we know its state.', 'The picture explains part of what the seeing part of the brain does. Whether the mouse is alert and moving explains more, in every animal.', 'Tested on pictures the guessers never saw.')}
      {chart('mouse-gain', 'How much state adds', 'Every mouse gains, by different amounts.', 'Pupil size helps all three mice. How much running adds changes from mouse to mouse, so each mouse is shown on its own.', 'Gain = guesser B’s score minus guesser A’s score.')}

      <h2 class="landing-subhead" id="inside-title">Inside the first mouse</h2><p class="landing-demo-note">From Amishi’s saved results and report in <a href="{FLAGSHIP}">AmishI123/neuroscience-project</a>, redrawn here. These are for the first mouse only.</p>
      <div class="tour-nums inside-nums"><p><b>90%</b><span>of brain cells were guessed better once state was added</span></p><p><b>+0.017</b><span>typical gain per cell (the middle value)</span></p><p><b>+0.35</b><span>the biggest gain for a single cell</span></p></div>
      {chart('mouse1-ablation', 'Which part of state?', 'It is the pupil, not the running.', 'Adding running barely moved the score. Adding pupil size gave almost the whole gain. This mouse ran on only about 5% of trials, so running had little to say.', 'Score on unseen pictures, first mouse.')}
      {chart('mouse1-cells', 'Which cells gain?', 'The cells that follow alertness gain most.', 'Cells whose activity rises or falls with pupil size gained about five times as much as the rest.', 'A cell “follows pupil” when its activity and pupil size move together (correlation above 0.1), as in Amishi’s report.')}
      {chart('mouse1-cell', 'One cell', 'From nearly unpredictable to predictable.', 'Brain cell 3035 was almost impossible to predict from the picture alone. Knowing the mouse’s state raised its score from 0.05 to 0.40.', 'Score for this one cell on unseen pictures.')}

      <section class="landing-more" aria-labelledby="checks-title" id="checks">
        <div class="lm-head"><div><h2 class="landing-subhead" id="checks-title">Trying to break the result</h2><p class="lp-lead">Three checks that could have made the gain disappear. It survived all three.</p></div><div class="hj-art" data-art="controls"></div></div>
        {grid([
            ('arrows-shuffle', 'Mix up the state', 'The gain disappears', 'We gave guesser B the pupil and running from the wrong moments, 20 times per mouse. It added nothing. The gain needs the mouse’s state at that moment.'),
            ('users', 'Leave one mouse out', 'Still there', 'Take any one mouse away and the other two still show the gain, so no single mouse carries the result.'),
            ('eye', 'Pupil or running?', 'Pupil helps every mouse', 'Taking each sign away in turn: pupil helps all three mice; running helps some more than others.'),
        ])}
      </section>
      {chart('mouse-loo', 'Leave one mouse out', 'The gain stays without any one mouse.', 'So the pattern does not hang on one recording. It is a check, not a promise about all mice.', 'Average gain over the two mice that are left.')}

      <div class="landing-facts" style="margin-top:28px">
        <div class="landing-fact"><h2>Code and data</h2><p>The analysis is in <a href="{FLAGSHIP}">AmishI123/neuroscience-project</a> (her notebooks 01–05). The numbers on this page are copied from its saved results, and an automatic check confirms they still match. Data: Willeke et al. (2022), <i>The Sensorium competition on predicting large-scale mouse primary visual cortex activity</i>, arXiv:2206.08666.</p></div>
        <div class="landing-fact landing-fact-not"><h2>What it does not show</h2><p>Three mice cannot speak for all mice. A better guess does not show that being alert or running causes the brain to change. Other things that happen at the same time could explain it.</p></div>
      </div>
      {bridge('What chapter 2 tells us:', 'the same picture lands differently depending on the state the mouse is in. So the next question: can a brain-wave headset measure that in a person?', 'eeg.html', 'Chapter 3')}
      {nav(('index.html', 'All chapters'), ('eeg.html', 'Chapter 3 · EEG'))}
    </section>""")

# ---------------- EEG ----------------
page("eeg.html", "Measure · EEG study · From neurons to next steps",
     "Chapter 3: a simple model reads eye state from one person’s EEG on one stretch of time, but not reliably across the recording, because the signal drifts.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'All chapters'), 'Chapter 3 · Measure · EEG study', '<span id="page-title">Can sensors on the head tell when someone’s eyes are closed?</span>', 'EEG is a cap of small sensors that pick up the brain’s electrical activity through the scalp. Closing your eyes is one of the clearest changes it can see. If a simple model cannot read even that reliably for two minutes, quieter states like tiredness will be harder still.', 'eegHero')}
      <section class="landing-problems answer"><p class="lp-energy"><b>On one stretch, yes. Over time, no.</b> On the last part of the recording the model scored 0.625 (0.5 is a coin flip, 1 is always right), and 0.728 once four glitchy readings were trimmed. But tested on five stretches across the recording, it averaged 0.478: about a coin flip. <span>Letting it see the last few moments as well did not help.</span></p></section>

      <section class="landing-more" aria-labelledby="how-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="how-title">How we tested it</h2><p class="lp-lead">Learn from earlier in the recording, then test on what comes later, like a real app would have to.</p></div><div class="hj-art" data-art="eegStudy"></div></div>
        {grid([
            ('activity', 'The recording', 'One person, two minutes', '14 sensors, about 128 readings a second. Each moment is marked eyes open or eyes closed (closed about 45% of the time).'),
            ('timeline', 'Learn, then test', 'Earlier, then later', 'The model learns from the first 70% of the recording, is checked on the next 15%, and is tested once on the last 15%.'),
            ('chart-dots', 'Two models', 'Now, or now plus a moment ago', 'One sees a single moment. The other also sees the last 9 readings, about a fourteenth of a second.'),
            ('target', 'The score', '0.5 is a coin flip', 'How often the model ranks an eyes-closed moment above an eyes-open one. 0.5 is guessing, 1.0 is always right.'),
            ('route-2', 'Five stretches', 'Moving forward in time', 'Learn from everything before a stretch, test on that stretch, and repeat five times across the recording.'),
            ('books', 'The data', 'A public recording', 'UCI EEG Eye State (Roesler, 2013), shared for anyone to study.'),
        ])}
      </section>

      <h2 class="landing-subhead">The results</h2>
      {chart('eeg-scale', 'How to read the score', 'Where the results sit between guessing and always right.', 'Anything near 0.5 is no better than flipping a coin. Below 0.5 means the model is wrong more often than right, so the pattern it learned has flipped.', 'The score is called AUC.')}
      {chart('eeg-holdout', 'The last stretch', 'Good on one stretch, better once glitchy readings are trimmed.', 'Four readings were glitches: up to 715,897 when normal is about 4,000. Trimming each sensor to the range seen while learning lifts the score from 0.625 to 0.728.', 'We added this check after the first results, so the new numbers sit next to the old ones, not in place of them.')}
      {chart('eeg-folds', 'Five stretches in time', 'Across the recording, it drifts to a coin flip.', 'Scores land on both sides of 0.5, and some fall well below it. Being worse than guessing means the pattern the model learned earlier had flipped by later on.', 'So the signal drifts within two minutes. Trimming glitchy readings and leaving a gap do not fix it.')}

      <section class="landing-more" aria-labelledby="checks-title" id="checks">
        <div class="lm-head"><div><h2 class="landing-subhead" id="checks-title">Making sure it is not our mistake</h2><p class="lp-lead">Three checks that the result comes from the recording, not from how we handled it.</p></div><div class="hj-art" data-art="controls"></div></div>
        {grid([
            ('arrows-shuffle', 'Mix up the answers', 'Scores 0.499, a coin flip', 'With eyes open and closed scrambled 20 times, the model scores a coin flip, as it should. Our method does not invent a pattern.'),
            ('route-2', 'Leave a gap', 'Scores 0.448, still near guessing', 'We left out the moments just before each test stretch, so the model could not lean on near-copies. The result stays near a coin flip.'),
            ('filter', 'Trim glitchy readings', 'Four readings, trimmed fairly', 'The limits come only from the part the model learns from, so the test part never shapes them.'),
        ])}
      </section>
      {chart('eeg-windows', 'How far back to look', 'Looking further back seems to help, but we did not pick a winner.', 'We chose to try 3, 9, 30 and 90 readings back before seeing any results. Ninety does best on average, but picking it now would mean tuning to this one recording.', 'Next: compare these on new recordings before choosing.')}

      <section class="landing-more" aria-labelledby="bands-title" id="bands">
        <div class="lm-head"><div><h2 class="landing-subhead" id="bands-title">Experiment 2: would brain-wave rhythms hold steady?</h2><p class="lp-lead">Alpha waves grow when eyes close. So we asked a follow-up question, wrote the plan down before running it, and tested it the same way.</p></div><div class="hj-art" data-art="eegStudy"></div></div>
        {grid([
            ('activity', 'The idea', 'Strength over the last second', 'Instead of the raw reading at one moment, the model sees how strong four kinds of brain wave were over the last second, including alpha.'),
            ('route-2', 'The test', 'Same five stretches, plus a gap', 'Learn from earlier, test on later, with one second left out between them, because the one-second windows overlap.'),
            ('target', 'The rule set beforehand', 'Better on average, never below 0.5', 'It counts as holding up only if it beats the raw readings on average and no stretch falls below a coin flip.'),
        ])}
      </section>
      <section class="landing-problems answer"><p class="lp-energy"><b>Better on average, but it still did not hold up.</b> All four rhythms averaged <b>0.566</b> across the five stretches, against <b>0.481</b> for the raw readings. But two stretches still dipped just below a coin flip (0.492 and 0.493), so by the rule we set beforehand it did not hold up. Alpha alone did worse (0.442). <span>Mixing up the answers gave 0.500, as it should.</span></p></section>
      {chart('eeg-bands', 'Experiment 2', 'Brain-wave rhythms help, but not enough to rely on.', 'Rhythms lift the average and the worst stretch, but a model that is sometimes worse than guessing is still not something to build an app on. This is why the apps ask the person.', 'With a one-second gap between learning and testing. Without the gap: 0.571 for rhythms, 0.529 for raw readings. Plan written before running: EXPERIMENT-2-PLAN.md in the source code.')}

      <div class="landing-facts" style="margin-top:28px">
        <div class="landing-fact"><h2>Rerun it</h2><p><code>python3 projects/eeg-eye-state/src/analyze.py</code> writes <code>results/metrics.json</code>, <code>src/analyze_bands.py</code> writes <code>results/bands.json</code> for experiment 2, and <code>python3 website/build_results.py</code> turns it into these charts. See the <a href="{REPO_BLOB}projects/eeg-eye-state/report.md">full report</a>. Data: Roesler, O. (2013). <i>EEG Eye State</i>. UCI Machine Learning Repository, doi:10.24432/C57G7J.</p></div>
        <div class="landing-fact landing-fact-not"><h2>What it does not show</h2><p>One person and one short recording cannot show how this works for other people. The only thing measured is eyes open or closed, not attention, tiredness or any condition.</p></div>
      </div>
      {bridge('What chapter 3 tells us:', 'a sensor that is right on one stretch and wrong on the next, even using brain-wave rhythms, is not something to build a tool on. So the apps ask the person instead of guessing.', 'tools.html', 'Chapter 4')}
      {nav(('mouse.html', 'Chapter 2 · Mouse'), ('tools.html', 'Chapter 4 · Design'))}
    </section>""")

# ---------------- tools ----------------
page("tools.html", "Design · From neurons to next steps",
     "Chapter 4: what the two studies found, the design rule each finding gives, and where that rule lives in Next Step and Helper Jobs.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'All chapters'), 'Chapter 4 · Design · Human–computer interaction', '<span id="page-title">From findings to features.</span>', 'Chapter 2 showed that how alert a brain is changes what gets through. Chapter 3 showed that a brain-wave headset could not reliably tell even whether someone’s eyes were closed. Each finding became a design rule, and each rule is a real feature in two working apps.', 'tablets')}
      <section class="landing-problems" id="rules" aria-labelledby="rules-title">
        <h2 class="landing-subhead" id="rules-title">Four findings, four design rules</h2>
        <p class="lp-lead">Read each card top to bottom: what we found, the rule it gives, and where the rule lives.</p>
        <ol aria-label="Findings, rules and features" tabindex="0">
          <li><p class="lp-k">From chapter 2</p><h3>Show less when energy is low.</h3><p class="lp-pain"><b>Found:</b> the same picture lands differently depending on the brain’s state.</p><p class="lp-fix"><b>In the apps:</b> Next Step asks “How much energy do you have today?” On “A little”, it shows just the next step. Helper Jobs shows one picture step at a time, read aloud.</p></li>
          <li><p class="lp-k">From chapter 3</p><h3>Ask, don’t guess.</h3><p class="lp-pain"><b>Found:</b> a headset read whether eyes were closed on one stretch, then drifted to a coin flip. Brain-wave rhythms did not fix it.</p><p class="lp-fix"><b>In the apps:</b> the person tells the app how they are doing. The energy check is optional, Help is a button they press, and nothing happens until they tap.</p></li>
          <li><p class="lp-k">From chapter 3</p><h3>Expect change halfway through.</h3><p class="lp-pain"><b>Found:</b> within two minutes, the brain-wave pattern for closed eyes had changed.</p><p class="lp-fix"><b>In the apps:</b> Next Step has Save &amp; pause, a note of where you stopped, and “Pick up where you left off”. Helper Jobs reminds helpers to take breaks.</p></li>
          <li><p class="lp-k">From real life</p><h3>When stuck, make it smaller.</h3><p class="lp-pain"><b>Seen:</b> a task that is too big all at once is where people stop.</p><p class="lp-fix"><b>In the apps:</b> Next Step’s “I’m stuck” offers to make the step smaller, ask a question or take a break. Nothing is sent, and your place is kept.</p></li>
        </ol>
      </section>
      <h2 class="landing-subhead">The rules, on real screens</h2><p class="landing-demo-note">Screens from the working apps, with made-up examples.</p>
      <ol class="landing-demo" aria-label="App screens" tabindex="0">
        {shot('img/next-step-energy.jpg', 'Next Step asks how much energy you have today: a little, some or plenty. A little shows just the next step.', 'Show less when energy is low', 'The person picks their energy; the plan shrinks to one step.', '78%')}
        {shot('img/next-step-stuck.jpg', 'Next Step step screen with Save and pause, a note for where I paused, and I’m stuck options: make it smaller, ask a question, see how others began, take a break.', 'Pause, and make it smaller', 'Save &amp; pause keeps your place; “I’m stuck” shrinks the step.', '78%')}
        {shot('img/helper-jobs-phone.jpg', 'A Helper Jobs step with a real photo of the place, a few words and Read aloud.', 'One picture step, read aloud', 'A few words, a photo of the real place, and a Help button.', '62%')}
      </ol>
      <section class="landing-problems two" aria-labelledby="apps-title">
        <h2 class="landing-subhead" id="apps-title">Two apps, built for real life</h2>
        <p class="lp-lead">Both follow the same rules: one step on the screen, big type, a picture, read aloud, and only made-up people in the examples.</p>
        <ol aria-label="Two apps" tabindex="0">
          <li><p class="lp-k">By Amishi Mehta · for schoolwork</p><h3>Next Step</h3><p class="lp-pain">For young people who find long instructions, interruptions or explaining their needs hard. Made with neurodivergent students in mind.</p><p class="lp-fix"><b>What it does:</b> turns a long assignment into one next step, practises words for asking for help, and keeps a note of where to restart. <a href="{NEXT_STEP}">Open Next Step →</a> <a href="{NEXT_STEP}presentation/">Its slides and handout →</a></p></li>
          <li><p class="lp-k">Family project · for Pragnya outings</p><h3>Helper Jobs</h3><p class="lp-pain">Built to give neurodivergent adults a real job at kids’ Sunday outings, with a volunteer always close by.</p><p class="lp-fix"><b>What it does:</b> picture steps read aloud in English, Hindi or Spanish, break reminders, and Help that reaches the lead’s phone in about a second. <a href="{HELPER_JOBS}">Open Helper Jobs →</a> <a href="{HELPER_JOBS}/presentation/">Its slides and handout →</a></p></li>
        </ol>
      </section>
      <div class="landing-facts">
        <div class="landing-fact"><h2>The loop on a phone</h2><p>The <a href="neuroscience-mobile/">phone tour</a> tells the same five chapters, one screen at a time, in the same design as the apps.</p></div>
        <div class="landing-fact landing-fact-not"><h2>Careful claims</h2><p>The studies suggest these rules; they do not prove the apps work. These are early test versions with made-up people in every example, not tested in a formal study, and they do not diagnose or treat anything.</p></div>
      </div>
      {bridge('Closing the loop:', 'do these designs actually help the people they are for? That is where the research goes next.', 'next.html', 'Chapter 5')}
      {nav(('eeg.html', 'Chapter 3 · EEG'), ('next.html', 'Chapter 5 · What’s next'))}
    </section>""")

# ---------------- next ----------------
EXPS = [
    ("flask", "1 · Tried · tests chapter 2", "Does the timing matter?", "Does the mouse’s state at that exact moment help more than its state a little earlier or later? We ran it on the first mouse: any shift erased the gain, but this dataset stores trials in shuffled order, so a shift is not a step in time. A real test needs the original trial timestamps."),
    ("activity", "2 · Done · tests chapter 3", "Brain-wave rhythms", "Rhythms did better on average (0.566 against 0.481) but two of five stretches still fell just below a coin flip, so by the rule set beforehand it did not hold up. See chapter 3."),
    ("brain", "3 · Planned · tests chapter 2", "Which brain cells change?", "Does alertness change every brain cell a little, or a few groups a lot? A first look at the first mouse found no clear pattern by where the cells sit. Groups are chosen before looking. Needs the full mouse recordings."),
    ("timeline", "4 · Started · tests chapter 3", "Why does it drift?", "How quickly does the eyes-closed pattern change, and can the model keep up if it keeps learning? The stretch-by-stretch scores and the glitch check are done."),
    ("users", "5 · Planned · closes the loop", "Do the apps help?", "Back to real life: do the four design rules make tasks easier to finish, for the people the apps are for? Needs consent, a task list written in advance and no personal data beyond what the test needs."),
]
ROADMAP = [
    ("Now · done", "Two studies, one follow-up, two apps.", "The mouse and EEG studies, every result checked and rerunnable, plus experiment 2 on brain-wave rhythms. Next Step and Helper Jobs working, with the four design rules built in.", "<b>Shown:</b> on this site, in the slides and in the phone tour."),
    ("Next · with an ASDRP mentor", "Run the remaining data experiments.", "Why the EEG drifts (experiment 4), using the data already here. Then groups of brain cells (experiment 3) in the full mouse recordings, and timing (experiment 1) if recordings with real trial timestamps can be found.", "<b>Aim:</b> a first paper, on why the EEG drifts and what brain-wave rhythms can and cannot fix, for a student research journal such as the <i>Journal of Emerging Investigators</i>, plus a poster."),
    ("Then · with people", "Study the design with the people it is for.", "Design sessions where Pragnya volunteers and families shape the apps, then a test of whether the four design rules make tasks easier. Consent first, and tasks written down before anyone takes part.", "<b>Aim:</b> a second paper, on the design rules, and better apps."),
    ("Longer term · the joined-up question", "Do apps that adjust to how you feel help people learn?", "Compare the energy-aware design with a fixed one, for the same person over several weeks. Then ask whether the brain findings predict who it helps most.", "<b>Aim:</b> a research path that uses brain science to design apps that work for real people."),
]
OUTPUTS = [
    ("books", "Papers", "Write-ups others can check", "Every study ends in a paper with its code, data links and limits, aimed at student journals and science fairs."),
    ("presentation", "Posters and talks", "Said out loud", "The same slides and charts as this site, for symposiums and science fairs."),
    ("code", "Open tools", "Anyone can rerun it", "Every analysis reruns with one command, and the apps stay open source."),
    ("heart-handshake", "Better apps", "Back to real life", "Each design study changes the apps, and each change is tested again."),
    ("route-2", "A design guide", "Rules others can use", "A short, plain guide to designing for good days and bad days, built only from findings that held up."),
    ("users", "Community", "Built with people, not for them", "Pragnya volunteers and families help decide what gets built and what gets tested."),
]
page("next.html", "Where this goes next · From neurons to next steps",
     "Chapter 5: the research plan. One follow-up done, three more data experiments, design studies with the people the apps are for, and papers others can check.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'All chapters'), 'Chapter 5 · Test, then go further', '<span id="page-title">Where this goes next.</span>', 'The loop does not stop at two studies and two apps. Each turn adds a study, a better design and a write-up others can check. Anything not yet done is labelled as a plan.', 'plan')}
      <section class="landing-problems" id="roadmap" aria-labelledby="road-title">
        <h2 class="landing-subhead" id="road-title">The road ahead</h2>
        <p class="lp-lead">Each step builds on the last: data first, then people, then the two together.</p>
        <ol aria-label="Research plan" tabindex="0">
          {''.join(f'<li><p class="lp-k">{k}</p><h3>{h}</h3><p class="lp-pain">{pn}</p><p class="lp-fix">{fx}</p></li>' for k, h, pn, fx in ROADMAP)}
        </ol>
      </section>
      <section class="landing-more" aria-labelledby="exp-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="exp-title">The next five experiments</h2><p class="lp-lead">One for each link in the loop, with the same steps as chapters 2 and 3.</p></div></div>
        {grid(EXPS)}
      </section>
      <section class="landing-more" aria-labelledby="out-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="out-title">What each turn of the loop produces</h2><p class="lp-lead">Not just results: things other people can read, check and use.</p></div></div>
        {grid(OUTPUTS)}
      </section>
      <p class="lp-energy"><b>The rule we keep:</b> a plan stays labelled as a plan until it has code, saved results, a rerun record, its limits written down and a page like the two studies. <span>No paper, poster or result is listed as done before it is.</span></p>
      {nav(('tools.html', 'Chapter 4 · Design'), ('index.html', 'Back to the start'))}
    </section>""")

# ---------------- the phone tour: the same five chapters, one screen at a time ----------------
TOUR = [
    ("home", "Start", "home", "The loop", "From neurons to next steps", "It started at Pragnya, where one child was dancing while another covered their ears in the same room. Is that the brain’s state? Five short screens follow that question from real life, into the lab, and back out again.",
     '<div class="loop-figure"><div data-art="loopTall"></div></div>', '<b>What we found, in three sentences:</b> In mice, brain cells reacted differently to the very same picture depending on how alert the mouse was. A brain-wave headset on a person could not reliably tell even whether their eyes were open or closed. So a helpful app should not try to read your brain: it should ask how you feel and show one small step at a time.', "index.html"),
    ("ch1", "Real life", "users", "Chapter 1 of 5 · Real life", "Same words, different moment.", "A step that is easy when someone is calm can be lost when they are tired, rushed or overloaded. Is that the brain itself? To find out, look inside a brain while its state changes.",
     '<div class="hj-art" data-art="note"></div>', "", "index.html#story"),
    ("ch2", "Understand", "eye", "Chapter 2 of 5 · Understand", "How alert a mouse is changes how its brain responds to what it sees.", "Mice watched pictures while thousands of brain cells were recorded. Guesser A saw only the picture. Guesser B also knew how alert and active the mouse was.",
     '<div class="hj-art" data-art="mouseStudy"></div>', '<b>Found:</b> knowing the mouse’s state made guesses 25–33% better, in all three mice.<div class="tour-nums"><p><b>25–33%</b><span>better guesses once state is known</span></p><p><b>3 of 3</b><span>mice show the gain</span></p></div>', "mouse.html"),
    ("ch3", "Measure", "activity", "Chapter 3 of 5 · Measure", "Can a brain-wave headset tell when a person’s eyes are closed?", "A cap of 14 sensors on one person’s head for two minutes (EEG). Can a simple model tell when their eyes are closed?",
     '<div class="hj-art" data-art="eegStudy"></div>', '<b>Found:</b> it worked on one stretch, then fell to no better than a coin flip. A smarter method using brain-wave rhythms helped, but was still not reliable.<div class="tour-nums"><p><b>0.625</b><span>on one stretch (0.5 is a coin flip)</span></p><p><b>0.478</b><span>across the recording: guessing</span></p><p><b>0.566</b><span>with brain-wave rhythms: better, still unreliable</span></p><p><b>2 of 5</b><span>stretches still below a coin flip</span></p></div>', "eeg.html"),
    ("ch4", "Design", "heart-handshake", "Chapter 4 of 5 · Design", "From findings to features.", "Alertness matters, but a headset cannot reliably measure it. So the apps ask, not guess. They show less on a low-energy day, and make pausing and coming back easy.",
     '<img src="{img}next-step-energy.jpg" alt="Next Step asks how much energy you have today: a little, some or plenty." style="width:100%;border:1px solid var(--line);border-radius:var(--radius-card)">', '<b>Built into:</b> Next Step, by Amishi Mehta, for schoolwork, and Helper Jobs, a family project that gives neurodivergent adults one picture step at a time while they help at Pragnya’s Sunday outings for kids.', "tools.html"),
    ("ch5", "Future", "flask", "Chapter 5 of 5 · Test, then go further", "Where this goes next.", "One follow-up experiment is done. Next: three more experiments on the same public data, testing the apps with Pragnya volunteers and families, and write-ups others can check. Everything here is a plan, and labelled that way.",
     '<div class="hj-art" data-art="plan"></div>', '<b>The aim:</b> a research path that uses brain science to design apps that work for real people.', "next.html"),
]
TOUR_JS = """<script>
(function(){
  var ids = %s, screens = document.querySelectorAll('[data-screen]'), tabs = document.querySelectorAll('[data-go]');
  function show(id){ if (ids.indexOf(id) < 0) id = 'home';
    screens.forEach(function(s){ s.hidden = s.dataset.screen !== id; });
    document.querySelectorAll('.experience-nav [data-go]').forEach(function(b){ if (b.dataset.go === id) b.setAttribute('aria-current', 'page'); else b.removeAttribute('aria-current'); });
    if (location.hash.slice(1) !== id) history.replaceState(null, '', '#' + id); window.scrollTo(0, 0); }
  tabs.forEach(function(b){ b.addEventListener('click', function(){ show(b.dataset.go); }); });
  window.addEventListener('hashchange', function(){ show(location.hash.slice(1)); });
  show(location.hash.slice(1));
})();
</script>""" % str([t[0] for t in TOUR]).replace("'", '"')


def tour(out, base, img):
    screens = []
    for i, (sid, tab, icon, eyebrow, title, sub, art, found, full) in enumerate(TOUR):
        nxt = TOUR[i + 1] if i + 1 < len(TOUR) else TOUR[0]
        go = f'<button class="button primary" type="button" data-go="{nxt[0]}">{"Start" if sid == "home" else ("Back to the start" if nxt[0] == "home" else "Next: " + nxt[1])} <span aria-hidden="true">→</span></button>'
        screens.append(f"""    <section class="screen active landing tour" data-screen="{sid}" aria-labelledby="t-{sid}"{' hidden' if i else ''}>
      <div class="hj-heading"><p class="eyebrow">{eyebrow}</p><h1 id="t-{sid}">{title}</h1><p class="hj-sub">{sub}</p></div>
      {art.replace('{img}', img)}
      {f'<section class="landing-problems answer"><p class="lp-energy">{found}</p></section>' if found and 'tour-nums' not in found else ''}
      {f'<section class="landing-problems answer"><p class="lp-energy">{found.split("<div")[0]}</p></section><div' + found.split("<div", 1)[1] if 'tour-nums' in found else ''}
      <div class="landing-actions">{go}<a class="button secondary" href="{SITE}{full}">{"Open the full site" if sid == "home" else "Read the full chapter"}</a></div>{'<p class="landing-try-note"><a href="download.html">Get it as an Android app</a> · or add this page to your home screen</p>' if sid == "home" else ''}
    </section>""")
    nav = '<nav class="experience-nav tour-nav" aria-label="Chapters">' + ''.join(f'<button type="button" data-go="{t[0]}"><span data-icon="{t[2]}" aria-hidden="true"></span>{t[1]}</button>' for t in TOUR if t[0] != 'ch1') + '</nav>'
    page(out, "Phone tour · From neurons to next steps", "The five chapters of From neurons to next steps, one phone screen at a time.",
         "\n".join(screens) + "\n    " + nav, base=base, extra_js=TOUR_JS,
         manifest='<link rel="manifest" href="manifest.webmanifest" />\n  ')


tour("neuroscience-mobile/index.html", "../", "../img/")


def download(out, base, apk):
    page(out, "Android app · From neurons to next steps", "The phone tour as an Android app, built from the same pages as the website.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'Back to the phone tour'), 'The phone tour · Android', '<span id="page-title">The same five chapters, as an Android app.</span>', 'The app is built straight from the phone tour on this website, so the words, numbers and pictures are the same. It is a test build for reviewers, not a store release.', 'phone')}
      <div class="landing-actions"><a class="button primary" href="{apk}" download>Download the Android app <span aria-hidden="true">→</span></a><a class="button secondary" href="index.html">Use it in the browser instead</a></div>
      <section class="landing-more" aria-labelledby="dl-title">
        <h2 class="landing-subhead" id="dl-title">Before you install</h2>
        {grid([
            ('route-2', 'Step 1', 'Download the file', 'Tap the button above on an Android phone. The file ends in .apk.'),
            ('shield-check', 'Step 2', 'Allow this one install', 'Android asks before installing apps from outside the store. Say yes for this file only.'),
            ('code', 'Check it', 'Same file as the code', f'Every new tour is built by GitHub from the repository. Its fingerprint (SHA-256) is in <a href="{REPO_BLOB}communication/projects/neuroscience-mobile/releases/SHA256.txt">SHA256.txt</a>.'),
        ])}
      </section>
      <div class="landing-facts"><div class="landing-fact landing-fact-not"><h2>What it is not</h2><p>It does not collect anything, does not need an account and does not diagnose anyone. It explains the research, one screen at a time.</p></div><div class="landing-fact"><h2>iPhone and iPad</h2><p>Open the <a href="index.html">phone tour</a> in Safari and choose Share, then Add to Home Screen. It works the same way.</p></div></div>
    </section>""", base=base)


download("neuroscience-mobile/download.html", "../", "../neuroscience-lab-debug.apk")
download("../communication/projects/neuroscience-mobile/download.html", "../../../website/", "releases/neuroscience-lab-debug.apk")
tour("../communication/projects/neuroscience-mobile/index.html", "../../../website/", "../../../website/img/")

# ---------------- the video ----------------
page("video/index.html", "Video · From neurons to next steps", "The five chapters of From neurons to next steps as a short narrated video, with captions.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('../index.html', 'All chapters'), 'The video', '<span id="page-title">The same story, in a few minutes.</span>', 'The slides with their speaker notes read aloud, and captions you can turn on. The words, numbers and drawings are the same as on the website.', 'loop')}
      <video controls preload="metadata" playsinline poster="../presentation/slides/01-cover.jpg" style="width:100%;height:auto;border:1px solid var(--line);border-radius:var(--radius-card);background:#000">
        <source src="from-neurons-to-next-steps.mp4" type="video/mp4">
        <track kind="captions" src="from-neurons-to-next-steps.vtt" srclang="en" label="English" default>
      </video>
      <div class="landing-actions" style="margin-top:18px"><a class="button secondary" href="from-neurons-to-next-steps.mp4" download>Download the video</a><a class="button secondary" href="from-neurons-to-next-steps.vtt" download>Download the captions</a><a class="button secondary" href="../presentation/">See the slides</a></div>
      <div class="landing-facts"><div class="landing-fact landing-fact-not"><h2>About the voice</h2><p>The narration is a computer voice reading the speaker notes, so anyone can rebuild the video from the repository. Amishi can replace any part with her own voice.</p></div><div class="landing-fact"><h2>Share it</h2><p>Send this page’s link, or download the video and captions to attach or upload anywhere. <a href="../share/">Everything to share</a>.</p></div></div>
    </section>""", base="../", og_extra=f'<meta property="og:video" content="{SITE}video/from-neurons-to-next-steps.mp4" />\n  <meta property="og:video:type" content="video/mp4" />\n  <meta property="og:video:width" content="1920" />\n  <meta property="og:video:height" content="1080" />')

# ---------------- share and demo: the handoff page ----------------
def qr(name, label, href):
    return f'<li><a href="{href}"><img src="../img/qr-{name}.svg" alt="QR code for {label}" width="180" height="180" style="width:100%;max-width:180px;background:#fff;border:1px solid var(--line);border-radius:var(--radius-card);padding:8px"></a><strong>{label}</strong><span>Point a phone camera at it.</span></li>'


def size(rel):
    f = W / rel
    return f"{f.stat().st_size / 1_048_576:.1f} MB" if f.exists() else ""


DEMO = [
    ("0:00 · Website", "Open with the loop.", "Open the website. Read the first paragraph out loud, then point at the loop drawing: real life, understand, measure, design, test.", "<b>Say:</b> “At Pragnya, one child danced while another covered their ears in the same room. Is that the brain’s state?”"),
    ("0:45 · Chapter 2", "Show the mouse result.", "Open the mouse study and scroll to the first chart: guesser A against guesser B, in all three mice.", "<b>Say:</b> “Knowing the mouse’s state made our guesses 25–33% better, and the gain disappears if the state comes from the wrong moment.”"),
    ("1:45 · Chapter 3", "Show the drift.", "Open the EEG study and scroll to the five-stretches chart, then to experiment 2.", "<b>Say:</b> “Good on one stretch, a coin flip over time. Even brain-wave rhythms didn’t fix it, so a tool shouldn’t guess.”"),
    ("2:45 · Chapter 4", "Show the apps.", "Open the design chapter, then hold up a phone with Next Step open on the energy question.", "<b>Say:</b> “So the app asks how much energy you have, and on a low day shows just the next step.”"),
    ("3:45 · Chapter 5", "Close on what’s next.", "Open the last chapter and point at the road ahead.", "<b>Say:</b> “Next: the remaining experiments with a mentor, a first paper, and testing the apps with the people they are for.”"),
]
page("share/index.html", "Share and demo · From neurons to next steps", "Everything to share or demo From neurons to next steps: one link, a five-minute demo, QR codes, the slides, the video and every download.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('../index.html', 'All chapters'), 'Share and demo', '<span id="page-title">Everything in one place.</span>', 'One link to send, a five-minute demo you can run from a laptop, codes for phones in the room, and every file to download.', 'phone')}
      <section class="landing-problems answer"><p class="lp-energy"><b>To share it, send one link:</b> <a href="{SITE}">{SITE.removeprefix("https://")}</a> <span>Everything else, including the slides, video, phone tour and both apps, is linked from there.</span></p></section>

      <section class="landing-problems" id="demo" aria-labelledby="demo-title">
        <h2 class="landing-subhead" id="demo-title">A five-minute demo</h2>
        <p class="lp-lead">One step per chapter. Or skip the talking and play the short video.</p>
        <ol aria-label="Demo steps" tabindex="0">
          {''.join(f'<li><p class="lp-k">{k}</p><h3>{h}</h3><p class="lp-pain">{a}</p><p class="lp-fix">{b}</p></li>' for k, h, a, b in DEMO)}
        </ol>
      </section>

      <section class="landing-more" aria-labelledby="present-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="present-title">Present it</h2><p class="lp-lead">The same story in every format. Pick the one that fits the room.</p></div></div>
        {grid([
            ('presentation', 'Slides, full screen', f'{N_SLIDES} slides', f'<a href="../presentation/present.html">Present</a> with arrow keys, or open the <a href="../presentation/presenter.html">presenter view</a> on the laptop for notes and a timer.'),
            ('player-play', 'Video', 'About four and a half minutes, with captions', '<a href="../video/">Play it here</a>, or download it below to play offline.'),
            ('device-mobile', 'Phone tour', 'Five chapters, one screen each', '<a href="../neuroscience-mobile/">Open it</a>, or let people scan the code below.'),
        ])}
      </section>

      <h2 class="landing-subhead">Codes for phones in the room</h2><p class="landing-demo-note">Put this page on the screen; people scan with their phone camera.</p>
      <ol class="landing-demo qr-row" aria-label="QR codes" tabindex="0">
        {qr('phone-tour', 'Phone tour', '../neuroscience-mobile/')}{qr('website', 'Website', '../')}{qr('video', 'Video', '../video/')}{qr('slides', 'Slides', '../presentation/')}
      </ol>

      <section class="landing-more" aria-labelledby="dl-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="dl-title">Download and send</h2><p class="lp-lead">Files you can attach to an email, upload, or open with no internet.</p></div></div>
        {grid([
            ('presentation', 'Slides', 'PowerPoint, with speaker notes', f'<a href="../presentation/from-neurons-to-next-steps-slides.pptx" download>Download</a> ({size("presentation/from-neurons-to-next-steps-slides.pptx")}). Opens in PowerPoint, Keynote and Google Slides.'),
            ('file-text', 'Slides', 'PDF', f'<a href="../presentation/from-neurons-to-next-steps-slides.pdf" download>Download</a> ({size("presentation/from-neurons-to-next-steps-slides.pdf")}). For printing or sending.'),
            ('player-play', 'Video', 'MP4, full HD', f'<a href="../video/from-neurons-to-next-steps.mp4" download>Download</a> ({size("video/from-neurons-to-next-steps.mp4")}). Captions: <a href="../video/from-neurons-to-next-steps.vtt" download>VTT file</a>.'),
            ('books', 'Packet', 'PDF of all five chapters', f'<a href="../ASDRP-neuroscience-portfolio-packet.pdf" download>Download</a> ({size("ASDRP-neuroscience-portfolio-packet.pdf")}). The website as pages.'),
            ('device-mobile', 'Android app', 'The phone tour, installed', '<a href="../neuroscience-mobile/download.html">How to install</a>. On iPhone, add the phone tour to the home screen instead.'),
            ('code', 'Source code', 'Everything, rerunnable', f'<a href="{REPO}">The portfolio</a> and <a href="{FLAGSHIP}">Amishi’s mouse study</a>.'),
        ])}
      </section>

      <section class="landing-more" aria-labelledby="apps2-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="apps2-title">The two apps</h2><p class="lp-lead">Live, with made-up examples. Each links back here.</p></div></div>
        {grid([
            ('heart-handshake', 'By Amishi Mehta', 'Next Step', f'<a href="{NEXT_STEP}">Open Next Step</a>. It can take about 30 seconds to wake up the first time. <a href="https://github.com/AmishI123/next-step">Source code</a>.'),
            ('users', 'Family project', 'Helper Jobs', f'<a href="{HELPER_JOBS}">Open Helper Jobs</a>. Built for real jobs at Pragnya’s Sunday outings. <a href="https://github.com/AmishI123/neurocomms-app">Source code</a>.'),
        ])}
      </section>

      <div class="landing-facts">
        <div class="landing-fact"><h2>Checked before every publish</h2><p>Every page, chart, drawing, download, the phone tour and the slide viewer are tested automatically before the site goes live, and every number is checked against the saved results. <a href="{REPO_BLOB}application/e2e_site.py">The test</a> · <a href="{REPO_BLOB}application/audit_portfolio.py">the number check</a>.</p></div>
      </div>
    </section>""", base="../")

# ---------------- for Amishi: the handoff pages ----------------
APP = W.parent / "application"
HANDOFF_JS = '<script src="../assets/handoff.js"></script>'


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def essay_body(md):
    """The essay text after the '---' line, with markdown bold removed."""
    body = md.split("\n---\n", 1)[1].strip()
    out = []
    for para in body.split("\n\n"):
        lines = [line.strip() for line in para.splitlines()]
        title = lines[0].replace("**", "") + "\n" if lines[0].startswith("**") and lines[0].endswith("**") else ""
        rest = lines[1:] if title else lines
        out.append(title + " ".join(rest).replace("**", ""))
    return "\n\n".join(out)


def toolbar(filename):
    return (f'<div class="landing-actions handoff-bar"><button class="button primary" type="button" data-download="{filename}">Download as a text file</button>'
            f'<button class="button secondary" type="button" data-copy>Copy everything</button><p class="landing-try-note" data-status aria-live="polite">Your writing stays in this browser until you download or copy it.</p></div>')


LEDGER = [
    ("target", "The mouse question", "You chose to compare guessing from the picture alone with the picture plus the mouse’s state.", "Your father helped shape the question.", "Confirm in your words"),
    ("eye", "Exploring the mouse data", "You learned Python, loaded the recordings and looked at brain cells, pupil size and running.", "Your father helped set up and fix problems.", "Confirm"),
    ("chart-dots", "Building the two guessers", "You built guesser A and guesser B and tested both on unseen pictures.", "Your father checked the code and gave advice.", "Confirm"),
    ("brain", "Pupil or running, and which cells gain", "You compared pupil with running, and found the cells that follow alertness gain most.", "Your father reviewed choices and writing.", "Confirm"),
    ("users", "Two more mice and the checks", "The other two mice, mixing up the state, and leaving one mouse out.", "Run in your repository with your father’s help.", "Say which parts you ran"),
    ("activity", "The EEG study", "The learn-from-earlier, test-on-later study and its write-up.", "Your father and AI tools helped set up and review it.", "Say which parts you did"),
    ("arrows-shuffle", "The EEG checks", "Five stretches, mixing up the answers, leaving a gap, trimming glitchy readings.", "Added with AI tools and your father.", "Say which parts you ran"),
    ("flask", "Experiment 2: brain-wave rhythms", "Planned, coded and run with AI help on 10 November 2026.", "AI tools wrote and ran it from a plan written first.", "Rerun it yourself first"),
    ("presentation", "Website, slides, phone tour and video", "The pages that tell the story.", "Built with AI tools and your father.", "Say what you designed, checked or will present"),
    ("heart-handshake", "Next Step", "Credited to you, Amishi Mehta.", "Built with AI tools and your father.", "Describe your part"),
    ("users", "Helper Jobs", "A family project for Pragnya’s Sunday outings.", "Built with AI tools and your father.", "Describe your part"),
]
(APP / "contribution-ledger.md").write_text(
    "# Who did what\n\nWritten to Amishi. The designed page is at https://amishi123.github.io/neuroscience-project/handoff/who-did-what.html. "
    "This file is written from the same list in `website/build_pages.py`.\n\n| Part | What it covers | Help | To do |\n|---|---|---|---|\n"
    + "".join(f"| {t} | {w} | {h} | {st} |\n" for _, t, w, h, st in LEDGER)
    + "\n## Rules\n\n- Only claim what Amishi did and can explain out loud.\n- Keep her father’s and the AI tools’ help visible.\n- Where a step was done for her, say so.\n")

QUESTIONS = [
    ("moment", "Your chapter 1 moment (the most important one)", "One real time from your own life, at school or anywhere, when the same instruction worked once and was lost a little later. What happened, and what did you notice? A few sentences. You decide how much to share; no names.", 6, "It opens the website, the slides, the video and Essay 1."),
    ("spark", "What first made the brain interesting to you?", "A class, a book, a conversation or something you saw.", 3, "Used in Essay 1 if it is different from your moment."),
    ("changed-mind", "A time the data changed your mind", "For example, expecting running to matter and finding it was the pupil.", 3, "Used in Essay 5."),
    ("next-step", "Next Step: your part", "What you designed, built, tested or decided.", 4, "Used in chapter 4 and Essay 5."),
    ("helper-jobs", "Helper Jobs: your part", "What you did for the Pragnya outings app, if anything.", 3, "Used in chapter 4."),
    ("real-need", "One real need that changed a design", "Something a person needed that made you build something differently.", 3, "Used in chapter 4."),
    ("voice", "The video: your voice?", "Do you want to record it yourself? How should you be credited?", 2, "See the recording script."),
]


def field(key, label, hint, rows, use):
    return (f'<div class="handoff-field"><label class="field" for="q-{key}">{label}</label><p class="hint">{hint}</p>'
            f'<textarea id="q-{key}" rows="{rows}" data-save="answer-{key}" data-label="{label}"></textarea><p class="hint used">{use}</p></div>')


STEPS = [
    ("1 · About 15 minutes", "Your real moment, and your parts.", "One real time from your own life when the same instruction worked once and was lost later, plus what you did in each app.", '<b>Opens:</b> the website, slides, video and Essay 1. <a href="answers.html">Write your answers →</a>'),
    ("2 · About 30 minutes each", "Make both essays yours.", "Drafts that follow the same five chapters. Fill the parts in [brackets] and change anything that does not sound like you.", '<b>Limit:</b> 375 words each. <a href="essay-1.html">Essay 1 →</a> <a href="essay-5.html">Essay 5 →</a>'),
    ("3 · About 10 minutes", "Check who did what.", "Eleven parts of the work. Confirm each one, or say what to change.", '<b>Rule:</b> only claim what you did and can explain. <a href="who-did-what.html">Check the list →</a>'),
    ("4 · Optional · About 20 minutes", "Your voice on the video.", f"Read {N_SLIDES} short parts, one per slide, on a phone. Any you skip keep the computer voice.", '<b>Then:</b> send the recordings. <a href="recording.html">Recording script →</a>'),
]
steps_html = "".join(f'<li><p class="lp-k">{k}</p><h3>{h}</h3><p class="lp-pain">{a}</p><p class="lp-fix">{b}</p></li>' for k, h, a, b in STEPS)

page("handoff/index.html", "For Amishi · From neurons to next steps", "What Amishi still adds to her portfolio: one real moment, her own essays, who did what, and her voice on the video.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('../index.html', 'All chapters'), 'For Amishi', '<span id="page-title">Four things only you can add.</span>', 'Everything else is built, checked and live. These four make it yours. Each page saves your writing in this browser while you work; download it when you are done and send it back.', 'family')}
      <section class="landing-problems" id="todo" aria-labelledby="todo-title">
        <h2 class="landing-subhead" id="todo-title">Your four steps</h2>
        <p class="lp-lead">Start with the first one. It changes the most.</p>
        <ol aria-label="Four steps" tabindex="0">{steps_html}</ol>
      </section>
      <section class="landing-more" aria-labelledby="see-title">
        <div class="lm-head"><div><h2 class="landing-subhead" id="see-title">See what is already done</h2><p class="lp-lead">The same story in every format, all linked together.</p></div><div class="hj-art" data-art="loop"></div></div>
        {grid([
            ('route-2', 'The website', 'Five chapters', '<a href="../">Read the story</a>, from real life into the lab and back.'),
            ('presentation', 'The slides', f'{N_SLIDES} slides, with notes', '<a href="../presentation/">See them</a>, or present them full screen.'),
            ('player-play', 'The video', 'About four and a half minutes', '<a href="../video/">Watch it</a>. Step 4 puts your voice on it.'),
            ('device-mobile', 'The phone tour', 'One chapter per screen', '<a href="../neuroscience-mobile/">Open it</a> on your phone.'),
            ('heart-handshake', 'Share and demo', 'Everything in one place', '<a href="../share/">Links, a five-minute demo, codes and downloads</a>.'),
            ('code', 'Your mouse study', 'Your code', f'<a href="{FLAGSHIP}">AmishI123/neuroscience-project</a>, checked against the website.'),
        ])}
      </section>
    </section>""", base="../")

page("handoff/answers.html", "Your answers · From neurons to next steps", "Amishi’s real moment for chapter 1, and her part in each app, written in her own words.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'For Amishi'), 'Step 1 of 4 · Your answers', '<span id="page-title">In your own words.</span>', 'Short and true beats long and polished. Write the way you would tell a friend. Nothing here is sent anywhere until you download it.', 'note')}
      <section class="landing-problems answer"><p class="lp-energy"><b>Why the first one matters:</b> the whole story starts with it. Chapter 1 says the work started from your own experience; one real moment shows it. <span>You decide how much to share. What happened and what you noticed is enough.</span></p></section>
      <div class="handoff-form">{''.join(field(*q) for q in QUESTIONS)}</div>
      {toolbar("amishi-answers.txt")}
      <p class="landing-note"><a href="index.html">← For Amishi</a><a href="essay-1.html">Step 2: Essay 1 →</a></p>
    </section>""", base="../", extra_js=HANDOFF_JS)


CHAPTER_TAGS = {
    "1": ("users", "Chapter 1 · Real life"), "2": ("eye", "Chapter 2 · Understand"), "3": ("activity", "Chapter 3 · Measure"),
    "4": ("heart-handshake", "Chapter 4 · Design"), "5": ("flask", "Chapter 5 · What’s next"),
}


def essay_read(body, chapters):
    """The draft typeset for reading: one row per paragraph with its chapter tag, [brackets] shown as boxes to fill."""
    import json as _json, re as _re
    rows = []
    for i, para in enumerate(body.split("\n\n")):
        ic, tag = CHAPTER_TAGS.get(chapters[i], ("", "")) if i < len(chapters) else ("", "")
        title, _, text = para.partition("\n") if "\n" in para else ("", "", para)
        text = _re.sub(r"\[([^\]]+)\]", lambda m: f'<mark class="slot"><b>Your part</b> {esc(m.group(1))}</mark>', esc(text))
        aside = f'<p class="essay-tag"><span data-icon="{ic}" aria-hidden="true"></span>{tag}</p>' if tag else '<p class="essay-tag"></p>'
        rows.append(f'<div class="essay-row">{aside}<div>{f"<h3>{esc(title)}</h3>" if title else ""}<p>{text}</p></div></div>')
    return f'<article class="essay-read" data-read data-chapters=\'{_json.dumps(chapters)}\' data-tags=\'{_json.dumps(CHAPTER_TAGS)}\'>{"".join(rows)}</article>'


def essay_page(num, title, prompt, src, art, prev, nxt, chapters):
    body = essay_body((APP / "essays" / src).read_text())
    page(f"handoff/essay-{num}.html", f"Essay {num} · From neurons to next steps", f"Essay {num} draft ({prompt}), following the five chapters, for Amishi to make her own.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'For Amishi'), f'Step 2 of 4 · Essay {num}', f'<span id="page-title">Make Essay {num} yours.</span>', f'The prompt: {prompt}. This draft follows the same five chapters as the website, so a reviewer who reads the essay and opens the site hears one story.', art)}
      <section class="essay-sheet" aria-labelledby="draft-{num}">
        <div class="essay-head"><p class="eyebrow">Essay {num} · draft</p><h2 id="draft-{num}">{title}</h2><p class="essay-meta"><span data-words-for="essay-{num}" data-limit="375"></span></p></div>
        {essay_read(body, chapters)}
        <p class="essay-key"><mark class="slot"><b>Your part</b> boxes like this</mark> ask for something only you know. The tag beside each paragraph shows which chapter of the website it matches.</p>
      </section>
      <section class="landing-more" aria-labelledby="how-{num}">
        <h2 class="landing-subhead" id="how-{num}">Make it yours, in three passes</h2>
        {grid([
            ('star', 'First', 'Fill the boxes', 'Each one asks for something only you know. Your answers from step 1 go here.'),
            ('message-2', 'Then', 'Make it sound like you', 'Change any word you would not say. Shorter is fine.'),
            ('shield-check', 'Last', 'Keep it true', 'Delete anything you cannot explain out loud, and keep your father’s help visible.'),
        ])}
      </section>
      <div class="essay-box"><label class="field" for="essay-{num}">Edit the draft here. The page above updates as you type.</label>
        <textarea id="essay-{num}" rows="24" data-save="essay-{num}" data-label="Essay {num}: {prompt}">{esc(body)}</textarea>
        <p class="hint" data-words-for="essay-{num}" data-limit="375"></p></div>
      {toolbar(f"essay-{num}.txt")}
      <p class="landing-try-note"><button class="link-button" type="button" data-reset>Start again from the original draft</button> · <button class="link-button" type="button" onclick="window.print()">Print the draft</button></p>
      <p class="landing-note"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a></p>
    </section>""", base="../", extra_js=HANDOFF_JS)


essay_page(1, "Why are you applying?", "why are you applying? Up to 375 words", "essay-1-why-applying.md", "plan", ("answers.html", "Step 1: your answers"), ("essay-5.html", "Essay 5"), ["1", "", "2", "3", "4", "5"])
essay_page(5, "Your hands-on research.", "your hands-on research, up to three examples. Up to 375 words", "essay-5-research-experience.md", "controls", ("essay-1.html", "Essay 1"), ("who-did-what.html", "Step 3: who did what"), ["2", "3", "4"])


def ledger_card(i, ic, t, w, h, st):
    return (f'<li><div class="lm-top"><span class="lm-icon" data-icon="{ic}"></span><p class="lm-k">{st}</p></div><h3>{t}</h3><p>{w}</p>'
            f'<p class="help-from"><b>Help:</b> {h}</p><label class="field" for="l-{i}">Your note</label>'
            f'<textarea id="l-{i}" rows="2" data-save="ledger-{i}" data-label="{t}" placeholder="Confirmed, or what to change"></textarea></li>')


ledger_html = "".join(ledger_card(i, *row) for i, row in enumerate(LEDGER))
page("handoff/who-did-what.html", "Who did what · From neurons to next steps", "Each part of the portfolio, what Amishi did, and the help she had, for her to confirm.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'For Amishi'), 'Step 3 of 4 · Who did what', '<span id="page-title">Only claim what you did.</span>', 'Reviewers trust a portfolio that is honest about help. For each part, write “confirmed” or what to change. The tag on each card says what is needed.', 'coordinator')}
      <section class="landing-problems answer"><p class="lp-energy"><b>The rule:</b> if you cannot explain it out loud, do not claim it. <span>Help from your father and from AI tools stays visible on the website and in the essays.</span></p></section>
      <ul class="lm-grid ledger">{ledger_html}</ul>
      {toolbar("who-did-what.txt")}
      <p class="landing-note"><a href="essay-5.html">← Essay 5</a><a href="recording.html">Step 4: your voice →</a></p>
    </section>""", base="../", extra_js=HANDOFF_JS)


def rec_card(i, part, slides):
    head_line, _, text = part.partition("\n")
    num, name = head_line.split(" · ", 1)
    img = f"../presentation/slides/{slides[i].name}" if i < len(slides) else ""
    return (f'<li><img src="{img}" alt="Slide {int(num)}: {esc(name)}" loading="lazy" width="1920" height="1080">'
            f'<strong>{num} · {esc(name)}</strong><span>{esc(text.strip())}</span><em class="file-name">Save as {num}.m4a</em></li>')


REC = (APP / "recording-script.md").read_text().split("\n## ")[1:]
SLIDE_FILES = sorted((W / "presentation/slides").glob("*.jpg"))
rec_html = "".join(rec_card(i, part, SLIDE_FILES) for i, part in enumerate(REC))
page("handoff/recording.html", "Your voice · From neurons to next steps", "The recording script for the video, one short part per slide, for Amishi to read in her own voice.", f"""    <section class="screen active landing" aria-labelledby="page-title">
{heading(('index.html', 'For Amishi'), 'Step 4 of 4 · Optional · Your voice', '<span id="page-title">Read it the way you would say it.</span>', f'{N_SLIDES} short parts, one per slide, about four and a half minutes in all. Record on a phone. Any part you skip keeps the computer voice, so you can do a few at a time.', 'breakTime')}
      <section class="landing-more" aria-labelledby="tips-title">
        <h2 class="landing-subhead" id="tips-title">Before you start</h2>
        {grid([
            ('home', 'Where', 'A quiet room', 'Soft things around you, like a bedroom, sound better than a kitchen.'),
            ('device-mobile', 'How', 'Your phone’s voice memo app', 'Hold it about a hand’s width away. One recording per part.'),
            ('message-2', 'What to say', 'Change words that are not yours', 'Keep the meaning and the numbers the same.'),
            ('certificate', 'When done', 'Name and send the files', f'Name each one by its number, 01.m4a to {N_SLIDES:02d}.m4a, and send them to your dad.'),
        ])}
      </section>
      <h2 class="landing-subhead">The {N_SLIDES} parts</h2><p class="landing-demo-note">Each part is read while its slide is on screen.</p>
      <ol class="landing-demo rec-list" aria-label="Recording script">{rec_html}</ol>
      <p class="landing-note"><a href="who-did-what.html">← Step 3</a><a href="index.html">Back to your four steps →</a></p>
    </section>""", base="../")

# ---------------- old addresses keep working ----------------
REDIRECTS = {
    "mouse-visual-cortex.html": "mouse.html", "mouse-leave-one-out.html": "mouse.html#checks",
    "eeg-eye-state.html": "eeg.html", "eeg-label-shuffle-control.html": "eeg.html#checks", "eeg-purge-gap.html": "eeg.html#checks",
    "reviewer-dashboard.html": "index.html", "reviewer-packet.html": "index.html",
    "mouse-visual-cortex-slides.html": "presentation/", "eeg-eye-state-slides.html": "presentation/", "release-verification.html": "share/",
}
for old, new in REDIRECTS.items():
    (W / old).write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved</title><meta http-equiv="refresh" content="0; url={new}"><link rel="canonical" href="{new}"></head><body><p>This page moved: <a href="{new}">{new}</a>.</p></body></html>\n')
print("built index, mouse, eeg, tools, next ·", len(REDIRECTS), "redirects")
