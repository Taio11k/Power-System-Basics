# Phase 8: Capstone and Portfolio Packaging (weeks 23–26, about 45 h)

**Phase outcome:** a complete, automated **grid connection study** for a solar PV + battery plant, written up as a consultancy-style report, plus a portfolio landing page, CV bullets and interview preparation.

---

## ⭐ The capstone: Grid Connection Study, PV + BESS plant on the CIGRE MV network

### The brief (treat it as if a client sent it)

> A developer wants to connect a **solar PV plant with a battery energy storage system (BESS)** to the 20 kV CIGRE MV benchmark network. You are the study engineer. Determine (1) the maximum plant export capacity that can be connected at the chosen bus without network reinforcement, (2) whether the connection meets the steady-state, fault-level and protection criteria, and (3) the mitigations needed for a larger plant. Deliver a study report and reproducible scripts.

You choose the **connection bus** using your P4 hosting-capacity results. You choose the **plant size** in the study itself (start near the hosting capacity, then test a larger case).

### Study scope (each item reuses a previous phase)

| # | Study | Reuses | Tool(s) |
|---|---|---|---|
| 1 | **Data and assumptions register**: network data, plant data, criteria. Every assumption gets an ID (A1, A2 …) and a source | all | Excel/Markdown |
| 2 | **Load flow, dimensioning cases:** (a) max PV export + min load, (b) no PV + max load, (c) BESS charging at max load | Phase 3 | PowerFactory + pandapower |
| 3 | **Contingency:** N-1 using the network's switches for alternative supply. Does the plant need to curtail in some outages? | Phase 3 | PF Contingency + `run_contingency` |
| 4 | **Voltage change** when the plant trips suddenly from full output. Compare it with a limit you take from a cited grid code (or label as an assumption) | Phases 3, 6 | PF + pandapower |
| 5 | **Reactive power capability** at the connection point: can the plant meet an assumed requirement (e.g. a power-factor range)? Use [RfG] as the framework and **state the national values as assumptions** | Phases 2, 6 | PF |
| 6 | **Short circuit (IEC 60909)** with and without the plant: equipment adequacy; **short-circuit ratio** SCR = S_k'' at the connection point / plant MW rating, with a weak-grid discussion | Phase 4 | PF + pandapower |
| 7 | **Protection impact:** re-check your P3 settings with the plant connected. Look for blinding and sympathetic tripping; propose setting changes | Phase 5 | Python TCC + PF/pandapower |
| 8 | **Time series (1 day or 1 year, 15-min):** voltage profile, line loading, and any **curtailment** needed to stay within limits. Show how the BESS reduces it | Phase 6 | pandapower time series / PF quasi-dynamic |
| 9 | **Dynamic (optional, if RMS is licensed):** a fault near the connection point. Does the plant stay connected (fault ride-through concept per [RfG])? Use a generic PV/static-generator model from the PowerFactory library and say which one | Phase 7 | PF RMS |

### Engineering standard you must meet

1. **Automation:** a single entry point, `python run_all_studies.py`, that:
   - runs every pandapower study,
   - drives PowerFactory through the Python API for the PF studies (or documents the manual steps if your licence blocks API use),
   - writes all tables to `results/*.csv` and all figures to `figures/*.png`.
2. **Cross-validation:** for each study type, a table comparing PF and pandapower on at least 3 key quantities, with differences explained.
3. **Assumptions register:** nothing appears in the report without a source or an assumption ID.
4. **Version control:** small, meaningful commits; a tagged release `v1.0` when finished.

### Repository layout
```
capstone-grid-connection-study/
├── README.md                    ← headline results first, then how to reproduce
├── report/Grid_Connection_Study.pdf
├── data/                        ← network data, profiles, assumptions_register.xlsx
├── src/
│   ├── pp_model.py              ← builds the pandapower model
│   ├── pf_runner.py             ← PowerFactory API wrapper
│   ├── studies/                 ← loadflow.py, contingency.py, shortcircuit.py, protection.py, timeseries.py
│   └── plotting.py
├── tests/                       ← e.g. "PF vs pandapower voltage difference < tolerance"
├── results/  figures/
└── run_all_studies.py
```

### Report template (consultancy style, 15–25 pages)
1. **Executive summary:** half a page. Max connectable capacity, key constraints, required mitigations. **Write it last.**
2. Introduction and scope
3. Network and plant description (SLD with the connection point highlighted)
4. Study criteria and assumptions register
5. Methodology and tools (versions, IEC 60909 method, cross-validation approach)
6. Results, one section per study 2–9 (tables + figures + a one-paragraph interpretation each)
7. Mitigation options and their effect
8. Conclusions and recommendations
9. Appendices: input data, full result tables, validation tables

