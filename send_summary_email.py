"""One-off encoder for an email with a PDF attachment.

The shared ~/.claude/skills/email/scripts/encode_email.py is text-only by design
(do not modify per the cardinal rule). This helper builds a multipart MIME
message with the project's summary.pdf attached and prints the base64url-encoded
raw string suitable for the Gmail API messages.send `raw` field.
"""

import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from pathlib import Path

PROJECT = Path("/home/vivekkarmarkar/Python Files/active-learning-video-expt")

BODY = """Hi,

Attaching the autonomous-run summary from the active-learning-video-expt project.

Setup: an autonomous agent compared (a) Molinaro, Yang, Engquist, Mishra (2023), "Neural Inverse Operators for Solving PDE Inverse Problems" (arXiv:2301.11167, from Siddhartha Mishra's group at ETH Zürich) against (b) the 73-minute first-author CRUNCH Group seminar by Roberto Molinaro. The rest of the 138-min recording is an unrelated second talk on relativistic-hydrodynamics PINNs and was excluded per the workflow spec.

Honest finding (using the binary-first a/b/c/d schema in problem_statement.md):
- (a) YES — the video covers a few points more explicitly than the paper does: an OOD-robustness heuristic, and a reframing of randomized batching as distribution-statistics probing. Both are modest additions.
- (c) NO — nothing in the video produced a "sudden click" that wasn't already clear from the paper.

The paper omitted from the video: the Section 3.3 motivating calculation that derives NIO's architecture 1:1 from a 4-step analytical inversion (Basis Construction → PDE Solve → Mode Mixing → Matrix Inversion). This is arguably the paper's deepest content and is absent from the talk.

Full report and reflections on whether autonomous agents should engage in video-based learning are in the attached PDF and in video_insights.md in the project repo.

Repo: https://github.com/VivekKarmarkar/active-learning-video-expt

— Vivek (via Claude Code autonomous run, 2026-05-22)
"""

def main():
    msg = MIMEMultipart()
    msg["From"] = "vivekkmk.assistant@gmail.com"
    msg["To"] = "vivekjobapp123@gmail.com"
    msg["Subject"] = "Active-learning video experiment — summary (Neural Inverse Operators / Mishra group)"

    msg.attach(MIMEText(BODY, "plain", "utf-8"))

    pdf = PROJECT / "summary.pdf"
    attach = MIMEApplication(pdf.read_bytes(), _subtype="pdf")
    attach.add_header("Content-Disposition", "attachment", filename="summary.pdf")
    msg.attach(attach)

    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode("ascii")
    print(raw)


if __name__ == "__main__":
    main()
