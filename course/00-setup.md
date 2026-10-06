# Phase 0: Setup and Orientation (week 1, about 10 h)

**Phase outcome:** every tool works, your portfolio repo exists, and you know exactly which job you are training for.

---

## Step 0.1: Read 10 real job postings (1.5 h)

**🎯 Objective:** know exactly which skills employers want in your target country.

**🛠️ Do**
1. Search LinkedIn or Indeed for: `graduate power systems engineer`, `power system studies engineer`, `grid connection engineer`, `junior protection engineer`.
2. Open 10 postings. Copy them into a file named `career/job-postings.md`. For each one, write down:
   - the tools named (PowerFactory, PSS®E, PSCAD, ETAP, MATLAB, Python …)
   - the studies named (load flow, short circuit, protection, harmonics, dynamic, EMT …)
   - the standards named (IEC 60909, grid code …)
3. Count how often each item appears. Put the top 10 in a table.

**📦 Output:** `career/job-postings.md` with a frequency table.

**✅ Done when**
- [ ] You can name the 3 most requested tools and the 3 most requested study types in your market.

**⚠️ Traps:** do not skip this step. The table is how you check later that your portfolio matches the market.

---

## Step 0.2: Python environment (2 h)

**🎯 Objective:** a clean, reproducible Python setup for power system work.

**🛠️ Do**
1. Install a recent Python 3 (check the supported versions on the [pandapower PyPI page](https://pypi.org/project/pandapower)) and VS Code with the Python and Jupyter extensions.
2. In this project folder, create a virtual environment and install the packages:
   ```bash
   python -m venv .venv
   ```
   ```bash
   .venv\Scripts\activate
   ```
   ```bash
   pip install pandapower numpy pandas matplotlib jupyter openpyxl
   ```
3. Create `00_setup/test_pandapower.py` with the minimal example from the pandapower docs:
   ```python
   import pandapower as pp

   net = pp.create_empty_network()
   b1 = pp.create_bus(net, vn_kv=20.0, name="MV bus")
   b2 = pp.create_bus(net, vn_kv=0.4, name="LV bus")
   b3 = pp.create_bus(net, vn_kv=0.4, name="Load bus")
   pp.create_ext_grid(net, bus=b1, vm_pu=1.02, name="Grid")
   pp.create_transformer(net, hv_bus=b1, lv_bus=b2, std_type="0.4 MVA 20/0.4 kV")
   pp.create_line(net, from_bus=b2, to_bus=b3, length_km=0.1, std_type="NAYY 4x50 SE")
   pp.create_load(net, bus=b3, p_mw=0.1, q_mvar=0.05, name="Load")
   pp.runpp(net)
   print(net.res_bus)
   print(net.res_line)
   ```
4. Run it. You should see a voltage table (`vm_pu`) with values close to 1.0.

**📦 Output:** `00_setup/test_pandapower.py` that runs without errors.

**✅ Done when**
- [ ] `net.res_bus` prints 3 rows of voltages.
- [ ] You can explain in one sentence what each `create_...` line builds (guess now; you will learn it properly in Phases 1–3).

**⚠️ Traps:** installing into the global Python instead of `.venv`; mixing Anaconda and pip. Pick one environment and keep it.

---

## Step 0.3: Git and GitHub portfolio repo (1 h)

**🛠️ Do**
1. Create a GitHub account if you don't have one. Use a professional username (e.g. your full name).
2. Create a public repo named `power-systems-portfolio`.
3. Clone it locally and create this skeleton:
   ```
   power-systems-portfolio/
   ├── README.md              ← portfolio landing page (filled in during Phase 8)
   ├── P1-load-flow-n1/
   ├── P2-short-circuit-iec60909/
   ├── P3-overcurrent-coordination/
   ├── P4-pv-hosting-capacity/
   ├── P5-transient-stability/
   └── capstone-grid-connection-study/
   ```
4. Add a `.gitignore` that excludes `.venv/`, `__pycache__/`, and large PowerFactory export files.

**✅ Done when**
- [ ] The repo is public and has the folder skeleton (empty folders need a `README.md` placeholder for Git to keep them).

**⚠️ Traps:** do not upload licensed material: textbook scans, copyrighted IEC standard text, or your PowerFactory licence files. Uploading your own models and results is fine.

---

## Step 0.4: Check your licences (2 h)

**🎯 Objective:** know your tools' limits **before** you design projects around them.

**🛠️ Do**

**PowerFactory**
1. Open it. Find the licence information (Help menu / licence settings) and write down:
   - the **maximum number of nodes (buses)**. DIgSILENT student and thesis licences are limited by node count.
   - the **modules included**: load flow, short circuit, **protection**, **RMS simulation**, **quasi-dynamic**, contingency analysis, Python scripting.
2. Open **Help → Tutorial** and the **Examples** window. List the tutorials and examples available to you.
3. Find the Python section in the PowerFactory User Manual. Note which Python versions your PowerFactory version supports for scripting.

**PSCAD**
1. Open it and run the **"My First Simulation"** tutorial ([PSCAD] link in REFERENCES.md).
2. Note the edition limits (node count etc.) shown in your licence or edition information.
3. PSCAD needs a **Fortran compiler** configured. The PSCAD Knowledge Base explains how; do this now, not in Phase 7.

**MATLAB**
1. Note whether you have Simulink and Simscape Electrical. They are not required, but useful with [SAADAT].

**📦 Output:** `00_setup/licences.md` listing the node limit and modules for each tool.

**✅ Done when**
- [ ] You know whether your PowerFactory licence includes the **protection** and **RMS simulation** modules. Phases 5 and 7 have a fallback path if it doesn't.
- [ ] PSCAD "My First Simulation" ran and produced a plot.

**⚠️ Traps:** discovering in Phase 7 that the Fortran compiler is missing or a module is not licensed.

---

## Step 0.5: The big picture in 1 day (3 h)

**🎯 Objective:** understand the full chain from power plant to socket before any math.

**📖 Learn**
- [VONMEIER] Ch. 7 *Transmission and Distribution Systems* (skim) and Ch. 1 *Physics of Electricity* (read).
- [GLOVER] Ch. 1 *Introduction* (read sections on history, industry structure and computers in power engineering).

**🛠️ Do**
1. Draw a single-line diagram by hand: power plant → step-up transformer → transmission (e.g. 150–500 kV) → substation → MV distribution (e.g. 20 kV) → distribution transformer → LV 230/400 V → house.
2. Start `GLOSSARY.md` with the first 20 terms you meet (bus, feeder, substation, single-line diagram, MV/LV, kVA vs kW, etc.). Add to it every week.
3. Start `LOG.md`. Every session, add one line: date, hours, what you did, and one thing you learned.

**📦 Output:** a photo of the hand-drawn single-line diagram in the repo, plus `GLOSSARY.md` and `LOG.md`.

**✅ Done when**
- [ ] You can explain to a non-engineer why we step voltage **up** for transmission (hint: losses ∝ I²R).
- [ ] You know what 230/400 V means (phase-to-neutral / phase-to-phase, [IEC60038]).

---

### 🏁 Phase 0 exit checklist
- [ ] pandapower runs · [ ] GitHub repo skeleton · [ ] licence limits recorded · [ ] PSCAD first simulation · [ ] job-posting table · [ ] LOG.md started
