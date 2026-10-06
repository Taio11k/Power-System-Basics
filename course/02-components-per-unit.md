# Phase 2: Components and the Per-Unit System (weeks 5–7, about 34 h)

**Phase outcome:** you can model transformers, lines/cables, sources and loads; convert a whole network to per-unit; and build the **same small network in pandapower and PowerFactory with matching results**.

---

## Step 2.1: Transformers (week 5, about 8 h)

**🎯 Objective:** read a transformer nameplate (S_r, U_r, u_k %, vector group) and turn it into an equivalent-circuit impedance.

**📖 Learn**
1. [VONMEIER] Ch. 8 *Transformers*.
2. [GLOVER] Ch. 3 *Power Transformers*: ideal transformer, equivalent circuit of practical transformers, three-phase connections and phase shift. Redo the examples.

**Key ideas**
- Short-circuit voltage **u_k** (%) = the impedance in percent on the transformer's own rating. **Z (Ω, referred to a side) = (u_k/100) · U_r² / S_r**.
- **u_kr** (resistive part) comes from the copper losses. X = √(Z² − R²).
- **Vector group** (e.g. Dyn11): Δ primary, earthed-star secondary, 30° phase shift. Phase 4 explains why this matters for earth faults.

**🛠️ Do**
1. `phase2/transformer.ipynb`: write `trafo_impedance(S_MVA, U_kV, uk_pct, ukr_pct)` returning R and X in Ω.
2. **Check:** 630 kVA, 20/0.4 kV, u_k = 4 % → Z on the LV side ≈ **0.0102 Ω**.
3. **Check (preview of Phase 4):** with an infinitely strong grid, the 3-phase fault current at the LV terminals ≈ S_r / (√3 · U_r · u_k) ≈ **22.7 kA**. Real IEC 60909 results differ slightly because of the voltage factor *c* and the grid impedance.
4. In pandapower, print the data of the transformer type you used in Phase 0:
   ```python
   import pandapower as pp
   net = pp.create_empty_network()
   print(pp.load_std_type(net, "0.4 MVA 20/0.4 kV", element="trafo"))
   ```
   Identify each field (`vk_percent`, `vkr_percent`, `pfe_kw`, `i0_percent`, `shift_degree`, `vector_group`) and write what it means in `GLOSSARY.md`.

**✅ Done when**
- [ ] Both checks pass.
- [ ] You can explain the meaning of u_k, why a larger u_k gives a lower fault current, and what Dyn11 means.

---

## Step 2.2: The per-unit system (week 5–6, about 8 h)

**🎯 Objective:** handle per-unit (p.u.) values fluently. Every power system tool and textbook uses them.

**📖 Learn**
1. [GLOVER] Ch. 3 section *The Per-Unit System*. Redo **every** example by hand.
2. [SAADAT] Ch. 3 (per-unit part) or [NPTEL] week 1–2 per-unit lectures.

**Key ideas**
- Choose S_base (system-wide, e.g. 100 MVA) and U_base (per voltage zone, set by transformer ratios).
- **Z_base = U_base² / S_base**, **I_base = S_base / (√3 · U_base)**.
- **Change of base:** Z_new = Z_old · (U_old / U_new)² · (S_new / S_old).

**🛠️ Do**
1. `pslib/perunit.py`: functions `z_base`, `i_base`, `to_pu`, `from_pu`, `change_base`.
2. **Check:** S_base = 100 MVA, U_base = 20 kV → Z_base = **4 Ω**, I_base ≈ **2.887 kA**.
3. **Check:** the 630 kVA transformer (u_k = 4 %) on a 100 MVA base → **≈ 6.35 p.u.**
4. Take a 3-zone example from [GLOVER] Ch. 3 (generator → transformer → line → transformer → load) and solve it **twice**: once in ohms, once in per-unit. Both give the same load current in amperes.

**✅ Done when**
- [ ] All checks pass and the 3-zone example matches in both methods.

**⚠️ Traps:** using one U_base for all zones (each transformer changes it), and forgetting the √3 in I_base.

---

## Step 2.3: Lines and cables (week 6, about 8 h)

**🎯 Objective:** model a line or cable with R, X and B, choose the right model, and estimate voltage drop.

**📖 Learn**
1. [VONMEIER] Ch. 9 *Analyzing Transmission Lines*.
2. [GLOVER] Ch. 4 (skim the derivations; just learn what drives R, L and C) and **Ch. 5 *Transmission Lines: Steady-State Operation*** (read closely: short/medium-line π-model, ABCD parameters, voltage regulation, loadability).

**Key ideas**
- π-model: series Z = (R + jX)·length, half of the shunt admittance at each end.
- Cables have **much larger capacitance** than overhead lines.
- **Thermal limit:** the maximum current (A) a conductor can carry. This is what "line loading %" means.
- **Approximate voltage drop:** ΔU ≈ (P·R + Q·X) / U (three-phase P and Q, line-to-line U).

