# Phase 1: AC and Three-Phase Fundamentals (weeks 2–4, about 32 h)

**Phase outcome:** you can solve any balanced AC circuit with phasors, compute P/Q/S and power factor, and convert between line and phase quantities in three-phase systems, by hand and in Python.

**Main reading:** [GLOVER] Ch. 2 *Fundamentals* · [VONMEIER] Ch. 3 *AC Power* and Ch. 4 *Three-Phase Power* · [MIT] notes Ch. 1–3.

---

## Step 1.1: Phasors and impedance (week 2, about 10 h)

**🎯 Objective:** turn sinusoids into complex numbers (phasors) and solve RL/RC circuits with them.

**📖 Learn**
1. [VONMEIER] Ch. 3, first sections, for the intuition.
2. [GLOVER] Ch. 2, sections on *Phasors* and *Network Equations*. Redo every worked example by hand.
3. Optional: [MIT] Ch. 1 *Review of network theory*.

**Key ideas to master**
- v(t) = √2·V·cos(ωt + θ) ↔ phasor **V = V∠θ** (V is RMS).
- Impedances: Z_R = R, Z_L = jωL, Z_C = 1/(jωC); ω = 2π·50 rad/s.
- Ohm's law with complex numbers: **I = V / Z**.

**🛠️ Do**
1. Create `phase1/phasors.ipynb`.
2. Use Python's built-in complex numbers (`1j`) and `cmath`. Solve this circuit:
   - Source 230 V RMS, 50 Hz; series R = 10 Ω and L = 31.83 mH.
   - Compute X_L, Z, then I (magnitude and angle).
3. **Check your answer:** X_L ≈ 10.0 Ω, Z ≈ 14.14∠45° Ω, **I ≈ 16.26 A ∠−45°**.
4. Plot v(t) and i(t) for 2 cycles with matplotlib and confirm that the current **lags** by 45° (2.5 ms at 50 Hz).
5. Repeat with a capacitor in place of the inductor (choose C so that X_C = 10 Ω) and confirm that the current **leads**.

**📦 Output:** `phase1/phasors.ipynb` with the hand calculation (photo or Markdown) next to the Python result.

**✅ Done when**
- [ ] Python and the hand calculation agree to 3 significant figures.
- [ ] You can explain lag versus lead without notes.

**⚠️ Traps:** mixing peak and RMS values (power engineers use **RMS**); degrees versus radians in `cmath` (it uses radians).

---

## Step 1.2: Complex power, P, Q and power factor (week 3, about 10 h)

**🎯 Objective:** compute and explain real, reactive and apparent power. This topic comes up in every interview.

**📖 Learn**
1. [VONMEIER] Ch. 3 (rest of the chapter): what reactive power *physically* is.
2. [GLOVER] Ch. 2 sections *Instantaneous Power in Single-Phase AC Circuits* and *Complex Power*. Redo the examples.

**Key ideas**
- **S = V · I\*** (the conjugate of the current!) = P + jQ
- |S| in VA, P in W, Q in var; pf = cos φ = P/|S|
- Inductive loads absorb Q (lagging pf); capacitors supply Q.

**🛠️ Do**
1. In `phase1/power.ipynb`, write a function `complex_power(V, I)` that returns P, Q, S and pf.
2. Apply it to the circuit from Step 1.1. **Check:** P ≈ 2645 W, Q ≈ 2645 var, |S| ≈ 3740 VA, pf ≈ 0.707 lagging. Also verify that P = I²R.
3. **Power-factor correction exercise:** a 100 kW load runs at pf 0.8 lagging. What capacitor rating (kvar) raises it to pf 0.95?
   - Method: Q₁ = P·tan(arccos 0.8); Q₂ = P·tan(arccos 0.95); Q_C = Q₁ − Q₂.
   - **Check:** Q_C ≈ **42.1 kvar**.
4. Write a short Markdown paragraph explaining why utilities charge or penalise low power factor (current, losses, and equipment sizing).

**📦 Output:** `phase1/power.ipynb`.

**✅ Done when**
- [ ] Both numeric checks pass.
- [ ] You can answer: "Why do we care about reactive power if it does no work?"

**⚠️ Traps:** using V·I instead of V·I\*, which flips the sign of Q.

---

## Step 1.3: Balanced three-phase systems (week 4, about 10 h)

**🎯 Objective:** analyse balanced three-phase systems with per-phase (single-line) equivalents.

**📖 Learn**
1. [VONMEIER] Ch. 4 *Three-Phase Power*.
2. [GLOVER] Ch. 2 sections *Balanced Three-Phase Circuits*, *Power in Balanced Three-Phase Circuits*, and *Advantages of Balanced Three-Phase versus Single-Phase Systems*.
3. [MIT] Ch. 3 *Polyphase networks*.

**Key ideas**
- Wye (Y): V_LL = √3 · V_LN, and V_LL leads V_LN by 30°. Delta (Δ): I_line = √3 · I_phase.
- Three-phase power: **S₃φ = √3 · V_LL · I_L**.
- Δ→Y impedance conversion for a balanced load: Z_Y = Z_Δ / 3.
- In a balanced system the neutral current is zero, so you can solve **one phase** and multiply.

**🛠️ Do**
1. In `phase1/three_phase.ipynb`, plot the three phase voltages of a 230/400 V system for one cycle. Plot their sum and show it is zero.
2. **Check:** 400 V line-to-line → 230.9 V line-to-neutral.
3. **Check:** a 100 kVA three-phase load at 400 V draws **I ≈ 144.3 A** per line.
4. Solve one balanced Y load and one balanced Δ load from [GLOVER] Ch. 2 examples using the per-phase method in Python.
5. Write a function `line_current(S_kVA, V_LL_kV)` that you will reuse in every later phase.

**📦 Output:** `phase1/three_phase.ipynb` and a `pslib/basics.py` module holding your reusable functions (`complex_power`, `line_current`, …).

**✅ Done when**
- [ ] All checks pass.
- [ ] You can draw the per-phase equivalent of a Y–Y system from memory.

**⚠️ Traps:** forgetting the √3 factor, and mixing line and phase quantities. Write units next to every number.

---

## 🏁 Phase 1 checkpoint (2 h)

Answer these in `phase1/checkpoint.md` **without notes**, then check them against the books:
1. What is the RMS value of a 325 V peak sinusoid?
2. A motor draws 20 kW at pf 0.85 lagging from 400 V three-phase. What are the line current, Q and S?
3. Why does a capacitor bank raise the voltage at the end of a feeder? (A qualitative answer is fine; you will quantify it in Phase 2.)
4. Why is three-phase used rather than single-phase for transmission?

**Exit criteria:** all 4 answered, and `pslib/basics.py` is committed to GitHub.
