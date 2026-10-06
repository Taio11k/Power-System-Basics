# Project context for Claude

This repo is a guided, self-study course: **power system basics → a junior power systems engineer portfolio**. Claude helps the learner follow it, answers questions, reviews their work and keeps the course files current.

## The learner
- Engineering degree in a non-power field, some Python, 10–12 h/week.
- Target: a junior power systems / grid studies engineer job. The portfolio must look like real consultancy studies.
- Follows **IEC** standards (230/400 V, 50 Hz), not NEC.
- Has student licences for **DIgSILENT PowerFactory, PSCAD and MATLAB**. These are installed on the learner's own PCs, not in cloud sessions. In the cloud, only Python (pandapower, numpy, etc.) can run; give PowerFactory and PSCAD steps as instructions to follow.
- Wants very guided ("hand-hold") instructions: exact reading, numbered actions, a deliverable, and check values for every step.

## Rules for content
- **Do not invent facts.** Every book, chapter, standard clause, API and number must be verified against a credible source (publisher page, official docs, standard body) before it goes in. When a value comes from a paid standard and cannot be verified, tell the learner to look it up and cite it; don't guess it.
- Recompute every worked check value numerically before publishing it.
- Chapter numbers refer to the editions listed in `REFERENCES.md`.

## Files
- `README.md`: start page, end goal, phase map
- `course/00-setup.md` … `course/08-capstone-portfolio.md`: one file per phase; every step has Objective / Learn / Do / Output / Done when / Traps
- `PROGRESS.md`: the learner's tick-box tracker
- `HANDOVER.md`: setup for a new PC or the cloud, the sync routine, and the start prompt
- `requirements.txt`: Python packages for the course
- `REFERENCES.md`: verified references with codes such as [GLOVER] and [PP-SC]
- `web/power-system-basics.html`: the **single source** of the course web page (a fragment without doctype/html/head/body tags)
- `web/build_pages.sh` + `.github/workflows/pages.yml`: GitHub Pages build and deploy

## Publishing the web page
- **GitHub Pages:** pushing changes under `web/` to `main` deploys automatically to https://taio11k.github.io/Power-System-Basics/
- **claude.ai copy:** https://claude.ai/artifact/CNg9KrHXyNkaiGcmMBEQQq (private). After changing the page, republish the same file to that URL: read the artifact first, then publish with `url` set to it.
- Keep the course markdown and the web page consistent when either changes.

## Git
- Owner account: **Taio11k** (admin). Collaborator: **DvEz373** (write).
- Default branch `main`. Use small, descriptive commits.
- The learner works from several PCs and the cloud. Pull before starting work, and commit and push at the end of every session (including `PROGRESS.md`), so the next machine sees the latest state.
