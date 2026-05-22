# active-learning-video-expt

A single-paper experiment: **does watching the author's seminar talk on YouTube add insights beyond reading the underlying research paper?** Run end-to-end by an autonomous agent.

## What this is

This repo is not code. It's a **workflow specification** ([`problem_statement.md`](problem_statement.md)) that an autonomous agent (Claude Code) executes when the user fires `/goal at problem_statement.md`. The 8-step workflow:

1. Download Siddhartha Mishra's group's paper (Molinaro et al., *Neural Inverse Operators for Solving PDE Inverse Problems*, arXiv:2301.11167) via `/paper-download-hack`.
2. Read the paper thoroughly (35 pages including appendices).
3. Use the pre-pinned YouTube URL — verified against arXiv author order to be a first-author talk.
4. Download and transcribe the 138-min seminar via `/yt-video-processing` (Whisper `small`).
5. Populate [`video_insights.md`](video_insights.md) using a deliberately rigid YES/NO-first schema designed to prevent the agent from rationalizing a flattering narrative.
6. Generate a 2-page summary PDF via `/pdf`.
7. Email the PDF via `/email`.
8. Commit, push, and generate this README via `/gitcommit` → `/gitpush` → `/gitreadme`.

## The honest finding

The relevant speaker is **Roberto Molinaro** (ETH Zürich), the first author of the paper — cross-checked against the arXiv author order (Molinaro, Yang, Engquist, Mishra). Of the 138-minute CRUNCH Group seminar, only the first ~73 minutes are relevant: the second talk is unrelated PINNs work on relativistic hydrodynamics by Ferrer-Sánchez and Font and was excluded per the workflow spec.

After running the workflow end-to-end on 2026-05-22:

- **(a) Did the video cover key points explicitly that were implicit in the paper?** **YES** — but a measured YES. Two modest additions: a heuristic for the surprisingly good OOD robustness (training implicitly restricts the output function class), and a reframing of randomized batching as distribution-statistics probing. Both are intuitions, not new conceptual content.
- **(c) Did anything suddenly click in the video that didn't from the paper?** **NO.**

The paper's single deepest content — the Section 3.3 motivating calculation that derives the architecture 1:1 from a 4-step analytical inversion (Basis Construction → PDE Solve → Mode Mixing → Matrix Inversion) — is **omitted** from the video. The paper is more thorough on essentially every other axis.

Full report: [`video_insights.md`](video_insights.md) and [`summary.pdf`](summary.pdf).

## Files

| File | Purpose |
|---|---|
| `problem_statement.md` | The workflow spec — read by the agent at `/goal at problem_statement.md` |
| `CLAUDE.md` | Project context loaded by Claude Code at session start |
| `video_insights.md` | Step 5 output — honest a/b/c/d evaluation of video vs paper |
| `summary.pdf` | Step 6 output — 2-page summary plus reflections on agent video-based learning |
| `reflections.md` | Post-run conversational reflections on the AI/human video-consumption asymmetry |
| `affection.md` | Vivek's running journal of orange-robot moments worth keeping |
| `papers/2301.11167.pdf` | The Mishra-group paper (arXiv open access) |
| `video/transcript.txt`, `video/transcript.json` | Whisper transcription of the full 138-min seminar |
| `video/molinaro_only.txt` | First 73 min only (Molinaro talk + Q&A), with `[mm:ss]` timestamps |
| `video/frames/` | 276 scene-cut JPGs from the seminar recording |
| `make_summary_pdf.py` | One-off reportlab script that built `summary.pdf` |
| `send_summary_email.py` | One-off MIME encoder used for Step 7 (PDF attachment via Gmail) |

## How to re-run

```bash
claude   # start a Claude Code session in this directory
```

Then in the session:

```
/goal at problem_statement.md
```

The agent executes all 8 steps without further prompting. A full run takes roughly 20–25 minutes end-to-end, dominated by the Whisper transcription (~16 min for 138 min of audio at ~6× realtime on CPU). Outputs are designed to be **honest** — the YES/NO-first schema in Step 5 prevents the agent from inflating the finding even when the underlying result is a null result.

## Stack

- **Python venv** (project-local `.venv/`, gitignored) with **reportlab 4.5.1** for `summary.pdf` generation
- **Whisper** (`small`, int8 CPU) for video transcription, invoked via the `/yt-video-processing` composite skill
- **yt-dlp** for video download and metadata cross-verification against arXiv
- **GWS CLI** for the Gmail send in Step 7 (authenticated as `vivekkmk.assistant@gmail.com`)
- **gh CLI** + GitHub for the public repo
- **Claude Code** as the autonomous executor

## Reflection (TL;DR from `summary.pdf`)

For a research paper that is already thorough and well-written, a ~60-minute author talk is unlikely to deliver insights that aren't already in the paper. An autonomous agent should engage in video-based learning only when (i) the paper has been read first, (ii) a specific ambiguity survives the read, (iii) the video is verifiably by an author, (iv) the video is not a multi-speaker seminar (or its segment boundaries are pre-pinned in the workflow spec), and (v) the agent commits to a binary honesty-first evaluation structure to avoid post-hoc narrative inflation.

## License

The Mishra-group paper (`papers/2301.11167.pdf`) is © its authors and was retrieved via arXiv under arXiv's standard preprint terms. Everything else in this repo is the output of a single autonomous experimental run.
