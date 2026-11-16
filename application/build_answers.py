"""Builds the ASDRP answers PDF and a plain-text copy from final_drafts.md and activities_final.md.

Run: python3 application/build_answers.py
Writes application/submission/ASDRP_application_answers.pdf and .txt
"""
import datetime
import html
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "submission"

PROMPTS = {
    "1": "Why are you applying for the Aspiring Scholars Directed Research Program? Why do you want to commit a large chunk of your time to doing scientific research? What questions or fields in science and engineering interest you, and why? What do you hope to do in STEM, at the Aspiring Scholars Directed Research Program and beyond?",
    "2": "Please discuss any previous science/math/computer science coursework (either at school or in another setting, such as summer programs or online classes). Please include your grades in these courses, if applicable. Please provide explanations for any grades that you think are not representative of your true potential.",
    "3": "If you have any other experience in STEM (such as clubs or volunteering) that you wish to discuss, please do so here.",
    "4": "How would you contribute diversity to STEM (science, technology, engineering, mathematics)? (Diversity is broadly defined)",
    "5": "Do you have any hands-on science experience or laboratory research experience? If so, please provide a detailed discussion of what you did, with whom you worked, what your specific tasks were, what you accomplished, etc. Limit to 3 examples.",
    "uploads": "If you have any files (e.g. scientific papers, posters) from previous research experience, please attach it here. You can upload up to 3 files.",
    "activities": "Please list out ALL school coursework and extracurricular activities that you may possibly engage in during the academic year. Include an average weekly time estimate for each. If you are not sure if you will have that commitment, please say so.",
    "fields": "First, second and third choice preferred research field (optional).",
    "advisor": "If you have a strong preference for a particular research advisor, field, or project, please indicate so. (optional)",
}
TITLES = {"1": "Why are you applying to ASDRP?", "2": "Science, math and computer science coursework",
          "3": "Other STEM experience", "4": "Contributing diversity to STEM",
          "5": "Hands-on science or research experience"}


