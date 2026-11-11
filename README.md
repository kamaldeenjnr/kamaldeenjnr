<a href="https://modelanalysishub.com">
  <img src="assets/banner.png" width="100%" alt="Amadu Kamal, data analyst and software engineer, Model Analysis Hub, Ghana. Beside the name, a map of Ghana's regions shaded by predicted malaria risk from his 2025 spatial model.">
</a>

<p>
  <a href="https://modelanalysishub.com">modelanalysishub.com</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/amadu-kamal-65ab5326a">LinkedIn</a> &nbsp;·&nbsp;
  <a href="mailto:amadukamal8@gmail.com">amadukamal8@gmail.com</a> &nbsp;·&nbsp;
  <a href="https://wa.me/233595586430">WhatsApp</a>
</p>

I trained in public health (BPH, Health Information, University of Health and Allied Sciences) and I write software. Most of my work sits where those meet: a model is only finished when someone can act on it, so I build the statistics and the system around them.

**Now**
- Taking **SafeWatch** from testing to a field trial at landing sites on the Volta Lake.
- Maintaining **QuantAI**, an in-browser statistics engine, and **ResearchGuard ML**, a validation tool for clinical prediction models.
- Weekly updates to a [funded-opportunities board](https://modelanalysishub.com/opportunities.html) for Ghanaian students.

<br>

## Systems

### SafeWatch &nbsp;<sub>water emergency alerts for the Volta Lake · grant project · 2026</sub>

Help on the lake often starts late because nobody knows where the accident is or whose job it is to go. SafeWatch routes an SOS to a named person on duty for that stretch of water and keeps escalating until someone accepts it.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/safewatch-architecture-dark.svg">
  <img src="assets/safewatch-architecture-light.svg" width="100%" alt="SafeWatch architecture: SOS from Android, browser, SMS or USSD; FastAPI and PostgreSQL server; escalation from on-duty responder to backup to coordinator, plus the nearest responder sharing location; dispatch screen; trip check-ins, storm warnings and an audit log alongside.">
</picture>

- **Four ways in, one queue.** Android, an installable web app, SMS and a USSD menu all create the same alert record, so a fisher with a basic phone is served the same way as one with a smartphone.
- **Acceptance, not delivery.** An alert counts as handled only when a person accepts it. Unanswered alerts move to the backup, then the coordinator, and in parallel to the closest responder sharing a location.
- **Alerts nobody has to send.** A missed trip check-in raises an alert by itself with the last known position. The forecast is checked hourly and storm warnings are drafted in Ewe, Twi and English for staff to send.

<sub><code>Python</code> <code>FastAPI</code> <code>PostgreSQL</code> <code>React</code> <code>TypeScript</code> <code>React Native</code> <code>Leaflet</code> <code>Africa's Talking</code> · <a href="https://modelanalysishub.com/projects.html#safewatch">case study</a> · <a href="https://safewatch-xyqr.onrender.com">live test server</a></sub>

<br>

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://modelanalysishub.com/ai.html"><img src="assets/work/quantai.webp" width="100%" alt="QuantAI interface"></a>
      <h3>QuantAI</h3>
      <p>A statistics engine that runs entirely in the browser, so data never leaves the user's machine. It picks each test from assumption checks (Shapiro-Wilk, Brown-Forsythe, expected counts), fits linear, logistic, Poisson, ordinal, multinomial, mixed-effects and Cox models with diagnostics, and exports every analysis as Stata, R, Python and SPSS code. Results are checked against SciPy and statsmodels.</p>
      <sub><code>JavaScript</code> <code>Cloudflare Workers</code> · <a href="https://modelanalysishub.com/ai.html">open it</a></sub>
    </td>
    <td width="50%" valign="top">
      <a href="https://modelanalysishub.com/projects.html#soma"><img src="assets/work/soma.webp" width="100%" alt="Soma food delivery platform"></a>
      <h3>Soma</h3>
      <p>Food delivery for Ho, Hohoe and the Volta Region. Customer, vendor, rider and admin apps on one backend; Mobile Money and card payments through Paystack with automatic payouts; delivery confirmed by PIN. Admin two-step sign-in, CSRF protection and automated tests on the money flows.</p>
      <sub><code>Node.js</code> <code>Express</code> <code>SQLite</code> <code>Paystack</code> · <a href="https://modelanalysishub.com/projects.html#soma">case study</a></sub>
    </td>
  </tr>
</table>

<br>

## Research and methods

<table>
  <tr>
    <td width="58%" valign="top">
      <img src="assets/researchguard-optimism.svg" width="100%" alt="Forest plot of optimism by scenario and model: up to 0.18 AUC on synthetic data where patients are recognisable, near zero on controls and on 99,343 real hospital visits.">
    </td>
    <td width="42%" valign="top">
      <h3><a href="https://github.com/kamaldeenjnr/researchguard-ml">ResearchGuard ML</a></h3>
      <p>When one patient has several records, a shuffled train/test split can test a model on people it has already seen. ResearchGuard builds splits that respect patients, sites and time, verifies every fold, and reports how much the usual method inflates the score.</p>
      <p>On 99,343 encounters from the Diabetes 130-US dataset, 20% of patients crossed random splits but AUC moved by at most 0.005. On data built with the problem, the inflation reached 0.18. Both results are reported.</p>
      <sub><code>Python</code> <code>scikit-learn</code> · v0.1.2 · 39 tests · CI on Python 3.10, 3.11 and 3.12</sub>
    </td>
  </tr>
  <tr>
    <td width="58%" valign="top">
      <a href="https://modelanalysishub.com/projects.html#malaria-risk"><img src="assets/work/malaria.webp" width="100%" alt="Predicted malaria risk by region in Ghana"></a>
    </td>
    <td width="42%" valign="top">
      <h3>Malaria risk across Ghana</h3>
      <p>A spatial model combining climate, population density and historical incidence to rank regional risk, estimate the probability that prevalence exceeds 30%, and compare predictions with observed prevalence region by region.</p>
      <sub><code>R</code> <code>Python</code> <code>ArcGIS</code> · 2025 · <a href="https://modelanalysishub.com/projects.html#malaria-risk">maps and validation</a></sub>
      <h3><a href="https://github.com/kamaldeenjnr/stroke-risk-prediction">stroke-risk-prediction</a></h3>
      <p>Stroke risk on clinical data where 4.9% of patients have the outcome: SMOTE inside the pipeline and a threshold set for 80% recall, because a screening tool has to catch the people at risk.</p>
      <sub><code>Python</code> <code>scikit-learn</code></sub>
    </td>
  </tr>
</table>

<br>

## Client and platform work

| | Project | What it is |
|---|---|---|
| <img src="assets/work/sunshine.webp" width="150" alt="The Sunshine Project website"> | **[The Sunshine Project](https://www.thesunshineproject.foundation)**<br><sub>NGO · 2026</sub> | Website for a Ghanaian NGO with a content system their staff run themselves, on its own domain with structured data and a sitemap. |
| <img src="assets/work/dashboard.webp" width="150" alt="Healthcare utilisation dashboard"> | **[Healthcare utilisation dashboard](https://modelanalysishub.com/projects.html#healthcare-dashboard)**<br><sub>Health data</sub> | Cost by diagnosis, length of stay by risk category and outcomes, filtered by region and facility type. |
| <img src="assets/work/projectflow.webp" width="150" alt="ProjectFlow"> | **[ProjectFlow](https://modelanalysishub.com/projects.html#projectflow)**<br><sub>Web platform · 2025</sub> | Research project management for universities, from undergraduate to PhD, draft to publication. |

<br>

## Toolkit

**Analysis** &nbsp; R · Python (pandas, NumPy, SciPy, statsmodels, scikit-learn) · Stata · ArcGIS<br>
**Engineering** &nbsp; TypeScript · JavaScript · FastAPI · Node.js · React · React Native · PostgreSQL · SQLite<br>
**Health data** &nbsp; DHIMS · e-Tracker · KoboCollect · GHILMIS<br>
**Infrastructure** &nbsp; GitHub Actions · Render · Vercel · Cloudflare Workers · GitHub Pages

<br>

<sub>Ghana · open to analysis, research and engineering work · <a href="https://modelanalysishub.com/#contact">get in touch</a></sub>
