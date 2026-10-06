# Phase 5: Protection Basics (weeks 14–16, about 32 h) → Portfolio Project P3

**Phase outcome:** you understand protection philosophy, can set and grade IEC IDMT overcurrent relays on a radial feeder, and can present a time-current coordination study.

**Main reading:** [GLOVER] Ch. 11 *System Protection* · [GERS] (chapters on overcurrent protection, CTs, coordination, and distributed generation) · [IEC60255] · [PP-PROT].

---

## Step 5.1: Protection philosophy and hardware (week 14, about 8 h)

**🎯 Objective:** know what protection must achieve and the main devices involved.

**📖 Learn**
- [GLOVER] Ch. 11 introduction, instrument transformers (CTs and VTs), overcurrent relays, and zones of protection.
- [GERS]: the introductory chapters and the current transformer chapter.

**Key ideas for `GLOSSARY.md`**
- The four goals: **selectivity** (only the nearest device trips), **sensitivity** (detects the minimum fault), **speed**, **reliability** (dependability and security).
- **Primary vs backup** protection; **zones** of protection.
- **CT ratio and saturation**; the relay sees **secondary** amps.
- Device types: fuse, circuit breaker plus relay, recloser; overcurrent (ANSI 50/51), earth-fault (50N/51N), differential (87), distance (21). For now, focus on 50/51.

**✅ Done when**
- [ ] You can explain why the relay closest to the fault must trip first, and what happens if it fails.

---

## Step 5.2: IDMT curves and your own TCC tool (week 14–15, about 8 h)

**🎯 Objective:** compute relay operating times and plot time-current characteristics (TCC).

**IEC inverse-time formula ([IEC60255]):**

&nbsp;&nbsp;&nbsp;&nbsp;**t = TMS · k / ((I / I_s)^α − 1)**

| Curve | k | α |
|---|---|---|
| Standard inverse (SI) | 0.14 | 0.02 |
| Very inverse (VI) | 13.5 | 1 |
| Extremely inverse (EI) | 80 | 2 |
| Long-time inverse (LTI) | 120 | 1 |

(Check these constants against the standard, [GERS], or a relay manual, and cite the source in your project.)

**🛠️ Do**
1. `pslib/protection.py`: function `idmt_time(I, Is, TMS, curve="SI")` plus a definite-time element (instantaneous 50 stage: trips at time t_inst when I > I_inst).
2. **Check:** SI curve, I_s = 400 A, TMS = 0.1, I = 4000 A (10 × I_s) → **t ≈ 0.297 s**.
3. Write `plot_tcc(relays)` that draws all relay curves on **log-log axes** (current on x, time on y), with vertical lines marking the fault currents.

**✅ Done when**
- [ ] The check passes and your plot looks like the TCC figures in [GERS]/[GLOVER].

---

## Step 5.3: Coordinate a radial feeder (week 15–16, about 10 h) ⭐

**🎯 Objective:** set three relays in series so that they are selective for every fault on the feeder.

**📖 Learn**
- [GERS], coordination of overcurrent relays: grading (time) margin, setting the pickup current, and using instantaneous elements.

**The procedure to follow (from downstream to upstream)**
1. **Choose the feeder.** In the CIGRE MV network (with the network's normally-open switches left open), choose one radial feeder. Place **R3** near the feeder end, **R2** mid-feeder, and **R1** at the feeder head in the substation.
2. **Collect data** (from Phases 3 and 4):
   - maximum load current through each relay (load flow),
   - **maximum** 3-phase fault current at each relay location and at the next downstream relay (P2 max case),
   - **minimum** fault current at the end of each relay's protected zone (P2 min case, 2-phase or 1-phase as appropriate).
3. **Pickup I_s:** above the maximum load current (with a margin; find the recommended factor in [GERS] and cite it) and below the minimum fault current at the end of the zone, including the backup zone.
4. **CT ratio:** choose a standard ratio so that the relay settings fall inside the relay's range.
5. **TMS of R3:** the lowest value, because nothing is downstream of it.
6. **Grade R2 above R3:** at the **maximum fault current seen by both** (the fault just downstream of R3), require t_R2 − t_R3 ≥ the grading margin. Typical margins are a few tenths of a second; take the exact value from [GERS] and explain what it is made of (breaker time, overshoot, errors, safety margin). Solve for TMS_R2.
7. **Grade R1 above R2** the same way.
8. **Instantaneous elements (optional):** set them so they do not reach past the next relay (look up the overreach rules in [GERS]).
9. **Verify:** plot all three curves plus the fault-current lines. For a fault at **each** bus, list which relay trips first and when.

**🛠️ Do the verification in two tools**
- **Python:** your own `pslib/protection.py` plus a script that reads the fault currents from `net.res_bus_sc` (pandapower).
- **And one of:**
  - **PowerFactory protection** (if licensed): add relay models from the library at the three locations, enter the settings, and use the **time-overcurrent plot** and short-circuit sweep to verify.
  - **pandapower protection** (fallback): follow `tutorials/protection/oc_relay.ipynb` **for your installed pandapower version** (the protection API has changed between versions) and reproduce your trip times.

**⚠️ Traps:** grading at the wrong current (always grade at the **maximum** current that flows through both relays); forgetting that the minimum fault current must still exceed the pickup; mixing primary and secondary amps.

---

## Step 5.4: How DER affects protection (week 16, about 2 h, reading only)

**📖 Learn**
- [GERS], the chapter on distributed generation. [BOLLEN], the chapter on protection.

**Note in `GLOSSARY.md`:** protection **blinding** (DER reduces the current seen by the feeder relay), **sympathetic tripping** (a healthy feeder trips because its DER feeds a fault on the neighbouring feeder), and **islanding / anti-islanding**. You will check these in the capstone.

---

## ⭐ Portfolio Project P3: Overcurrent Protection Coordination Study

**Folder:** `P3-overcurrent-coordination/`

**Report must include**
1. Scope and the feeder SLD with relay and CT locations.
2. Input data: load currents, max/min fault currents (link to P2).
3. Setting criteria with cited sources (pickup factor, grading margin).
4. A **settings table**: relay, CT ratio, curve, I_s (primary and secondary), TMS, instantaneous setting.
5. A **TCC plot** with all relays and fault-current markers.
6. A **discrimination table**: fault location → first relay to trip → time → backup relay → time → margin achieved.
7. Validation: Python vs PowerFactory (or pandapower protection).
8. Conclusions, including one paragraph on how adding DER to this feeder could affect the settings.

**✅ P3 is done when**
- [ ] Every fault location has a positive grading margin of at least your chosen value.
- [ ] The TCC plot is clean enough to put in a CV.
