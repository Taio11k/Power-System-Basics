# Phase 7: Stability and an EMT Introduction (weeks 20–22, about 34 h) → Portfolio Project P5

**Phase outcome:** you understand rotor-angle (transient) stability, can find a critical clearing time analytically, numerically and in PowerFactory RMS simulation (automated with Python), and you can explain when an **EMT** tool such as PSCAD is needed instead of RMS.

**Main reading:** [GLOVER] Ch. 12 *Power System Stability* · [SAADAT] stability chapter · [P-STAB2021] (the stability classification paper) · [KUNDUR] or [MACHOWSKI] as a reference · [NPTEL] week 12.

---

## Step 7.1: Stability classification (week 20, about 3 h)

**📖 Learn**
- [P-STAB2021] (free copy linked in REFERENCES.md). Read the introduction and the classification figure.

**Key idea:** stability is classified into **rotor angle** (small-signal, transient), **voltage**, **frequency**, and, added in 2021 for inverter-dominated grids, **converter-driven** and **resonance** stability.

**🛠️ Do:** redraw the classification tree in your own diagram for `GLOSSARY.md`.

---

## Step 7.2: Swing equation and equal-area criterion (week 20, about 9 h)

**📖 Learn**
- [GLOVER] Ch. 12: swing equation, single-machine infinite-bus (SMIB), equal-area criterion, numerical integration. [SAADAT] covers the same topics with MATLAB.

**Key equations (per-unit)**
- Swing: **(2H/ω_s) · d²δ/dt² = P_m − P_e**, with P_e = P_max · sin δ and P_max = E'·V/X.
- For a bolted 3-phase fault at the generator terminals (P_e = 0 during the fault), cleared with the post-fault network the same as the pre-fault one:
  - **cos δ_cr = (π − 2δ_0)·sin δ_0 − cos δ_0**
  - **t_cr = √(4H·(δ_cr − δ_0) / (ω_s·P_m))**

**🛠️ Do**
1. `phase7/smib.ipynb`. Data: H = 5 s, f = 50 Hz, P_m = 0.9 p.u., P_max = 1.8 p.u.
2. **Analytical check:** δ_0 = 30°, δ_cr ≈ **79.6°**, t_cr ≈ **0.247 s**.
3. **Numerical:** integrate the swing equation with `scipy.integrate.solve_ivp` (`pip install scipy`), or your own RK4 or Euler loop. Apply the fault (P_e = 0) from t = 0 until the clearing time t_c, then set P_e = P_max sin δ. Plot δ(t) for t_c = 0.20 s (stable, oscillates) and t_c = 0.30 s (unstable, δ runs away).
4. Find t_cr by **bisection** on t_c. It should match the analytical value to within about 1 ms.

**✅ Done when**
- [ ] The analytical, numerical and bisection values agree.
- [ ] You can explain the equal-area criterion with a sketch.

---

## Step 7.3: RMS simulation in PowerFactory on the 9-bus system (week 21, about 10 h) ⭐

**🎯 Objective:** run a real multi-machine transient stability study and automate it.

**📖 Learn**
- PowerFactory User Manual: RMS/EMT simulation chapter (initial conditions `ComInc`, run simulation `ComSim`, events such as short-circuit events, results and plots). Do the built-in RMS tutorial if your licence has one.
- [ANDERSON] for the 9-bus dynamic data (generator H, X'_d etc.). The [MathWorks IEEE 9-bus page](https://ch.mathworks.com/help/sps/ug/ieee-9-bus.html) describes the same 3-machine system.

**🛠️ Do**
1. Add dynamic data to your Phase 3 9-bus model (start with classical generator models, then optionally add AVR and governor).
2. Define a 3-phase fault on a line near a generator bus at t = 0.1 s, cleared by tripping the line after Δt.
3. Plot the rotor angles **relative to a reference machine** and the bus voltages, for one stable case and one unstable case.
4. **Automate the critical clearing time search with the Python API**:
   - `import powerfactory`, `app = powerfactory.GetApplication()` (or run it as a Python command object inside PowerFactory), activate the project and study case.
   - Loop: set the clearing event time → run `ComInc` + `ComSim` → read the rotor-angle results → decide stable or unstable (e.g. the max angle difference stays below a threshold you define and justify) → bisect.
   - Write the results to CSV and plot them with matplotlib.
5. Repeat for at least 3 fault locations. Make a table: fault location → CCT.

**⚠️ Traps:** absolute rotor angles drift, so always use **relative** angles; the load model (constant-impedance vs constant-power) changes the results, so state it; a too-large simulation time step.

**Fallback if RMS simulation is not in your licence:** do the same multi-machine study in Python (classical model, solving the network algebraic equations at each step, as in [SAADAT]/[GLOVER] Ch. 12) or with MATLAB/Simulink and [SAADAT]'s files. Say so honestly in the report.

---

## Step 7.4: EMT introduction with PSCAD (week 22, about 8 h)

**🎯 Objective:** see what RMS tools hide, and know when EMT is required.

**📖 Learn**
- [PSCAD]: work through the tutorial projects in order (the docs recommend first-time users do all of them).
- Why the industry cares: [AEMO] uses PSS®E for RMS but **PSCAD for EMT** connection studies. EMT is needed for inverter-based resources, weak grids, switching transients and control interactions.

**🛠️ Do (a mini-study that links back to Phase 4)**
1. In PSCAD, build: a 20 kV, 50 Hz three-phase source with impedance (choose R/X) → circuit breaker → a 3-phase fault to ground.
2. Apply the fault at different **points on the voltage wave** (e.g. at voltage zero and at voltage peak). Plot the phase currents. You will see the **DC offset** change.
3. **Compare with IEC 60909:** compute I_k'' and the peak factor **κ = 1.02 + 0.98·e^(−3R/X)**, then i_p = κ·√2·I_k''. Compare with the worst-case peak in PSCAD. Do they agree? This connects theory, standard and simulation, which makes a strong portfolio item.
4. (Optional) Energise a capacitor bank and observe the switching overvoltage and inrush current.

**✅ Done when**
- [ ] You can explain in two sentences the difference between RMS (phasor) simulation and EMT (waveform) simulation, and give one study that needs each.

---

## ⭐ Portfolio Project P5: Transient Stability (CCT) Study plus EMT Fault Demonstration

**Folder:** `P5-transient-stability/`

**Report must include**
1. SMIB validation: analytical vs numerical vs bisection CCT.
2. 9-bus RMS study: model data and sources, fault cases, rotor-angle plots, CCT table.
3. **Automation:** a short description of your PowerFactory Python script. Recruiters look for this skill.
4. PSCAD: a fault-current waveform plot, and the i_p comparison with IEC 60909.
5. Conclusions: which faults are most critical and why.

**✅ P5 is done when**
- [ ] The CCT search runs automatically from one script.
- [ ] The PSCAD peak-current check is documented with numbers.
