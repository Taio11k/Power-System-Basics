# Job-posting analysis: Australia (Step 0.1)

Collected on 2026-10-07 from SEEK Australia. Ads expire, so the key details are recorded here.

Target roles: graduate to mid-level power systems / grid connection / network planning engineer.

## The 10 postings

| # | Role | Employer | Location | Level | Link |
|---|---|---|---|---|---|
| 1 | Graduate Power System Engineer | Siemens | Melbourne VIC | Graduate | [SEEK 95004165](https://au.seek.com/job/95004165) |
| 2 | Graduate Grid Engineer | Morson Edge | Melbourne VIC | Graduate to 2 yrs | [SEEK 94519149](https://au.seek.com/job/94519149) |
| 3 | Graduate Electrical Engineer (Grid), Wind Energy | Goldwind Australia | Melbourne VIC | Graduate | [SEEK 95071321](https://au.seek.com/job/95071321) |
| 4 | Engineer – Energy System Planning | AEMO | Sydney NSW (any capital) | 2+ yrs | [SEEK 95082093](https://au.seek.com/job/95082093) |
| 5 | Engineer | AEMO | Melbourne VIC | Not stated | [SEEK 94998471](https://au.seek.com/job/94998471) |
| 6 | Engineer – Future Energy Planning | Endeavour Energy (DNSP) | Parramatta NSW | Not stated | [SEEK 94961890](https://au.seek.com/job/94961890) |
| 7 | Power Systems Engineer (Engineer/Senior/Principal) | SM Grid Partners | Melbourne VIC / Brisbane QLD | Several levels | [SEEK 94870009](https://au.seek.com/job/94870009) |
| 8 | Grid Engineer | Resourceful Recruitment | Brisbane QLD | 2–5 yrs | [SEEK 94905643](https://au.seek.com/job/94905643) |
| 9 | Electrical Engineer | FortEng | Brisbane QLD | 2+ yrs | [SEEK 95024709](https://au.seek.com/job/95024709) |
| 10 | Power Systems Engineer (Mid to Senior) | GHD | Perth WA | Mid to senior | [SEEK 94568212](https://au.seek.com/job/94568212) |

Not counted: WSP's "Power & Energy Group" expressions of interest (junior to principal; no tools or studies named) and Acerez's Power System Engineer (5+ years; PSS/E, PSCAD, Python, NER generator performance assessment).

### What each posting names

| # | Tools | Studies | Rules and standards |
|---|---|---|---|
| 1 | PSS®E, PSCAD, PowerFactory, Python | Steady-state, transient, power quality, small-signal; grid connection engineering for the NEM | NER |
| 2 | PSS/E, PSCAD, PowerFactory | Load flow, dynamic analysis, wind turbine model validation; grid connection, registration and commissioning documents | AEMO, GPS |
| 3 | none named | Grid connection; power systems; NEM | AEMO |
| 4 | PSS/E, PSCAD, PowerFactory | Load flow, fault level; Integrated System Plan (ISP) | AEMO |
| 5 | PSS®E, PowerFactory, PSCAD, Python (automation) | Load flow, fault level; system strength and inertia; ISP | NEM |
| 6 | none named ("data science techniques") | Network constraint modelling, connection assessments, forecasting, planning | none named |
| 7 | PSCAD, PSS/E, PowerFactory | Grid connection studies for BESS, solar, wind, data centres | NEM/WEM, Australian grid code |
| 8 | PSS/E (with Python scripting), PSCAD, PowerFactory | Grid connection modelling; R0/R1/R2 model data and validation; hold-point testing | NER Chapter 5, Schedule 5.2, clause 5.3.4A/B; GPS; AEMO |
| 9 | PSCAD, DIgSILENT PowerFactory, PSS®E | Design and modelling of utility renewable projects | none named |
| 10 | PowerFactory, ETAP, PSCAD, Python | Load flow, fault analysis, stability, dynamic studies | WA ESM Rules, Technical Rules, AEMO |

## Frequency table (top 10)

| Rank | Item | Type | Count (of 10) |
|---|---|---|---|
| 1 | PowerFactory | Tool | 8 |
| 1 | PSCAD (EMT) | Tool | 8 |
| 3 | PSS®E | Tool | 7 |
| 4 | Grid connection / generator studies | Study | 5 |
| 5 | Load flow | Study | 4 (5 counting #6's constraint modelling) |
| 5 | Python | Tool | 4 |
| 5 | NEM / WEM market knowledge | Rules | 4 |
| 5 | AEMO processes | Rules | 4 |
| 9 | Fault level / short circuit | Study | 3 |
| 9 | Dynamic / stability (RMS) | Study | 3 |
| 9 | Network planning (ISP, DNSP planning) | Study | 3 |

Named less often: NER (2), GPS (2), power quality (1), system strength (1), ETAP (1), MATLAB (0), protection (0 in this sample), IEC or AS standards (0).

## Answers to "Done when"

- **3 most requested tools:** PowerFactory, PSCAD, PSS®E (Python close behind).
- **3 most requested study types:** grid connection studies, load flow, then fault level and dynamic stability (tied).

## What this means for the course

1. **The course already matches most of the market.** Load flow (P1), fault level (P2), dynamic stability (P5), PowerFactory and Python automation are all in it. The capstone (a grid connection study for a PV + BESS plant) is exactly the most common job type here.
2. **PSCAD matters more in Australia than the course assumes.** It is in 8 of 10 ads, because AEMO requires EMT models for connections. Install it (free edition; register at pscad.com) and do the Phase 7 EMT demo in PSCAD, not only in PowerFactory's EMT module.
3. **PSS®E is not in the course but is in 7 of 10 ads.** Siemens offers a free academic version, *PSS®E Xplore*, with full capability up to 50 buses ([Siemens page](https://www.siemens.com/fr-ca/products/pss-software/psse-explore-academic-users/)). The 9-bus system fits easily, so P1 could also be cross-checked in PSS®E.
4. **Australian rules replace the European grid code.** Ads ask for the NER (Chapter 5 and Schedule 5.2), Generator Performance Standards (GPS) and AEMO's connection process. The capstone uses the EU [RfG] as its grid-code framework; for this market, use NER S5.2 instead.
5. **Protection was not named in this sample.** Keep P3; protection roles exist in Australia but are often advertised separately by utilities and secondary-systems contractors.
