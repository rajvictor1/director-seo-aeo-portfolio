# AI Search Citation Measurement Framework

## 1. Purpose
Define how a Director of SEO & AEO measures AI-search brand visibility and reports results to leadership.

## 2. Dimensions

### Brand
Track mentions of the target brand (Hevo Data) and key competitors (Fivetran, Airbyte, Stitch, Matillion).

### Engines
ChatGPT, Gemini, Claude.

### Prompt Categories
- **Category** — "best no-code ETL tool"
- **Comparison** — "Hevo vs Fivetran"
- **Integration** — "sync Salesforce to Snowflake"
- **Capability** — "how to handle schema drift"
- **Brand** — "Hevo Data pricing"
- **Trust** — "Is Hevo HIPAA compliant"

### Metrics
| Metric | Type | Formula |
|--------|------|---------|
| Citation share | % | Mentions of brand / total relevant answers |
| Absolute mentions | Count | Sum of monthly brand mentions |
| Cited URLs | Count | Distinct URLs cited for brand |
| Sentiment | % | Positive / neutral / negative split |
| Engine coverage | % | Prompts with data per engine |
| Competitor gap | % | Brand share - competitor share |

## 3. Sampling Method

### Stratified Random Sampling
- 150 prompts per month
- 30 prompts per category (6 categories)
- 50 prompts per engine
- Rotate 20% of prompts monthly to capture new trends

### Data Points per Answer
- Was the brand mentioned? (yes/no)
- Was the brand cited with a URL? (yes/no)
- Which URL was cited?
- Sentiment (positive / neutral / negative)
- Position in answer (first / second / later)

## 4. Quality Controls

- Two reviewers score 10% of answers to measure inter-rater reliability.
- Flag answers where the model contradicts itself or hallucinates facts.
- Exclude prompts that return errors or non-answers.

## 5. Tools

| Stage | Tool |
|-------|------|
| Prompt management | Google Sheet / Airtable |
| Manual probing | ChatGPT, Gemini, Claude web UI |
| Structured logging | CSV / JSON |
| Dashboard | Static HTML + Chart.js |
| Future automation | Platform APIs + custom scraper |

## 6. Reporting

### Weekly AEO Pulse (SEO Team)
- New mentions this week
- New cited URLs
- Anomalies (drops, competitor spikes)
- Action items for content / PR

### Monthly AEO Review (Head of Marketing)
- Citation share trend
- Competitor gap
- Top cited pages
- Content / schema / PR actions taken

### Quarterly Board Snapshot (C-level)
- AI-search share of organic strategy
- Forecasted traffic and pipeline impact
- ROI of AEO program
- Resource asks for next quarter

## 7. Risks and Caveats

- AI-search citation measurement is not yet standardized.
- Platform APIs may restrict programmatic access.
- Sentiment scoring is subjective; use reviewer calibration.
- Correlation to revenue is directional, not causal.

---

Built by Rajesh Kumar | Powered by [BrandOps Site](https://www.brandops.site)
