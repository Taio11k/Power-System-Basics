# Tool licences and limits (Step 0.4)

Recorded on 2026-10-07 on the main Windows PC.

## DIgSILENT PowerFactory 2024

Source: **Help → About PowerFactory**.

- **Version:** PowerFactory 2024 (x64), build 24.0.2.0 (24037) / rev. 108412
- **Licence:** CodeMeter 6.50 (Workstation), **unlimited number of nodes**, valid without time limit
- **Maintenance:** active, up to and including 30/12/2099
- **Python API:** works from Python 3.12 (PowerFactory ships API folders for Python 3.8–3.12). Tested with `00_setup/test_powerfactory.py` in engine mode.

### Modules the course needs

| Phase | Module | Licensed? |
|---|---|---|
| 3 | Load flow (base package), Contingency Analysis | ✅ |
| 4 | Short circuit, IEC 60909 (base package) | ✅ |
| 5 | Time-Overcurrent Protection | ✅ |
| 6 | Quasi-Dynamic Simulation | ✅ |
| 7 | Stability Analysis Functions (RMS) | ✅ |
| 7 | Electromagnetic Transients (EMT) | ✅ |
| 3, 7, 8 | Scripting and Automation (Python API) | ✅ |

None of the course's "if not licensed" fallback paths are needed.

### All licensed modules

**Individual modules:** Contingency Analysis · Quasi-Dynamic Simulation · Network Reduction · Time-Overcurrent Protection · Distance Protection · Arc-Flash Analysis · Cable Analysis · Power Quality and Harmonic Analysis · Connection Request Assessment · Transmission Network Tools · Distribution Network Tools · Economic Analysis Tools · Probabilistic Analysis · Reliability Analysis Functions · OPF (Reactive Power Optimisation) · OPF (Economic Dispatch) · Unit Commitment and Dispatch Optimisation · Techno-Economical Analysis · State Estimation · Stability Analysis Functions (RMS) · Electromagnetic Transients (EMT) · Motor Starting Functions · Small Signal Stability (Eigenvalue Analysis) · System Parameter Identification · Scripting and Automation · PFM Master Station · OPC Interface · C37 Simulation Interface · Co-Simulation Interface · CIM Import (ENTSO-E Profile) · CIM Import/Export (ENTSO-E Profile)

**Corporate modules:** Multi-User Database · PSS/E Export · Integral Export · CIM Import/Export (ENTSO-E Profile) - corp. · NG · Enedis

### Examples available (Help → Welcome to PowerFactory → Examples)

- **Application examples:** LV Distribution Network · MV Distribution Network · Transmission System · Texas Grid · Industrial Network · MV Microgrid · Hydro Power Plant · Wind Farm · Offshore Wind Farm · Railway Systems · Advanced Protection · Switching Transients · Lightning Transients · State Estimation · MMC STATCOM
- **Examples from literature:** 9 Bus System · 14 Bus System · 39 Bus System · 13 Node Feeder · RBTS Bus 2 · SSR · HVDC-LCC · Resonance Studies · CIGRE 604 HVDC-MMC
- **Examples from standards:** IEC 60909 Examples 1–4 · IEC 61363 · IEC 61660 · IEEE Std. 399-1997 · D-A-CH-CZ 2nd Edition · BDEW / VDE-AR-N 4110 · VDE-AR-N 4105

Useful later: **9 Bus System** (Phases 3 and 7), **IEC 60909 Examples** (Phase 4), **LV Distribution Network** with its quasi-dynamic and hosting-capacity study cases (Phase 6).

Still to do for Step 0.4: list the built-in tutorials (**Help → Tutorial…**).

## PSCAD

Not installed on this PC. PowerFactory's EMT module can cover the Phase 7 EMT demo; install PSCAD (with its Fortran compiler) before Phase 7 if you also want it on your CV.

## MATLAB

Not installed on this PC (optional in this course).
