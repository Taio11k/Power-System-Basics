# Progress Tracker

Tick a box only when that step's **✅ Done when** checklist is fully true. Record the dates.

Started on: 2026-10-07 · Target finish (start + 26 weeks): 2027-04-07

## Phase 0: Setup (week 1)
- [ ] 0.1 Job-posting analysis → `career/job-postings.md`
- [ ] 0.2 Python + pandapower runs
- [x] 0.3 GitHub portfolio repo skeleton (Taio11k/power-systems-portfolio, private for now)
- [ ] 0.4 Licence limits recorded; PSCAD first simulation + Fortran compiler OK
- [ ] 0.5 Big picture SLD drawing, `GLOSSARY.md`, `LOG.md`

## Phase 1: AC fundamentals (weeks 2–4)
- [ ] 1.1 Phasors and impedance (check: I ≈ 16.26 A ∠−45°)
- [ ] 1.2 Complex power and PF correction (check: 42.1 kvar)
- [ ] 1.3 Three-phase (check: 144.3 A)
- [ ] Phase 1 checkpoint answered

## Phase 2: Components and per-unit (weeks 5–7)
- [ ] 2.1 Transformers (check: 0.0102 Ω, 22.7 kA)
- [ ] 2.2 Per-unit (check: 4 Ω, 2.887 kA, 6.35 p.u.)
- [ ] 2.3 Lines and cables (check: ≈ 1.56 % drop)
- [ ] 2.4 Sources and loads
- [ ] 2.5 Mini-project A: pandapower ↔ PowerFactory match

## Phase 3: Power flow (weeks 8–10)
- [ ] 3.1 Y_bus by hand + `build_ybus`
- [ ] 3.2 Own Newton-Raphson solver validated vs MATPOWER and pandapower
- [ ] 3.3 Limits and mitigation exercise
- [ ] 3.4 9-bus in PowerFactory
- [ ] 3.5 N-1 contingency in both tools
- [ ] ⭐ **P1 published**

## Phase 4: Short circuit (weeks 11–13)
- [ ] 4.1 Symmetrical faults
- [ ] 4.2 Symmetrical components
- [ ] 4.3 Unsymmetrical faults
- [ ] 4.4 IEC 60909 in pandapower + PowerFactory (CIGRE MV)
- [ ] ⭐ **P2 published**

## Phase 5: Protection (weeks 14–16)
- [ ] 5.1 Philosophy and hardware
- [ ] 5.2 IDMT + TCC tool (check: 0.297 s)
- [ ] 5.3 Radial feeder coordination
- [ ] 5.4 DER impact reading
- [ ] ⭐ **P3 published**

## Phase 6: Distribution and DER (weeks 17–19)
- [ ] 6.1 Voltage rise study
- [ ] 6.2 Time series (pandapower + PF quasi-dynamic)
- [ ] 6.3 Hosting capacity (deterministic + stochastic)
- [ ] 6.4 Mitigations
- [ ] ⭐ **P4 published**

## Phase 7: Stability and EMT (weeks 20–22)
- [ ] 7.1 Stability classification
- [ ] 7.2 SMIB (check: δ_cr ≈ 79.6°, t_cr ≈ 0.247 s)
- [ ] 7.3 PowerFactory RMS + automated CCT search
- [ ] 7.4 PSCAD fault + i_p vs IEC 60909
- [ ] ⭐ **P5 published**

## Phase 8: Capstone and portfolio (weeks 23–26)
- [ ] Assumptions register + models
- [ ] Studies 2–8 (+9 optional)
- [ ] `run_all_studies.py` reproduces everything
- [ ] Report PDF + executive summary
- [ ] ⭐ **Capstone published (tag v1.0)**
- [ ] Portfolio landing page
- [ ] CV bullets with real numbers
- [ ] 18 interview answers written and practised
