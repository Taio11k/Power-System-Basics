# Power System Basics → Junior Power Systems Engineer Portfolio

**Web version:** [Power System Basics on claude.ai](https://claude.ai/artifact/CNg9KrHXyNkaiGcmMBEQQq) (an interactive roadmap with progress ticks).

A guided course, from zero to a portfolio. It assumes an engineering degree in another field, some Python, and 10+ hours a week. It follows **IEC** standards (230/400 V, 50 Hz).

---

## 🎯 The end goal (what "finished" means)

After about **26 weeks** you will have a **public GitHub portfolio with 5 study projects and 1 capstone**. Each one has the same structure as real consultancy and utility work:

| # | Project | Tools | Real job equivalent |
|---|---|---|---|
| P1 | Load flow and N-1 contingency study (9-bus transmission system) | PowerFactory + pandapower | Network planning study |
| P2 | IEC 60909 short-circuit study (CIGRE MV network) | PowerFactory + pandapower | Fault level / switchgear rating check |
| P3 | Overcurrent protection coordination (radial MV feeder) | Python TCC tool + PowerFactory or pandapower | Protection setting study |
| P4 | PV hosting capacity with time series (CIGRE MV/LV) | pandapower time series + PowerFactory quasi-dynamic | DER / distribution planning study |
| P5 | Transient stability: critical clearing time (9-bus) plus one EMT demo | PowerFactory RMS + Python API, PSCAD | Dynamic study |
| ⭐ **Capstone** | **Grid connection study for a solar PV + battery plant**, automated with Python, published as a consultancy-style PDF report | All of the above | **This is the exact work that graduate power systems engineers are hired for** |

**The outcome:** in an interview you can say "I ran load flow, N-1, IEC 60909 short circuit, protection coordination, hosting capacity and transient stability studies in PowerFactory, automated them with Python, and cross-validated the results in pandapower. Here are the reports." That sentence matches the requirements in graduate job postings ([REFERENCES.md → G](REFERENCES.md#g-job-market-evidence-why-the-course-is-built-this-way)).

---

## 🗺️ The map

```
Phase 0  Setup & orientation ........................ week 1
Phase 1  AC & three-phase fundamentals .............. weeks 2–4
Phase 2  Components & the per-unit system ........... weeks 5–7
Phase 3  Power flow  ──────────────► P1 ............. weeks 8–10
Phase 4  Faults & IEC 60909 short circuit ─► P2 ..... weeks 11–13
Phase 5  Protection basics ─────────► P3 ............ weeks 14–16
Phase 6  Distribution & solar (DER) integration ─► P4  weeks 17–19
Phase 7  Stability & EMT intro ─────► P5 ............ weeks 20–22
Phase 8  CAPSTONE + portfolio packaging ............. weeks 23–26
```

| Phase | File |
|---|---|
| 0 | [course/00-setup.md](course/00-setup.md) |
| 1 | [course/01-ac-fundamentals.md](course/01-ac-fundamentals.md) |
| 2 | [course/02-components-per-unit.md](course/02-components-per-unit.md) |
| 3 | [course/03-power-flow.md](course/03-power-flow.md) |
| 4 | [course/04-short-circuit.md](course/04-short-circuit.md) |
| 5 | [course/05-protection.md](course/05-protection.md) |
| 6 | [course/06-distribution-der.md](course/06-distribution-der.md) |
| 7 | [course/07-stability-emt.md](course/07-stability-emt.md) |
| 8 | [course/08-capstone-portfolio.md](course/08-capstone-portfolio.md) |
| — | [PROGRESS.md](PROGRESS.md): tick boxes as you go |
| — | [REFERENCES.md](REFERENCES.md): every book, paper, standard and doc, with links |

---

## 🧭 How to use this course (read once)

1. **Do the phases in order.** Each phase depends on the one before it.
2. **Every step has the same 6 parts:**
   - **🎯 Objective**: what you will be able to do
   - **📖 Learn**: exactly what to read or watch (reference codes are in REFERENCES.md)
   - **🛠️ Do**: numbered actions; follow them literally
   - **📦 Output**: the file you must produce
   - **✅ Done when**: the self-check. Move on only when every box is true
   - **⚠️ Traps**: the mistakes beginners usually make here
3. **A weekly rhythm that works for 10–12 hours:**
   - 2 sessions × 2 h: **Learn** (read with pen and paper, redo the textbook examples by hand)
   - 2 sessions × 2–3 h: **Do** (code and simulation)
   - 1 session × 1 h: **Write** (update `LOG.md` and your project README)
4. **The validation rule:** never trust one tool. Check every number at least two ways: by hand ↔ Python ↔ PowerFactory. Recruiters and senior engineers value this habit above all.
5. **When stuck for more than 45 minutes:** write down exactly what you expected versus what you got, re-read the "Traps" section, then ask (an AI, a forum, or a lecturer) with that note.

## 🧰 Your toolset

| Tool | Role in this course |
|---|---|
| **DIgSILENT PowerFactory** (student licence) | Main **industry** tool for every study. Check your licence's node limit and included modules in Phase 0 |
| **Python + pandapower** | Your **automation and cross-validation** tool, and your public GitHub code |
| **PSCAD** (student/free) | EMT (electromagnetic transient) demo in Phase 7 |
| **MATLAB** | Optional companion for the [SAADAT] book examples and MATPOWER |
| **Git + GitHub** | Your public portfolio |

## 📚 Minimum reading kit

- **Must have:** [GLOVER] 7th ed. SI (main) + [VONMEIER] (intuition). Both are in [REFERENCES.md](REFERENCES.md).
- **Free:** [MIT] 6.061 notes, [NPTEL] videos, [EIG] wiki, pandapower docs.
- **Borrow when needed:** [GERS] (Phase 5), [BOLLEN] (Phase 6), [KUNDUR] or [MACHOWSKI] (Phase 7).
