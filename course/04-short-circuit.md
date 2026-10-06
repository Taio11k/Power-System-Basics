# Phase 4: Faults and IEC 60909 Short-Circuit Calculation (weeks 11–13, about 34 h) → Portfolio Project P2

**Phase outcome:** you can calculate symmetrical and unsymmetrical fault currents by hand with symmetrical components, run IEC 60909 studies in PowerFactory and pandapower, and check equipment ratings against the results.

**Main reading:** [GLOVER] Ch. 8 *Symmetrical Faults*, Ch. 9 *Symmetrical Components*, Ch. 10 *Unsymmetrical Faults* · [MIT] Ch. 4 · [NPTEL] weeks 9–11 · [PP-SC] · [IEC60909].

**Test system from now on:** the **CIGRE MV benchmark network** ([CIGRE-575], [PP-CIGRE]): a 110/20 kV substation with 2 transformers, 15 buses, 15 lines, 8 switches, and versions with PV, wind, batteries and CHP. You will use it in Phases 4, 5, 6 and the capstone.

---

## Step 4.1: Symmetrical (three-phase) faults (week 11, about 8 h)

**🎯 Objective:** calculate three-phase fault currents with Thévenin equivalents.

**📖 Learn**
- [GLOVER] Ch. 8. Focus on: the series R-L circuit transient (DC offset), the synchronous machine reactances X''_d, X'_d, X_d, and fault calculation with the bus impedance matrix Z_bus.

**Key ideas**
- At the fault location: **I_k = U_prefault / Z_Th** (Thévenin).
- The fault current has an AC part that decays from the **subtransient** to the transient to the steady-state value, plus a decaying **DC offset**. That is why IEC 60909 defines several currents:
  - **I_k''**: initial symmetrical short-circuit current (RMS)
  - **i_p**: peak short-circuit current, the first peak including DC offset, used for **making** capacity and mechanical forces
  - **I_th**: thermal equivalent current, used for cable and equipment heating
- **Fault level:** S_k'' = √3 · U_n · I_k'' (MVA).

**🛠️ Do**
1. In `phase4/sym_fault.ipynb`, compute I_k'' at the LV side of a 630 kVA, 20/0.4 kV, u_k = 4 % transformer fed from a 20 kV grid with S_k'' = 250 MVA:
   - Z_grid (referred to 0.4 kV) = U²/S_k'' ; Z_trafo from Step 2.1.
   - I_k'' = U_n / (√3 · |Z_grid + Z_trafo|) (ignore the voltage factor *c* for now).
   - Compare with the "infinite grid" answer from Step 2.1 (≈ 22.7 kA). The finite grid gives **less** current; explain why.
2. Redo one Z_bus fault example from [GLOVER] Ch. 8 in Python.

**✅ Done when**
- [ ] You can explain I_k'', i_p and I_th, and which equipment rating each one is checked against.

---

## Step 4.2: Symmetrical components (week 11–12, about 8 h)

**🎯 Objective:** decompose unbalanced phasors into positive, negative and zero sequences.

**📖 Learn**
- [GLOVER] Ch. 9 (all of it) · [MIT] Ch. 4 *Introduction to symmetrical components*.

**Key ideas**
- a = 1∠120°. **[V_a, V_b, V_c]ᵀ = A · [V_0, V_1, V_2]ᵀ**, where A = [[1,1,1],[1,a²,a],[1,a,a²]].
- Each element has **sequence impedances** Z_1, Z_2, Z_0. Z_0 depends strongly on earthing and on the transformer vector group (e.g. **a Dyn transformer blocks zero-sequence current between its sides**).

**🛠️ Do**
1. `pslib/symcomp.py`: functions `abc_to_012` and `012_to_abc`. Test that a balanced set gives only V_1 ≠ 0.
2. Take an unbalanced example from [GLOVER] Ch. 9 and reproduce its sequence components.
3. Draw (by hand) the zero-sequence network for Y-grounded/Δ and Dyn transformers, as in [GLOVER] Ch. 9.

**✅ Done when**
- [ ] Your functions reproduce the textbook examples.
- [ ] You can explain why an earth fault on the LV side of a Dyn11 transformer is not "seen" as zero-sequence current on the MV side.

---

## Step 4.3: Unsymmetrical faults (week 12, about 6 h)

**📖 Learn**
- [GLOVER] Ch. 10: single line-to-ground (SLG), line-to-line (LL), double line-to-ground (DLG).

