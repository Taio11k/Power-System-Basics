# Phase 3: Power Flow (Load Flow) (weeks 8–10, about 36 h) → Portfolio Project P1

**Phase outcome:** you understand what a load flow solver does inside (you write one yourself), you can run professional load flow and N-1 contingency studies in PowerFactory and pandapower, and you have published **P1**.

**Main reading:** [GLOVER] Ch. 6 *Power Flows* · [VONMEIER] Ch. 12 *Power Flow* and Ch. 13 *Limits* · [SAADAT] power flow chapter · [NPTEL] weeks 5–6 · [MIT] Ch. 5.

**Test system for this phase:** the **9-bus, 3-generator system** (WSCC system from [ANDERSON]; MATPOWER `case9`; pandapower `pn.case9()`). You will reuse it in Phase 7, so build it carefully.

> Note: pandapower's `case9` is converted from MATPOWER's `case9`. Bus numbering and some values can differ from the Anderson & Fouad drawing. Always match elements **by their data**, not by bus numbers.

---

## Step 3.1: Bus types and the admittance matrix Y_bus (week 8, about 8 h)

**🎯 Objective:** formulate the power flow problem and build Y_bus by hand.

**📖 Learn**
- [GLOVER] Ch. 6, first sections: the power flow problem, bus types, building Y_bus. Redo the examples.

**Key ideas**
| Bus type | Known | Unknown | Example |
|---|---|---|---|
| Slack (reference) | \|V\|, θ = 0 | P, Q | external grid / largest plant |
| PV | P, \|V\| | Q, θ | generator with voltage control |
| PQ | P, Q | \|V\|, θ | load bus |

- Y_bus: diagonal Y_ii = sum of admittances connected to bus i (including line charging B/2); off-diagonal Y_ij = −(series admittance between i and j).
- Power flow equations: S_i = V_i · (Σ_j Y_ij V_j)\*. They are **nonlinear**, so we need an iterative solver.

**🛠️ Do**
1. Build Y_bus **by hand** for a 3-bus example in [GLOVER] Ch. 6.
2. Write `pslib/ybus.py` with a function `build_ybus(bus_count, branches)`. Each branch is (from, to, r, x, b) in p.u. Reproduce the hand result.
3. Download MATPOWER `case9.m` (it comes with MATPOWER). Read its `bus`, `gen` and `branch` tables, build the case9 Y_bus with your function, and print it.

**✅ Done when**
- [ ] Your function reproduces the textbook Y_bus.
- [ ] You can explain why Y_bus is sparse and symmetric (when there are no phase-shifting transformers).

---

## Step 3.2: Write your own Newton-Raphson solver (week 8–9, about 10 h) ⭐

**🎯 Objective:** understand load flow from the inside. This is a strong interview talking point and a strong GitHub item.

**📖 Learn**
- [GLOVER] Ch. 6 sections on Gauss-Seidel and Newton-Raphson power flow. [SAADAT] has the same algorithms with MATLAB code. Read it to understand the method, **don't copy it**.

**🛠️ Do: follow these steps in `pslib/newton_raphson.py`**
1. Inputs: Y_bus, bus types, P and Q specs (p.u.), V setpoints for PV and slack buses.
2. Start with a **flat start**: all |V| = 1.0 (or the setpoint), all θ = 0.
3. Loop:
   1. Compute the calculated injections P_calc and Q_calc from V and Y_bus.
   2. Mismatch: ΔP for all non-slack buses; ΔQ for PQ buses only.
   3. If max |mismatch| < 1e-8 p.u., stop.
   4. Build the Jacobian (∂P/∂θ, ∂P/∂|V|, ∂Q/∂θ, ∂Q/∂|V|). Simplest correct method first: **numerical differentiation**. Upgrade later to analytical formulas from the textbook.
   5. Solve J·Δx = mismatch with `numpy.linalg.solve`; update θ and |V|.
4. Print the iteration count and the mismatch per iteration. NR should converge in about 3–6 iterations.
5. **Validate three ways** on case9:
   - your solver,
   - MATPOWER in MATLAB: `results = runpf('case9')`,
   - pandapower: `net = pn.case9(); pp.runpp(net)`.
   Put all three voltage magnitudes and angles in one table.
6. Add a simple test file `tests/test_nr.py` that asserts your voltages match the MATPOWER values within 1e-4 p.u.

**📦 Output:** `pslib/newton_raphson.py`, `tests/test_nr.py`, and a comparison table in `phase3/nr_validation.md`.

**✅ Done when**
- [ ] All three tools agree to about 4 decimals in |V| and about 0.01° in θ.
- [ ] You can explain why NR converges quadratically and what happens to the Jacobian near voltage collapse (it becomes singular).

**⚠️ Traps:** degrees versus radians; mixing MW and p.u. (divide by baseMVA = 100); forgetting the line charging (b) in Y_bus; MATPOWER's bus numbers start at 1 but Python indexes start at 0.

---

## Step 3.3: Operating limits and controls (week 9, about 4 h)

**🎯 Objective:** know what "a problem" means in a load flow result, and the usual fixes.

**📖 Learn**
- [VONMEIER] Ch. 13 *Limits*. [GLOVER] Ch. 6 sections on control of power flow (generator voltage, tap-changing transformers, shunt capacitors).

