# Project 3 — AI Search Visibility & Citation Dashboard

## Executive Summary

This project is a working dashboard and measurement framework for tracking brand visibility inside AI search answers (ChatGPT, Gemini, Claude). It is built around Hevo Data as the subject and shows how a Director of SEO & AEO would measure AI-search acquisition, report to leadership, and forecast business impact.

The dashboard uses simulated data because public APIs for AI-search citations do not yet exist at scale. The methodology and metrics are real, and the code structure is ready to swap in live probe data when APIs become available.

---

## 1. Why AI-Search Measurement Matters

B2B buyers are increasingly starting their evaluation in conversational search engines. For Hevo Data, queries like:
- "best no-code ETL tool for Snowflake"
- "Hevo vs Fivetran"
- "how do I sync Salesforce to Snowflake without code"

...are now being answered directly by AI models. If Hevo is not cited, competitors get the traffic, trust, and demo signups that would have come from traditional organic search.

---

## 2. KPI Framework

### Primary KPIs (Leadership Reporting)

| KPI | Definition | Target |
|-----|------------|--------|
| Citation Share | % of target prompts where Hevo is cited | 45% by end of quarter |
| Cited URL Count | Unique Hevo URLs appearing in AI answers | +40% vs baseline |
| Brand Mention Trend | Monthly absolute mentions across engines | +25% MoM |
| Sentiment Score | % of Hevo mentions that are positive | > 70% |

### Secondary KPIs

| KPI | Definition |
|-----|------------|
| Engine Coverage | Citation rate by ChatGPT / Gemini / Claude |
| Competitor Gap | Hevo share vs Fivetran / Airbyte by engine |
| Prompt Coverage | % of target prompt set probed |
| URL Diversity | Number of distinct Hevo pages cited |

---

## 3. Data Collection Methodology

### Prompt Set
A fixed set of 150 prompts representing category, comparison, integration, capability, brand, and trust intent. See [`data/prompt_set.csv`](data/prompt_set.csv) for a sample.

### Probe Sampling
- Run 150 probes per month across ChatGPT, Gemini, and Claude.
- Record whether Hevo is mentioned, which URL(s) are cited, and sentiment.
- Rotate a subset of prompts monthly to capture emerging queries.

### Automation
Until stable APIs exist:
- Manual sampling with structured logging
- Future: OpenAI / Anthropic / Google APIs for programmatic answer extraction
- Future: third-party AEO monitoring tools

---

## 4. Dashboard

The interactive dashboard is at [`dashboard.html`](dashboard.html).

It shows:
- Monthly citation share trend (Hevo vs competitors)
- Brand mentions by AI engine
- Sentiment breakdown
- Top cited Hevo URLs
- Forecast tying citations to estimated traffic

---

## 5. Sample Findings from Simulated Data

| Finding | Implication |
|---------|-------------|
| Hevo citation share grew from 12% to 32% over 6 months | AEO playbook is working |
| ChatGPT is the strongest engine for Hevo | Prioritize ChatGPT-optimized content |
| Comparison pages are the most cited URLs | Double down on vs-pages |
| Sentiment is 75%+ positive | Reputation management is effective |
| Fivetran still leads overall share | Close gap with more authority content |

---

## 6. Forecast Model

### Logic
- Each AI citation ≈ 3–5 incremental organic clicks to the cited URL
- 1,000 monthly AI citations ≈ 3,000–5,000 incremental sessions
- At 2.5% demo CVR and 15% SQL rate ≈ 11–19 SQLs per month
- At 20% close and $15K ACV ≈ $33K–$57K new monthly ACV

### 90-Day Target
- Increase Hevo citation share from 32% to 45% across target prompt set
- Estimated incremental impact: 5,000–8,000 sessions, 12–20 SQLs, $36K–$60K new ACV

---

## 7. Reporting Cadence

| Report | Audience | Frequency | Contents |
|--------|----------|-----------|----------|
| AEO Pulse | SEO team | Weekly | Mention counts, new cited URLs, anomalies |
| AEO Review | Head of Marketing | Monthly | Citation share, competitor gap, action items |
| Board Snapshot | C-level | Quarterly | Traffic forecast, pipeline impact, ROI |

---

## 8. Files in This Project

| File | Purpose |
|------|---------|
| [`README.md`](README.md) | Strategy and methodology |
| [`dashboard.html`](dashboard.html) | Interactive HTML dashboard |
| [`data/citation_data.json`](data/citation_data.json) | Simulated citation dataset |
| [`data/prompt_set.csv`](data/prompt_set.csv) | Target prompt set sample |
| [`measurement-framework.md`](measurement-framework.md) | Detailed KPI and reporting specs |

---

*Built as a Director of SEO & AEO portfolio piece. Dashboard data is simulated to demonstrate methodology.*

Built by Rajesh Kumar | Powered by [BrandOps Site](https://www.brandops.site)