**🛠️ Do**
1. **Hand estimate:** a 20 kV line, 5 km, R' = 0.3 Ω/km, X' = 0.35 Ω/km, feeding 3 MW + 1 Mvar. ΔU ≈ (3·1.5 + 1·1.75) MW·Ω / 20 kV ≈ **312 V ≈ 1.56 %**.
2. **pandapower:** build ext_grid (vm_pu = 1.0) → line created with `pp.create_line_from_parameters(...)` using the values above (pick a small `c_nf_per_km`, e.g. 10, and `max_i_ka=0.4`) → load. Run `pp.runpp`. Compare the end voltage with your estimate (it should be close but not identical, and you should be able to say why).
3. List all line types with `pp.available_std_types(net, element="line")`. Print the parameters of `"NAYY 4x50 SE"` (cable) and an overhead-line type such as `"149-AL1/24-ST1A 20.0"` with `pp.load_std_type(..., element="line")`. If a name is not in the list (versions differ), pick another cable and overhead-line type of similar size. Compare c_nf_per_km between them.
4. Increase the load until line loading exceeds 100 %. Note the voltage at that point.

**✅ Done when**
- [ ] The hand estimate and pandapower agree within a few tenths of a percent, and you can explain the difference.
- [ ] You can say which limit (voltage or thermal) is hit first for your example, and why that changes for long versus short lines.

---

## Step 2.4: Sources and loads (week 7, about 4 h)

**🎯 Objective:** know how grids, generators and loads are represented in studies.

**📖 Learn**
- [VONMEIER] Ch. 6 *Loads*, Ch. 10 *Machines* (synchronous generator sections), Ch. 11 *Matching Generation and Load*.

**Key ideas to note in `GLOSSARY.md`**
- **External grid / slack**: the "infinite" upstream network. It is described in studies by its **short-circuit power S_k''** and R/X ratio, which matter in Phase 4.
- **Synchronous generator**: controls P (via its prime mover) and voltage (via excitation), so it is a **PV bus**.
- **Load models**: constant power (PQ), constant impedance (Z), constant current (I), and "ZIP" mixes.
- **Inverter-based resources** (PV, battery, wind): in load flow usually "static generators" with set P and Q.

**✅ Done when**
- [ ] You can explain the difference between pandapower `ext_grid`, `gen` and `sgen` elements, and name their PowerFactory equivalents (`ElmXnet`, `ElmSym`, `ElmGenstat`).

---

## Step 2.5: Mini-project A, first cross-validation (week 7, about 6 h) ⭐

**🎯 Objective:** build the **same** network in PowerFactory and pandapower and get the **same answer**. This is the core skill of the whole course.

**🛠️ Do**
1. Use the Phase 0 network (20 kV grid → 0.4 MVA transformer → 100 m NAYY cable → 100 kW + 50 kvar load).
2. Get the exact transformer and cable data from pandapower (`load_std_type`, Steps 2.1/2.3).
3. **PowerFactory:** first do the built-in load flow tutorial (Help → Tutorial). Then create a new project:
   - External grid (`ElmXnet`): 20 kV bus, voltage setpoint 1.02 p.u.
   - Two-winding transformer type (`TypTr2`): rated power, voltages, short-circuit voltage, copper losses, no-load losses, no-load current, and vector group, copied from the pandapower data.
   - Cable type (`TypLne`): R', X', C' (or B'), rated current, copied from the pandapower data. Length 0.1 km.
   - Load (`ElmLod`): 0.1 MW, 0.05 Mvar.
   - Run load flow (`ComLdf`).
4. Fill a comparison table in `phase2/mini_project_A.md`:

   | Quantity | Hand estimate | pandapower | PowerFactory | Diff PF vs pp |
   |---|---|---|---|---|
   | U at LV bus (p.u.) | | | | |
   | U at load bus (p.u.) | | | | |
   | Trafo loading (%) | | | | |
   | Cable loading (%) | | | | |
   | Losses (kW) | | | | |

5. If the results differ by more than about 0.1 % in voltage, hunt for the cause: tap position, transformer model, load voltage dependency, or the external grid setpoint. **Write down what you found.** This kind of debugging write-up is strong interview material.

**📦 Output:** `phase2/mini_project_A.md` with the table, screenshots of both models, and a "lessons learned" paragraph.

**✅ Done when**
- [ ] PF and pandapower voltages agree to about 3 decimal places in p.u., or you have documented why they don't.

**⚠️ Traps:** PowerFactory's load may be voltage-dependent by default (check the load flow settings and load type); transformer tap not at neutral; entering B in µS when the field expects nF, or the reverse.

---

## 🏁 Phase 2 checkpoint
Without notes: (1) convert 0.05 p.u. on a 25 MVA, 150/20 kV base to ohms on the 20 kV side; (2) explain why the voltage at a lightly loaded long cable's end can be **higher** than at its source (hint: capacitance → Ferranti effect, see [GLOVER] Ch. 5); (3) explain what u_k = 6 % tells you.