**Key ideas**
- **Voltage limits:** set by the grid code or planning criteria of each utility. For LV/MV public supply, [EN50160] requires the supply voltage to stay within ±10 % for 95 % of the 10-minute averages. Transmission planning criteria are usually tighter. In your studies, **state the criteria you assume** and cite the source.
- **Thermal limits:** line or transformer loading ≤ 100 % of the rating.
- **Generator reactive limits** (Q_min/Q_max): when a PV bus reaches a limit, it becomes a PQ bus.
- **Voltage control tools:** generator AVR setpoints, transformer taps (OLTC), shunt capacitors and reactors.

**🛠️ Do**
1. In pandapower case9, scale all loads up in 10 % steps (`net.load.p_mw *= 1.1`) until a voltage or loading limit is violated. Record which limit fails first.
2. Fix it with **one** measure (e.g. add a shunt capacitor with `pp.create_shunt`, or raise a generator voltage setpoint). Show the before and after.

**✅ Done when**
- [ ] You have a before/after table showing your mitigation works.

---

## Step 3.4: The 9-bus system in PowerFactory (week 9–10, about 6 h)

**🛠️ Do**
1. Check whether your PowerFactory **Examples** window already has a 9-bus (WSCC/IEEE) example. If it does, open it, **but still check every parameter** against [ANDERSON] or the [MathWorks IEEE 9-bus page](https://ch.mathworks.com/help/sps/ug/ieee-9-bus.html).
2. Otherwise build it yourself from the Anderson & Fouad data: 3 generators (16.5 kV, 18 kV, 13.8 kV), 3 step-up transformers to 230 kV, 6 lines, 3 loads. Use 100 MVA as the system base.
3. Run the load flow. Compare bus voltages, angles and generator outputs with your pandapower case9 results. Expect small differences if the datasets differ slightly. **Document every difference you find and its cause.**
4. Make the single-line diagram presentable: name the buses, show results boxes (U p.u., loading %), and use colour by loading. Export it as an image for the report.

**✅ Done when**
- [ ] The PowerFactory load flow converges and matches your reference within an explained tolerance.

---

## Step 3.5: N-1 contingency analysis (week 10, about 4 h)

**🎯 Objective:** run the study type that network planners run every day.

**📖 Learn**
- [PP-N1] pandapower contingency docs and the `contingency_analysis.ipynb` tutorial ([PP-TUT]).
- PowerFactory User Manual: chapter on Contingency Analysis.

**Key idea:** "N-1" means the system must still meet its criteria after losing **any one** element (line, transformer, generator).

**🛠️ Do**
1. **pandapower:**
   ```python
   import pandapower as pp
   import pandapower.networks as pn
   import pandapower.contingency as contingency

   net = pn.case9()
   nminus1_cases = {"line": {"index": net.line.index.values}}
   res = contingency.run_contingency(net, nminus1_cases)
   ```
   Check the `contingency` docs for the result keys (e.g. `max_loading_percent`, `min_vm_pu`, `max_vm_pu`).
2. **PowerFactory:** run the Contingency Analysis command for all lines (and transformers if no generator would be islanded).
3. Make a results table: outage → worst loading (element, %) → min/max voltage (bus, p.u.) → criteria violated? (Y/N).
4. For the worst contingency, propose one mitigation and re-run it.

**⚠️ Traps:** outaging a generator step-up transformer islands the generator, so the power flow may fail or give meaningless results. Handle islanding explicitly and say so in the report. Also check that line ratings (`max_i_ka`) exist; without ratings, loading % means nothing.

---

## ⭐ Portfolio Project P1: Load Flow and N-1 Contingency Study (week 10, about 4 h)

**Folder:** `power-systems-portfolio/P1-load-flow-n1/`

**Required contents**
```
P1-load-flow-n1/
├── README.md            ← 1-page summary: goal, method, key results table, 1 SLD image, conclusions
├── report/P1_report.pdf ← 5–8 page study report (structure below)
├── pandapower/          ← scripts that reproduce every number
├── powerfactory/        ← screenshots of the SLD and results (and the .pfd export if your licence allows)
├── pslib/               ← your own Y_bus and NR solver + tests
└── results/             ← CSV tables and plots
```

**Report structure (the same template is reused in every project)**
1. **Scope:** what question this study answers.
2. **Network description:** single-line diagram and data sources (cite [ANDERSON]/MATPOWER).
3. **Assumptions and criteria:** e.g. voltage 0.95–1.05 p.u. in normal state and 0.90–1.10 p.u. post-contingency, loading ≤ 100 %. **Label these as assumptions** and say where real projects would take them from (the grid code).
4. **Method:** tools and versions, solver, cross-validation approach.
5. **Results:** base case (N-0) and N-1 tables, plus the load-increase study.
6. **Issues and mitigations.**
7. **Validation:** your NR solver vs MATPOWER vs pandapower vs PowerFactory.
8. **Conclusions.**

**✅ P1 is done when**
- [ ] A stranger can clone the repo, run one script, and reproduce your tables.
- [ ] The README shows the SLD image and the key results table at the top.
- [ ] The PDF reads like a short consultancy study, not like homework.
