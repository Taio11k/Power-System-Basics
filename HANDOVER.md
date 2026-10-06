# Handover: continue the course on any computer

GitHub is the one shared copy of this course and your work. Every PC and every cloud session pulls from it and pushes back to it. Claude's own memory stays on the computer where it was written, so the shared context lives in [CLAUDE.md](CLAUDE.md), which Claude Code reads automatically when you open this folder.

---

## Option A: Claude Code in the cloud (nothing to install)

1. Go to https://claude.ai/code and sign in with your Claude account.
2. Pick the repo **Taio11k/Power-System-Basics**. The first time, GitHub may ask you to give Claude access to the repo.
3. Paste the start prompt below.

You can run Python and pandapower in the cloud. **PowerFactory, PSCAD and MATLAB cannot run there**; do those steps on a PC where they are installed.

---

## Option B: a new local PC (one-time setup, about 30 min)

### 1. Install the tools
- **Git**: https://git-scm.com
- **GitHub CLI** (`gh`): https://cli.github.com
- **Claude Code**: the Claude desktop app (Code tab) or the CLI, signed in with **the same Claude account**
- **Python 3**, a version supported by pandapower (check https://pypi.org/project/pandapower), plus VS Code with the Python and Jupyter extensions
- Your licensed tools if this PC will run them: **PowerFactory, PSCAD** (with its Fortran compiler) and **MATLAB**. Check each licence's terms for using it on more than one computer.

### 2. Sign in to GitHub
Sign in as **Taio11k** (owner) or **DvEz373** (collaborator). Both can push.
```bash
gh auth login
```
```bash
gh auth setup-git
```

### 3. Get the repo
```bash
git clone https://github.com/Taio11k/Power-System-Basics.git
```
```bash
cd Power-System-Basics
```

### 4. Set your commit author for this repo
Use the same name and email as the earlier commits so the history stays consistent. See them with `git log -1 --format="%an <%ae>"`.
```bash
git config user.name "YOUR NAME"
```
```bash
git config user.email "YOUR EMAIL"
```

### 5. Create the Python environment
Windows:
```bash
python -m venv .venv
```
```bash
.venv\Scripts\activate
```
macOS or Linux: `python3 -m venv .venv`, then `source .venv/bin/activate`.
```bash
pip install -r requirements.txt
```
Check it works by running the minimal example in [course/00-setup.md](course/00-setup.md) (Step 0.2).

### 6. Open the folder in Claude Code and paste the start prompt below.

---

## Start prompt (paste at the beginning of every new session)

```text
I'm continuing my Power System Basics course from this repo.

1. Sync: run `git pull` so you have the latest work from my other computers and the cloud.
2. Load context: read CLAUDE.md, README.md, PROGRESS.md and HANDOVER.md, then the course/ file for the phase I'm on.
3. Check this machine: is the Python environment set up (.venv + requirements.txt)? If not, walk me through HANDOVER.md step by step. Ask me which of PowerFactory, PSCAD and MATLAB are installed here, and adapt the steps to that.
4. Tell me where I am: the current phase and step, its objective, what to read (exact chapters), the numbered actions, the file I must produce, and the check values.
5. Guide me through that one step. Wait for my results before moving to the next step, and check my numbers against the check values.

Rules: hand-hold me; don't skip steps. Don't invent facts, references or numbers. Verify them against credible sources and say when you can't.

When I say "wrap up": tick the finished steps in PROGRESS.md, add a line to LOG.md, then commit and push everything.
```

---

## Daily routine: keep every machine in sync

| When | Do |
|---|---|
| **Start of a session** | `git pull` (or ask Claude to pull) |
| **While working** | Tick boxes in `PROGRESS.md`; add a line to `LOG.md` |
| **End of a session** | Commit and push (or ask Claude to "commit and push my progress") |

**One machine at a time.** Push before you switch to another PC or the cloud, and pull when you arrive. If you forget and Git reports a conflict, ask Claude to resolve it.

---

## What syncs and what doesn't

| Item | Syncs through GitHub? | Notes |
|---|---|---|
| Course files, your notebooks, scripts, reports | ✅ yes | Commit them |
| `PROGRESS.md`, `LOG.md`, `GLOSSARY.md` | ✅ yes | Commit them |
| `CLAUDE.md` (Claude's project context) | ✅ yes | Update it when something important changes |
| Claude's memory on each PC | ❌ no | Put anything Claude must always know into `CLAUDE.md` |
| Python `.venv/` | ❌ no | Rebuild it per PC with `pip install -r requirements.txt` |
| PowerFactory project exports (`*.pfd`) | ❌ no (ignored) | `.gitignore` leaves them out because they can be large. To sync them, remove `*.pfd` from `.gitignore`; for big files, use Git LFS |
| Software licences | ❌ no | Installed per PC; never commit licence files |

---

## Websites (update automatically or on request)
- **Public site:** https://taio11k.github.io/Power-System-Basics/ redeploys automatically when `web/` changes on `main`.
- **claude.ai copy:** https://claude.ai/artifact/CNg9KrHXyNkaiGcmMBEQQq is private and updates only when Claude republishes it. Ask for that after page changes.
