"""Build the reviewer-facing ASDRP portfolio packet as a PDF."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, PageBreak


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "ASDRP-neuroscience-portfolio-packet.pdf"


def build() -> None:
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Eyebrow", parent=styles["Normal"], fontSize=8, leading=11, textColor=colors.HexColor("#567567"), spaceAfter=8))
    styles.add(ParagraphStyle(name="Hero", parent=styles["Title"], fontSize=28, leading=30, textColor=colors.HexColor("#17212b"), spaceAfter=12))
    styles.add(ParagraphStyle(name="Section", parent=styles["Heading1"], fontSize=18, leading=22, textColor=colors.HexColor("#216b4c"), spaceBefore=18, spaceAfter=8))
    styles.add(ParagraphStyle(name="Body2", parent=styles["BodyText"], fontSize=10, leading=15, textColor=colors.HexColor("#34434a"), spaceAfter=8))
    styles.add(ParagraphStyle(name="Small", parent=styles["BodyText"], fontSize=8, leading=11, textColor=colors.HexColor("#637077")))

    doc = SimpleDocTemplate(str(OUT), pagesize=letter, rightMargin=.72 * inch, leftMargin=.72 * inch, topMargin=.65 * inch, bottomMargin=.65 * inch, title="ASDRP Neuroscience Portfolio")
    story = []
    story += [Paragraph("ASDRP / REVIEWER PACKET", styles["Eyebrow"]), Paragraph("Evidence first.<br/><i>Curiosity always.</i>", styles["Hero"]), Paragraph("A connected portfolio of reproducible neuroscience experiments, applied neurotechnology, and communication artifacts.", styles["Body2"]), Spacer(1, 12)]

    status = [[Paragraph("PROJECT", styles["Small"]), Paragraph("VERIFIED STATUS", styles["Small"]), Paragraph("PRIMARY EVIDENCE", styles["Small"])],
              ["Mouse visual cortex", "Three-mouse replication complete; population extension pending", "Sensorium report, replication summary, figures"],
              ["EEG eye state", "Time-aware study plus label-shuffle control complete", "Python analysis, metrics, report, explainer"],
              ["Neurodivergent / Neurocomms", "Applied project references and templates connected", "Mobile, HTML, presentation, PDF, video patterns"]]
    table = Table(status, colWidths=[1.45 * inch, 2.15 * inch, 3.0 * inch])
    table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#edf4ef")), ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#216b4c")), ("GRID", (0, 0), (-1, -1), .35, colors.HexColor("#dce2dc")), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"), ("FONTSIZE", (0, 0), (-1, -1), 8), ("LEADING", (0, 0), (-1, -1), 11), ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8faf7")]), ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7), ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]))
    story += [table, Spacer(1, 14)]

    story += [Paragraph("1 / Portfolio thesis", styles["Section"]), Paragraph("We study how neural activity relates to behavior, then translate the work into accessible tools and explanations. The portfolio moves from a scientific question to a public, reviewable artifact without hiding uncertainty or collaboration boundaries.", styles["Body2"])]
    story += [Paragraph("2 / Flagship study", styles["Section"]), Paragraph("The mouse visual-cortex project compares stimulus-only and behavior-augmented ridge-regression encoding models on Sensorium recordings. Under the same pipeline, the original mouse rises from 0.1265 to 0.1583, a second mouse rises from 0.1543 to 0.2034, and a third rises from 0.1431 to 0.1905. Pupil improves all three animals; running varies by animal. A leave-one-animal-out sensitivity check keeps the mean gain positive in every omission. The claim remains about prediction, not causation.", styles["Body2"])]
    story += [Paragraph("3 / Complementary study", styles["Section"]), Paragraph("The EEG eye-state project tests whether causal temporal context improves classification from a public 14-channel EEG recording. The pointwise baseline reaches test ROC AUC 0.625; the first context extension reaches 0.530 on the final chronological block. Five forward-chaining folds average 0.478 and 0.488 ROC AUC, while 20 global label shuffles average 0.499 and 0.501. A 90-sample purge-gap sensitivity analysis averages 0.448 and 0.443. The negative result is retained because validation improvement did not guarantee held-out generalization.", styles["Body2"])]
    story += [Paragraph("4 / Translation layer", styles["Section"]), Paragraph("The neuro-divergent and neurocomms work contributes human-centered patterns for communication and accessibility applications. Those patterns are reused as mobile specifications, HTML explainers, presentation surfaces, PDF examples, video scripts, and scope/limitations notes for the research projects.", styles["Body2"])]
    story += [PageBreak(), Paragraph("5 / Evidence and reproducibility", styles["Section"]), Paragraph("The umbrella repository contains the reviewer index, contribution ledger, reproducibility checklist, interactive explainers, project reports, presentation outlines, and video production gates. The flagship repository now includes a core dependency manifest, a written replication protocol, and behavior-shuffle controls across three animals. The EEG project retains the downloaded ARFF data, provenance note, analysis script, metrics JSON, label-shuffle control, and report.", styles["Body2"])]
    story += [Paragraph("6 / Honest remaining work", styles["Section"]), Paragraph("Before submission, the applicant must personalize the essays with genuine experiences, extend the mouse replication beyond three animals for population-level uncertainty, and record the final videos in the applicant’s own voice. Descriptive within-animal bootstrap intervals are now documented, but this packet does not present population-level uncertainty as complete.", styles["Body2"])]
    story += [Paragraph("Portfolio links", styles["Section"]), Paragraph("GitHub hub: github.com/AmishI123/neuroscience-project/tree/main/portfolio<br/>Flagship code: github.com/AmishI123/neuroscience-project<br/>Live portfolio: amishi123.github.io/neuroscience-project", styles["Body2"]), Spacer(1, 18), Paragraph("Generated from the committed application materials. Source Markdown remains alongside this PDF.", styles["Small"])]
    doc.build(story)
    print(OUT)


if __name__ == "__main__":
    build()
