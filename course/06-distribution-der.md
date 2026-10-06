# Phase 6: Distribution Networks and Solar (DER) Integration (weeks 17–19, about 34 h) → Portfolio Project P4

**Phase outcome:** you can run time-series (quasi-static) studies, calculate PV hosting capacity, test voltage-control mitigations, and publish **P4**. Distribution and renewable integration studies are among the most common entry-level jobs in this field.

**Main reading:** [VONMEIER] Ch. 7 (distribution sections), Ch. 5 *Power Quality*, Ch. 14 *Power Electronics* · [GLOVER] Ch. 15 *Power Distribution* · [BOLLEN] Ch. 3 *hosting capacity approach* and the overvoltage and overloading chapters · [KERSTING] for depth · [EN50160].

---

## Step 6.1: How distribution networks behave (week 17, about 8 h)

**🎯 Objective:** understand radial MV/LV feeders and why rooftop and utility PV raise voltages.

**📖 Learn**
- [GLOVER] Ch. 15 and [VONMEIER] Ch. 7 for structure: radial vs meshed-operated-radially, normally-open points, MV/LV transformers.
- [BOLLEN]: the chapter on overvoltages caused by DG.

**Key idea: voltage rise.** For a generator exporting P and Q through a line with R and X:

&nbsp;&nbsp;&nbsp;&nbsp;**ΔU ≈ (P·R + Q·X) / U**  (Q > 0 means injecting reactive power)

So PV **raises** the voltage, especially where R/X is high (LV cables). **Absorbing** reactive power (Q < 0) reduces the rise. This is the basis of Q(U) and cos φ(P) control.

**🛠️ Do**
1. `phase6/voltage_rise.ipynb`: on the pandapower CIGRE **LV** network (`pn.create_cigre_network_lv()`), add one PV system (`pp.create_sgen`) at the end of a feeder. Increase P from 0 to the point where the voltage exceeds 1.10 p.u. (or your stated limit). Plot U vs P.
2. Repeat with the PV absorbing reactive power (e.g. Q = −0.3·P). Show how far the curve moves.
3. Check the result with the ΔU formula above.

**✅ Done when**
- [ ] You can explain why the same PV causes a larger voltage rise on LV cables than on MV overhead lines (R/X ratio).

---

## Step 6.2: Time-series simulation (week 17–18, about 8 h)

**🎯 Objective:** simulate a day or a year in 15-minute steps instead of one snapshot.

**📖 Learn**
- [PP] *Time Series Simulation* docs. [PP-TUT] notebooks `time_series.ipynb` and `time_series_multiple_loads_generators.ipynb`. Complete both.
- PowerFactory User Manual: **Quasi-Dynamic Simulation** chapter.

**🛠️ Do**
1. Build daily profiles (96 values of 15 min) for residential load and PV. Use the `cigre_timeseries_15min.json` file in the pandapower tutorials folder, or make simple synthetic shapes (a bell curve for PV, evening peaks for load) and **label them as synthetic**.
2. pandapower: `DFData` + `ConstControl` for loads and sgens, `OutputWriter` for `res_bus.vm_pu` and `res_line.loading_percent`, then `run_timeseries`.
3. Plot the voltage at the feeder end over the day for 0 %, 50 % and 100 % PV penetration (all on one plot).
4. PowerFactory: attach the same profiles as time characteristics and run the **Quasi-Dynamic Simulation** for the same day. Compare the feeder-end voltage curves.

**✅ Done when**
- [ ] You see the "duck" pattern: midday voltage rise from PV and an evening dip from load, consistent in both tools.

---

## Step 6.3: Hosting capacity (week 18, about 8 h) ⭐

**🎯 Objective:** answer the utility question "How much PV can this feeder take before something breaks?"

**📖 Learn**
- [BOLLEN] Ch. 3: hosting capacity = the amount of DG at which a performance index reaches its limit. Learn the **performance index → limit → hosting capacity** logic.
- [PP-TUT] `hosting_capacity.ipynb`: work through it completely.

**🛠️ Do**
1. **Define the criteria first** (write them in the report): e.g. max voltage ≤ 1.10 p.u. or a tighter planning value, line and transformer loading ≤ 100 %. Cite where each comes from ([EN50160], or "assumed, as typical utility planning practice").
2. **Deterministic hosting capacity:** for each candidate bus, increase PV until the first limit is violated. Record the MW and which limit failed. Make a bar chart per bus.
3. **Stochastic hosting capacity** (as in the pandapower tutorial): place PV randomly, repeat N times (e.g. 500), and plot the distribution of hosting capacity. Report the 5th percentile, the median and the 95th percentile.
4. Do it on **CIGRE MV** (and optionally CIGRE LV).

---

## Step 6.4: Mitigation, raising the hosting capacity (week 19, about 6 h)

**📖 Learn**
- [PP-TUT] `DER_control_tutorial.ipynb` and `vm_set_tap.ipynb`. [BOLLEN]: the sections on methods to increase hosting capacity.

**🛠️ Do:** test at least two mitigations and recompute the hosting capacity for each:
1. **Reactive power control** of the PV inverters: fixed cos φ, cos φ(P), or Q(U) droop.
2. **Transformer tap / OLTC setpoint** change.
3. (Optional) **Battery** absorbing PV at midday (`pp.create_storage`, with a simple time-series controller).

Make a table: mitigation → new hosting capacity → side effects (higher losses, more reactive power from the grid, more transformer loading).

---

## ⭐ Portfolio Project P4: PV Hosting Capacity Study with Time Series

**Folder:** `P4-pv-hosting-capacity/`

**Report must include**
1. Scope: "What PV capacity can the CIGRE MV network host, and how can it be raised?"
2. Network, profiles (with their source or "synthetic" label), and criteria with sources.
3. Daily time-series results at several penetration levels (plots).
4. Deterministic hosting capacity per bus (bar chart) and stochastic results (histogram).
5. Mitigation comparison table.
6. Validation: the pandapower time series vs the PowerFactory quasi-dynamic simulation for one case.
7. Conclusions and recommendations, written as if to a utility planner.

**✅ P4 is done when**
- [ ] The whole study runs from one script and finishes in a reasonable time.
- [ ] The README includes the hosting-capacity bar chart and a one-line headline result.
