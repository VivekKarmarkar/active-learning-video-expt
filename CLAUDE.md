# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

An experiment investigating whether YouTube videos provide insights that complement (or surface things missed by) reading the underlying research paper. The "codebase" is not code — it is a workflow specification (`problem_statement.md`) that an autonomous agent executes end-to-end on the user's command.

The specific paper under study is Siddhartha Mishra (ETH Zürich) et al.'s work on **Neural Inverse Operators**.

## Execution protocol

The user triggers a full run by invoking:

```
/goal at problem_statement.md
```

At that point the agent must autonomously execute the 8-step workflow in `problem_statement.md` without further prompting. The steps chain these skills in order:

1. `paper-download-hack` — locate and download the Mishra paper
2. Read the paper thoroughly (no skill — direct Read of the PDF)
3. (Pre-pinned) Use the verified YouTube URL embedded in `problem_statement.md` — a CRUNCH Group dual-talk seminar where the first speaker, Roberto Molinaro (ETH Zürich, first author of the paper), presents the work. Only Molinaro's portion is relevant; the second talk (PINNs for relativistic hydrodynamics) is unrelated. Playwright not needed.
4. `yt-video-processing` — download and process the video (this is the agent's substitute for "watching")
5. Populate `video_insights.md` honestly using the a/b/c/d schema (see below)
6. `pdf` — write a short summary focused on `video_insights.md` plus reflections on video-based learning for autonomous agents
7. `email` — send the PDF to `vivekjobapp123@gmail.com`
8. `gitcommit` → `gitpush` → `gitreadme`

Per the user's global "Strict Composition Enforcement" rule, follow the steps in order with no shortcuts.

## The honesty mandate (Step 5)

`video_insights.md` is populated using a deliberately rigid structure:

- **(a)** YES/NO — did the video cover key points that were only implicit in the paper?
- **(b)** If YES, list them. If NO, write `NA`.
- **(c)** YES/NO — did any insights *suddenly click* from the video that did *not* click from the paper?
- **(d)** If YES, list them. If NO, write `NA`.

The binary-first structure exists to prevent the agent from waffling into a flattering narrative. If the video added nothing, the honest answer is `NO`/`NA` — and that null result is the actual finding of the experiment.

Do not soften, hedge, or pad these answers. Do not invent insights the video did not actually produce.

## Files

- `problem_statement.md` — the workflow spec (the contract; never modify during an autonomous run)
- `video_insights.md` — the honest output of Step 5 (empty until a run completes)
- `CLAUDE.md` — this file