### Suggested schedule
| Week | Work |
|---|---|
| 23 | Brief, assumptions register, models in both tools, studies 2–3 |
| 24 | Studies 4–7 |
| 25 | Study 8 (+9), automation clean-up, tests |
| 26 | Report writing, executive summary, portfolio packaging (below) |

**✅ Capstone is done when**
- [ ] `run_all_studies.py` reproduces every number in the report.
- [ ] The executive summary answers the 3 brief questions in under 200 words.
- [ ] Someone non-technical could read the first page and know the answer.

---

## Portfolio packaging (week 26)

### 1. Portfolio landing page (`power-systems-portfolio/README.md`)
- One line about you: "Engineer transitioning into power systems: load flow, short circuit (IEC 60909), protection, DER integration and stability studies in DIgSILENT PowerFactory and Python."
- **Skills matrix:** studies (rows) × tools (columns: PowerFactory, pandapower, PSCAD, MATLAB, Python API) with ✔ marks linking to the project that proves each one.
- **Project cards:** for each project, 1 image (SLD, TCC or hosting-capacity chart) + 1-sentence result + links to the README and PDF.
- **Honesty line:** "All projects are self-directed studies on public benchmark networks (CIGRE TB 575, WSCC 9-bus) with documented assumptions." Recruiters respect this; never present them as client work.

### 2. CV bullets (fill in **your real numbers**; never invent results)
Use this pattern: *action verb + study + tool + scale + verification/result*.
- "Performed IEC 60909 max/min short-circuit study of a 15-bus 20 kV benchmark network in DIgSILENT PowerFactory; cross-validated against pandapower (max deviation __ %)."
- "Coordinated IEC IDMT overcurrent relays on a radial MV feeder; achieved ≥ __ s grading margin for all fault locations."
- "Automated critical-clearing-time search for a 3-machine 9-bus system via the PowerFactory Python API."
- "Quantified PV hosting capacity (__ MW) of a CIGRE MV feeder with time-series simulation; Q(U) control increased it by __ %."
- "Delivered a grid connection study (load flow, N-1, IEC 60909, protection, time series) for a __ MW PV + BESS plant; fully reproducible Python pipeline."

### 3. LinkedIn
One post per project (P1–P5, capstone): the problem, one figure, one surprising lesson (e.g. a validation bug you found), and the repo link. Post them across weeks 10–26 as each project finishes, not all at the end.

### 4. Interview preparation: you should be able to answer all of these
1. What is reactive power and why does it matter for voltage?
2. Explain the per-unit system and why we use it.
3. What are PQ, PV and slack buses?
4. How does Newton-Raphson load flow work? When does it fail to converge?
5. What does N-1 mean? Give an example of a contingency violation and a fix.
6. Difference between I_k'', i_p and I_th? Which equipment rating does each check?
7. Why does IEC 60909 use a voltage factor c, and why are there max and min cases?
8. Why can a single-line-to-ground fault exceed a three-phase fault?
9. What does the vector group Dyn11 mean, and why does it matter for earth faults?
10. How do you grade two IDMT relays? What is the grading margin made of?
11. What is protection blinding?
12. Why does PV raise feeder voltage, and how does Q(U) control help?
13. Define hosting capacity.
14. What is the critical clearing time? Explain the equal-area criterion.
15. When do you need EMT (PSCAD) instead of RMS simulation?
16. What is the short-circuit ratio and why do inverter-based plants care about it?
17. Walk me through your capstone: the biggest constraint and how you'd mitigate it.
18. Tell me about a time two tools gave different answers. How did you find out why?

Write your answers in `career/interview_answers.md`, then practise saying each one aloud in under 2 minutes.

---

## After the course (optional next steps, by job target)
- **Grid connection / renewables consultancy:** harmonics and power-quality studies, more EMT modelling in PSCAD, grid code compliance studies.
- **Protection engineering:** distance (21) and differential (87) protection; IEC 61850 substation automation.
- **Distribution utility / DSO:** unbalanced 3-phase LV analysis (pandapower `runpp_3ph`, OpenDSS), smart-meter data analysis.
- **Energy system modelling:** PyPSA ([P-PYPSA]) for capacity expansion and market studies.
