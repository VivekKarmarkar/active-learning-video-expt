"""Generate summary.pdf for the active-learning-video-expt project.

Short report (2-3 pages) covering the experimental setup, the honest a/b/c/d
findings from video_insights.md, and reflections on directing autonomous agents
to do video-based learning for research-paper tasks.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable,
)
from reportlab.lib import colors


def build_styles():
    base = getSampleStyleSheet()
    styles = {
        "title": ParagraphStyle(
            "title", parent=base["Title"],
            fontSize=16, leading=20, spaceAfter=6, alignment=TA_LEFT,
        ),
        "subtitle": ParagraphStyle(
            "subtitle", parent=base["Normal"],
            fontSize=9, leading=12, textColor=colors.grey, spaceAfter=12,
        ),
        "h2": ParagraphStyle(
            "h2", parent=base["Heading2"],
            fontSize=12, leading=15, spaceBefore=10, spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "body", parent=base["BodyText"],
            fontSize=10, leading=13, alignment=TA_JUSTIFY, spaceAfter=6,
        ),
        "bullet": ParagraphStyle(
            "bullet", parent=base["BodyText"],
            fontSize=10, leading=13, alignment=TA_JUSTIFY, leftIndent=14,
            bulletIndent=0, spaceAfter=4,
        ),
        "ab": ParagraphStyle(
            "ab", parent=base["BodyText"],
            fontSize=10, leading=13, alignment=TA_JUSTIFY, leftIndent=14,
            spaceAfter=6,
        ),
    }
    return styles


def hr():
    return HRFlowable(width="100%", thickness=0.4, color=colors.lightgrey,
                      spaceBefore=4, spaceAfter=8)


def main():
    out_path = "/home/vivekkarmarkar/Python Files/active-learning-video-expt/summary.pdf"
    doc = SimpleDocTemplate(
        out_path, pagesize=letter,
        leftMargin=0.85*inch, rightMargin=0.85*inch,
        topMargin=0.7*inch, bottomMargin=0.7*inch,
        title="Active Learning Video Experiment — Summary",
        author="Autonomous run, Claude Code",
    )
    s = build_styles()
    story = []

    # Title
    story.append(Paragraph(
        "Does YouTube Help an Autonomous Agent Understand a Research Paper?",
        s["title"],
    ))
    story.append(Paragraph(
        "Project: <b>active-learning-video-expt</b> &nbsp;|&nbsp; "
        "Paper: Molinaro, Yang, Engquist, Mishra (2023), "
        "<i>Neural Inverse Operators for Solving PDE Inverse Problems</i> "
        "(arXiv:2301.11167) &nbsp;|&nbsp; "
        "Video: CRUNCH Group seminar, 2023-07-29, presented by first author "
        "Roberto Molinaro &nbsp;|&nbsp; "
        "Run date: 2026-05-22",
        s["subtitle"],
    ))
    story.append(hr())

    # Section 1 — Setup
    story.append(Paragraph("1. The experiment", s["h2"]))
    story.append(Paragraph(
        "An autonomous agent executed an 8-step workflow defined in "
        "<font face='Courier'>problem_statement.md</font>: "
        "download the Molinaro et al. paper (open-access via arXiv), read all 35 "
        "pages thoroughly, download and transcribe the 138-minute CRUNCH Group "
        "seminar (Whisper small, ~6&times; realtime on CPU), isolate the first "
        "73 minutes of the transcript (Molinaro's talk plus the Q&amp;A on his "
        "talk &mdash; the second talk on relativistic-hydrodynamics PINNs by "
        "Ferrer-Sánchez and Font was pre-flagged as unrelated and excluded), "
        "and then populate <font face='Courier'>video_insights.md</font> using "
        "the deliberately rigid binary-first a/b/c/d schema. "
        "The schema's purpose is to prevent the agent from rationalizing a "
        "flattering &ldquo;the video taught me a lot&rdquo; narrative.",
        s["body"],
    ))

    # Section 2 — Findings
    story.append(Paragraph("2. Honest findings", s["h2"]))

    story.append(Paragraph(
        "<b>(a) Did the video cover key points explicitly that were implicit "
        "in the paper? &mdash; YES</b> (a measured yes).",
        s["ab"],
    ))

    story.append(Paragraph(
        "<b>(b) Two additions, both modest:</b>",
        s["ab"],
    ))

    story.append(Paragraph(
        "&bull; <b>Heuristic for OOD robustness.</b> The paper reports (Table 11) "
        "that NIO generalizes well out-of-distribution despite the underlying "
        "inverse map being only weakly stable. The paper does not explain why. "
        "In the video (~55:25), Molinaro offers the hand-wave: training "
        "implicitly restricts the model's output function class, producing a "
        "<i>practical</i> stability stronger than the <i>analytical</i> weak "
        "stability of the map. He admits this has no proof.",
        s["bullet"],
    ))
    story.append(Paragraph(
        "&bull; <b>Reframing of randomized batching.</b> Section 3.4 of the "
        "paper introduces randomized batching as bagging-inspired permutation "
        "training for <i>L-tilde</i>-invariance (varying the number of "
        "operator samples at test time). In the video (~38:30), Molinaro "
        "reframes it: instead of just feeding the empirical mean of the "
        "<i>f<sub>l</sub></i> representations, you could compute multiple "
        "statistics (mean, std, min, max, &hellip;) and feed all of them; "
        "randomized batching is &ldquo;a more efficient way&rdquo; of achieving "
        "this distribution-probing effect over training iterations.",
        s["bullet"],
    ))

    story.append(Paragraph(
        "<b>Honest caveat:</b> the single most important conceptual content "
        "in the paper &mdash; the Section 3.3 motivating calculation that "
        "derives NIO's architecture 1:1 from a 4-step analytical inversion "
        "(Basis Construction &rarr; PDE Solve &rarr; Mode Mixing &rarr; "
        "Matrix Inversion, mapping to trunk-net, branch-net, and FNO "
        "nonlinear layers) &mdash; is <i>omitted</i> from the video. The "
        "video collapses this into a 2-step heuristic. The paper is more "
        "thorough on essentially every other axis.",
        s["ab"],
    ))

    story.append(Paragraph(
        "<b>(c) Did anything suddenly click in the video that didn't from the "
        "paper? &mdash; NO.</b>",
        s["ab"],
    ))
    story.append(Paragraph(
        "<b>(d) NA.</b>",
        s["ab"],
    ))

    # Section 3 — Reflections
    story.append(Paragraph(
        "3. Should autonomous agents engage in video-based learning?",
        s["h2"],
    ))

    story.append(Paragraph(
        "Tentative conclusion from this single-paper experiment: "
        "<b>not as a default</b>, but worth keeping as a conditional tool. "
        "Reasons:",
        s["body"],
    ))

    story.append(Paragraph(
        "&bull; <b>Cost.</b> ~16 minutes of compute to download and transcribe "
        "138 minutes of audio, plus ~5 min of agent context-budget to read "
        "73 min of transcript. A 35-page paper takes ~1&ndash;2 min to read "
        "with the same agent.",
        s["bullet"],
    ))
    story.append(Paragraph(
        "&bull; <b>Asymmetric information yield.</b> Papers are the canonical "
        "artifact; authors write them precisely because they want a "
        "definitive technical record. Talks are pedagogical surfaces "
        "optimized for live audiences, with content selectively trimmed.",
        s["bullet"],
    ))
    story.append(Paragraph(
        "&bull; <b>Hallucination risk on dual-talk seminars.</b> This run "
        "came close to a categorical failure mode. The video contained a "
        "second unrelated talk; without the pre-pinned segment cutoff in "
        "<font face='Courier'>problem_statement.md</font>, the agent could "
        "have ingested both talks and attributed insights from the wrong "
        "paper. Video sources are not as self-clearly bounded as PDFs.",
        s["bullet"],
    ))
    story.append(Paragraph(
        "&bull; <b>Honesty pressure.</b> The temptation to inflate &ldquo;the "
        "video taught me X&rdquo; is real. The binary-first a/b/c/d structure "
        "in this experiment forced an explicit YES/NO before any narrative, "
        "and held the answer to a <i>measured</i> yes. An unsupervised "
        "agent without such a gate would likely generate a flattering "
        "&ldquo;watched a great video, learned a lot&rdquo; report.",
        s["bullet"],
    ))

    story.append(Paragraph(
        "<b>Suggested heuristic.</b> Direct an autonomous agent to engage in "
        "video-based learning only when <i>all</i> of:",
        s["body"],
    ))
    story.append(Paragraph(
        "(i) the paper has been read first; "
        "(ii) a specific ambiguity survives the read; "
        "(iii) the video is verifiably by an author (cross-check arXiv "
        "author order, as done here); "
        "(iv) the video is not a multi-speaker seminar &mdash; or if it is, "
        "the relevant segment boundaries are pre-pinned in the workflow spec; "
        "(v) the agent commits to a binary honesty-first evaluation structure "
        "before reasoning.",
        s["ab"],
    ))
    story.append(Paragraph(
        "When all five hold, ~20 min of additional compute can be worth it. "
        "When any fails, the marginal information yield does not justify "
        "the cost &mdash; and the failure modes (wrong-talk attribution, "
        "narrative inflation) outweigh the value.",
        s["body"],
    ))

    doc.build(story)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