**Key formulas (bolted fault, Z_f = 0)**
- **SLG:** I_a = 3·V_f / (Z_1 + Z_2 + Z_0)
- **LL:** I_b = −I_c = −j·√3·V_f / (Z_1 + Z_2)
- **DLG:** see [GLOVER] Ch. 10 (Z_2 and Z_0 in parallel)

**🛠️ Do**
1. Code all three fault types in `pslib/faults.py`. Reproduce [GLOVER] Ch. 10 examples.
2. Show that SLG current can be **higher** than three-phase current when Z_0 < Z_1, and explain when that happens (solidly earthed networks, close to Yn-connected transformers).

---

## Step 4.4: IEC 60909 in practice (week 13, about 8 h)

**🎯 Objective:** run standard-compliant short-circuit studies like a consultant.

**📖 Learn**
- [PP-SC] *Running a Short-Circuit Calculation* and *Short-Circuit Currents* pages, plus the tutorials in the `shortcircuit/` folder of [PP-TUT].
- PowerFactory User Manual: short-circuit chapter (method "IEC 60909").
- Optional: the short-circuit section of [EIG] for an LV view.

**Key IEC 60909 concepts** (write each in your own words in `GLOSSARY.md`)
- **Equivalent voltage source** at the fault location: c·U_n/√3. Loads and line capacitances are neglected.
- **Voltage factor c**: c_max for maximum currents (equipment rating), c_min for minimum currents (protection sensitivity). **Look up the exact c values in [IEC60909] Table 1** (or your PowerFactory/pandapower docs) and record them with their source. Do not guess them.
- **Max vs min case:** different source strengths, different c factors, and different conductor temperatures.
- **Correction factors** for generators and power-station units (K_G, K_S), and the 2016 edition's treatment of **full-converter units** (PV, batteries, type-4 wind).

**🛠️ Do**
1. **pandapower on CIGRE MV:**
   ```python
   import pandapower.networks as pn
   import pandapower.shortcircuit as sc

   net = pn.create_cigre_network_mv(with_der=False)
   print(net.ext_grid.T)         # check s_sc_max_mva, rx_max etc.; set them if missing
   sc.calc_sc(net, case="max", fault="3ph")
   print(net.res_bus_sc)
   ```
   Then run `case="min"`. Read the docs to find which extra parameters the min case and single-phase (`fault="1ph"`) calculations need, such as zero-sequence data. Add them if they are missing and **record every value you assumed**.
2. **Export the network data** to build it in PowerFactory: `pp.to_excel(net, "cigre_mv.xlsx")`. Open the Excel file; every bus, line, transformer and load is listed there.
3. **PowerFactory:** build the CIGRE MV network (15 buses; check it fits your node limit). Use the same source S_k'' and R/X. Run the short-circuit command (IEC 60909) for max and min, 3-phase and 1-phase, at all buses.
4. **Compare** I_k'' and i_p at every bus between pandapower and PowerFactory in one table. Explain differences above about 1 %.
5. **Equipment check:** assume the 20 kV switchgear is rated at, for example, 16 kA (I_k) and 40 kA (peak). State this clearly as an **assumption**. Is every bus within the rating? What margin?
6. **DER effect:** repeat with `with_der="pv_wind"`. How much does I_k'' rise at each bus? Why is the contribution of inverter-based generation small compared with synchronous machines?

**⚠️ Traps:** comparing a max case in one tool with a min case in the other; transformer tap positions; motor and generator contributions being on in one tool and off in the other; a 1-phase fault calculation without proper zero-sequence data.

---

## ⭐ Portfolio Project P2: IEC 60909 Short-Circuit Study of the CIGRE MV Network

**Folder:** `P2-short-circuit-iec60909/`. Same structure and report template as P1.

**Report must include**
1. Scope: the maximum fault levels for equipment rating, and the minimum fault levels for protection (you will reuse them in Phase 5).
2. Network and source data, with assumptions (source S_k'', R/X, zero-sequence data).
3. Method: IEC 60909-0:2016, max and min cases, fault types 3ph, 2ph, 1ph.
4. Results: a bus-by-bus table of I_k''(max), i_p, I_k''(min), and a colour-coded SLD of fault levels.
5. Equipment adequacy check against the assumed ratings.
6. The effect of DER on fault levels.
7. Validation: pandapower vs PowerFactory, plus one hand calculation at the 20 kV busbar.
8. Conclusions.

**✅ P2 is done when**
- [ ] Every number is reproducible by script.
- [ ] One bus is also hand-calculated and matches.
- [ ] A reader can see at a glance whether the switchgear is adequate.