def sections():
    text = (HERE / "final_drafts.md").read_text()
    out = {}
    for m in re.finditer(r"(?ms)^## (\S+) .*?\(limit (\d+)\), \d+ words\n(.*?)(?=^## |\Z)", text):
        key = m.group(1) if m.group(1)[0].isdigit() else "advisor"
        body = m.group(3).strip()
        paras = [re.sub(r"\s+", " ", p.replace("**", "")).strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
        out[key] = (int(m.group(2)), paras)
    return out


def activities():
    text = (HERE / "activities_final.md").read_text().split("---", 1)[1]
    items = []
    for blk in re.split(r"\n\s*\n", text.strip()):
        lines = blk.strip().split("\n")
        items.append((lines[0].strip("* "), " ".join(lines[1:]).strip()))
    return items


def words(paras):
    return sum(len(p.split()) for p in paras)


def esc(s):
    return html.escape(s)


def build():
    S, A = sections(), activities()
    act_words = sum(len(t.split()) + len(b.split()) for t, b in A)

    # Plain text: one paragraph per line, one blank line only between questions.
    txt = ["ASDRP APPLICATION ANSWERS (Amishi Mehta)", "Each paragraph is one line, ready to paste.", ""]
    for k in "12345":
        lim, paras = S[k]
        txt += [f"===== QUESTION {k}: {TITLES[k]} ({words(paras)} of {lim} words) =====", *paras, ""]
    txt += [f"===== ACTIVITIES (about {act_words} of 1000 words) ====="] + [x for t, b in A for x in (t, b)] + [""]
    txt += ["===== PREFERRED FIELDS =====", "1. Biology", "2. Cognitive Science & Psychology", "3. Chemistry", ""]
    lim, paras = S["advisor"]
    txt += [f"===== ADVISOR PREFERENCE ({words(paras)} of {lim} words) =====", *paras, ""]
    (OUT / "ASDRP_application_answers.txt").write_text("\n".join(txt))

    def answer(label, title, prompt, paras, lim):
        body = "".join(f"<p>{esc(p)}</p>" for p in paras)
        return (f'<section><div class="q">{label}</div><h2>{esc(title)}</h2>'
                f'<div class="prompt">The form asks: {esc(prompt)}</div>'
                f'<div class="wc">{words(paras)} of {lim} words</div><div class="ans">{body}</div></section>')

    parts = []
    for k in "12345":
        lim, paras = S[k]
        parts.append(answer(f"Question {k}", TITLES[k], PROMPTS[k], paras, lim))
    parts.append(f'<section><div class="q">Uploads</div><h2>Papers or posters (up to 3 files)</h2>'
                 f'<div class="prompt">The form asks: {esc(PROMPTS["uploads"])}</div>'
                 '<ol class="plain"><li>Amishi_Mehta_research_report.pdf</li><li>Amishi_Mehta_poster.pdf</li>'
                 '<li>Amishi_Mehta_portfolio_packet.pdf (her website as a PDF)</li></ol></section>')
    act = "".join(f"<p><b>{esc(t)}</b> {esc(b)}</p>" for t, b in A)
    parts.append(f'<section><div class="q">Activities</div><h2>All coursework and extracurricular activities</h2>'
                 f'<div class="prompt">The form asks: {esc(PROMPTS["activities"])}</div>'
                 f'<div class="wc">about {act_words} of 1000 words</div><div class="ans act">{act}</div></section>')
    parts.append('<section><div class="q">Transcript</div><h2>Unofficial transcript</h2>'
                 '<p class="note">Upload a transcript showing her full name, school name, and all courses completed or scheduled.</p></section>')
    parts.append(f'<section><div class="q">Research fields</div><h2>Preferred fields</h2>'
                 f'<div class="prompt">The form asks: {esc(PROMPTS["fields"])}</div>'
                 '<ol class="plain"><li>Biology</li><li>Cognitive Science &amp; Psychology</li><li>Chemistry</li></ol></section>')
    lim, paras = S["advisor"]
    parts.append(answer("Advisor preference", "Preferred advisor, field or project", PROMPTS["advisor"], paras, lim))

    intro = """<section class="intro"><h2>About ASDRP</h2>
<p class="note">The Aspiring Scholars Directed Research Program (ASDRP) is a research program in which high school students
carry out real scientific research projects under the guidance of research advisors. The application asks why the student
wants to do research, what they have studied, what STEM experience they have, how they would contribute to a diverse
research community, and what hands-on research they have done. Students are matched to research fields and advisors based
on the strength of their application.</p>
<p class="note">This document gives each answer in the same order as the form. Above each answer is the question the form
asks. Copy only the answer text into the form. A plain-text copy (ASDRP_application_answers.txt) has each paragraph on a
single line, which pastes most cleanly.</p></section>"""

    check = """<section class="check"><h2>Before submitting</h2><ol>
<li>Read every answer aloud and change anything that does not sound like her.</li>
<li>Advisor answer: check whether it is <b>Dr.</b> or <b>Mrs.</b> Sahar Jahanikia on the ASDRP faculty page.</li>
<li>Be ready to explain everything the website shows, including the EEG study and the apps.</li>
<li>Upload the transcript, the research report, the poster and the portfolio packet.</li></ol></section>"""

    fit = """<section><div class="q">How it fits together</div><h2>One thread across every answer</h2>
<p class="note"><b>The thread:</b> the same input reaches a brain differently depending on its state. She saw it at Pragnya,
measured it in mouse visual cortex, built a small tool around it, and wants to understand it at the cellular level on the
way to a career in anesthesia.</p>
<table><tr><th>Answer</th><th>Its part of the thread</th><th>Where a reviewer can check it</th></tr>
<tr><td>1. Why ASDRP</td><td>Pragnya moment, then the mouse study, then anesthesia</td><td>Portfolio home and mouse pages</td></tr>
<tr><td>2. Coursework</td><td>Biology, Chemistry, Calculus and self-taught Python as the tools</td><td>Transcript; notebooks in the research repo</td></tr>
<tr><td>3. STEM experience</td><td>Pragnya, past tutoring and hospice volunteering; Next Step as "ask, don't guess"</td><td>Portfolio Design page; Next Step app</td></tr>
<tr><td>4. Diversity</td><td>Different children, different ways through the same room</td><td>(Her own experience)</td></tr>
<tr><td>5. Hands-on research</td><td>Three mice, the controls, prediction not cause</td><td>Report, poster, portfolio (link at the end of the essay)</td></tr>
<tr><td>Advisor</td><td>How brain state and medications change neurons</td><td>Portfolio home page (her goal)</td></tr></table>
<p class="note"><b>Links:</b> portfolio amishi123.github.io/neuroscience-project · research code github.com/AmishI123/neuroscience-project ·
Next Step next-step-live.onrender.com · Helper Jobs helper-jobs.onrender.com</p></section>"""

    css = """@page{size:Letter;margin:0.8in 0.85in}
body{font-family:Georgia,"Times New Roman",serif;font-size:11.5pt;line-height:1.5;color:#1d1d1d}
.cover h1{font-size:24pt;margin:0 0 4pt}.cover .sub{color:#555;font-size:12pt;margin-bottom:14pt}
h2{font-family:Helvetica,Arial,sans-serif;font-size:14pt;margin:2pt 0 4pt;color:#1f3a5f}
.q{font-family:Helvetica,Arial,sans-serif;font-size:9pt;letter-spacing:.08em;text-transform:uppercase;color:#9a4a1f}
.q,h2,.prompt,.wc{break-after:avoid;page-break-after:avoid}
.prompt{font-style:italic;color:#555;font-size:10pt;margin-bottom:4pt}
.wc{font-family:Helvetica,Arial,sans-serif;font-size:9pt;color:#666;margin-bottom:6pt}
.ans p{margin:0;text-indent:1.6em}.ans p:first-child{text-indent:0}
.ans.act p{text-indent:0}
p.note{margin:0 0 6pt}
section{margin-bottom:18pt}section+section{border-top:1px solid #ddd;padding-top:12pt}
.check,.intro{background:#f6f2ea;padding:10pt 14pt;border-radius:6px}
ol.plain{margin:0 0 0 18pt;padding:0}
table{border-collapse:collapse;width:100%;font-size:10pt;margin:6pt 0 8pt}
th,td{border-bottom:1px solid #ddd;padding:4pt 6pt;text-align:left;vertical-align:top}
th{font-family:Helvetica,Arial,sans-serif;color:#1f3a5f}"""
    today = datetime.date.today().strftime("%B %d, %Y")
    doc = (f'<!doctype html><html><head><meta charset="utf-8"><title>ASDRP application answers</title><style>{css}</style></head><body>'
           f'<div class="cover"><h1>ASDRP application answers</h1><div class="sub">Amishi Mehta · answers in application order · {today}</div></div>'
           f'{intro}{check}{"".join(parts)}{fit}</body></html>')
    page = OUT / "_answers.html"
    page.write_text(doc)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        p = b.new_page()
        p.goto(page.as_uri())
        p.pdf(path=str(OUT / "ASDRP_application_answers.pdf"), format="Letter", print_background=True,
              display_header_footer=True, header_template="<span></span>",
              footer_template='<div style="font-size:8px;width:100%;text-align:center;color:#888">ASDRP application answers · page <span class="pageNumber"></span> of <span class="totalPages"></span></div>',
              margin={"top": "0.8in", "bottom": "0.8in", "left": "0.85in", "right": "0.85in"})
        b.close()
    page.unlink()


if __name__ == "__main__":
    build()
    print("wrote", OUT / "ASDRP_application_answers.pdf", "and .txt")
