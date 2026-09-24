# Project 1 — Hevo Data AEO/GEO Playbook

## Executive Summary

Hevo Data is a no-code ETL/ELT data integration platform serving mid-market data teams that need fast, managed pipelines without dedicated data engineering resources. This playbook defines a 90-day AI-search (AEO/GEO) strategy to position Hevo as the answer inside ChatGPT, Gemini, and Claude for high-intent data integration and ETL buying questions.

This artifact demonstrates Director-level ownership of:
- AEO/GEO strategy
- B2B SaaS product marketing SEO
- Schema.org and `llms.txt` implementation
- Cross-functional execution roadmap
- Forecasting and measurement

---

## 1. Business Context

### Product Snapshot
- **Company:** Hevo Data
- **Website:** https://hevodata.com
- **Category:** No-code ETL/ELT data integration platform
- **Core value:** Set up data pipelines in minutes without writing code; event-based transparent pricing
- **Target buyers:** Data analysts, RevOps, growth teams, and small-to-mid-market data engineers
- **Key competitors:** Fivetran, Airbyte, Stitch, Matillion, Rivery, Informatica

### Why AEO/GEO Matters for Hevo
AI search engines are increasingly the first stop for B2B buyers. Queries like "best no-code ETL tool for Snowflake" or "Hevo vs Fivetran" are now being answered directly by ChatGPT, Gemini, and Claude. AEO/GEO ensures Hevo’s content, data, and authority signals are the sources those models cite.

---

## 2. Strategic Priorities

| Priority | Objective | AI-Search Intent |
|----------|-----------|------------------|
| 1 | Own the comparison narrative | "Hevo vs Fivetran", "Hevo vs Airbyte", "best no-code ETL" |
| 2 | Capture integration-specific queries | "Connect Salesforce to Snowflake", "Stripe to BigQuery pipeline" |
| 3 | Build programmatic solution pages | "no-code CDC replication", "schema drift handling" |
| 4 | Earn citations through authority | G2, Gartner Peer Insights, Reddit, data engineering blogs |
| 5 | Enable model discoverability | `llms.txt`, structured data, entity clarity |

---

## 3. AI-Citation Content Framework

### Questions Hevo Should Own

#### Category 1: Tool Comparison
- "What is the best no-code ETL tool for small data teams?"
- "Hevo vs Fivetran: which is easier to set up?"
- "Airbyte vs Hevo: which is better for teams without data engineers?"
- "Cheaper alternative to Fivetran for startups"

#### Category 2: Integration-Specific
- "How do I sync Salesforce data to Snowflake without code?"
- "Best way to load Stripe data into BigQuery"
- "Connect HubSpot to Redshift automatically"
- "PostgreSQL CDC to BigQuery"

#### Category 3: Capability / Use Case
- "How to handle schema drift in ETL pipelines"
- "What is reverse ETL and do I need it?"
- "No-code data pipeline monitoring tools"
- "How to replicate SaaS data to a data warehouse"

### Content Format for AI Citations
Each answer target should be answered in a format AI models can easily extract and cite:
- H2/H3 question mirror
- 2–3 sentence direct answer
- Bulleted comparison or step list
- Real customer evidence (case study, G2 quote)
- Internal link to deeper product or documentation page

---

## 4. `llms.txt` for Hevo Data

See [`llms.txt`](llms.txt) for the full implementation.

### Purpose
`llms.txt` helps AI crawlers understand Hevo’s site structure, trust signals, and most citation-worthy pages.

### Key Sections
- **Site identity** — what Hevo is and who it serves
- **Crawl preferences** — allowed and disallowed sections
- **Citation-ready pages** — comparison pages, integration guides, case studies, docs
- **Authority signals** — G2 profile, Gartner, SOC 2, customer logos
- **Product facts** — connector count, free tier, pricing model

---

## 5. Schema.org Implementation Brief

### Recommended Markup

| Page Type | Schema Type | Business Impact |
|-----------|-------------|-----------------|
| Homepage | `Organization`, `SoftwareApplication` | Entity clarity for brand queries |
| Pricing | `Offer`, `AggregateOffer` | Pricing model transparency in AI answers |
| Integration pages | `HowTo`, `FAQPage` | Capture connector-specific queries |
| Comparison pages | `WebPage` + `FAQPage` | Own vs-pages in AI citations |
| Case studies | `CaseStudy`, `Organization` (customer) | Trust and social proof |
| Docs / help | `TechArticle`, `HowTo` | Support and implementation queries |

### Priority Schema Fields
- `name`, `applicationCategory`, `operatingSystem`, `offers`, `aggregateRating`
- `featureList` for key product capabilities
- `sameAs` linking to G2, LinkedIn, Crunchbase
- `FAQPage` markup for comparison and integration pages

---

## 6. 90-Day Execution Roadmap

### Phase 1 — Foundation (Days 1–30)
- [ ] Publish `llms.txt` at root
- [ ] Roll out `Organization` + `SoftwareApplication` schema sitewide
- [ ] Audit and refresh top 10 comparison pages for AEO formatting
- [ ] Build FAQ schema for top 20 integration pages
- [ ] Define AI-search KPI baseline (brand mentions, cited URLs)

### Phase 2 — Scale (Days 31–60)
- [ ] Launch 5 new comparison pages (Hevo vs X)
- [ ] Launch 10 new integration-specific solution pages
- [ ] Add case-study schema and customer quote modules
- [ ] Pitch 3 data-engineering blogs for authority citations
- [ ] Begin G2/Gartner review-response cadence

### Phase 3 — Optimize (Days 61–90)
- [ ] Compare AI-engine citation share vs competitors
- [ ] Refresh underperforming pages based on AI answer gaps
- [ ] Launch programmatic "Connect [Source] to [Destination]" page series
- [ ] Build internal AEO dashboard
- [ ] Present 90-day results to leadership

---

## 7. Measurement Framework

### Leading Indicators (Weekly)
- Brand mention count inside AI answers for target query sets
- Citation URL share (Hevo pages cited vs competitor pages)
- New AEO-optimized pages indexed
- Schema markup validity score

### Lagging Indicators (Monthly)
- Organic traffic to comparison and integration pages
- Branded search volume trend
- Demo/signup conversions from organic search
- Backlinks and referring domains from AEO content

### Forecast Model
See [`forecast-model.md`](forecast-model.md) for the 90-day forecast assumptions and model.

---

## 8. RACI

| Activity | SEO (You) | Product | Engineering | Content/PMM | PR |
|----------|-----------|---------|-------------|-------------|-----|
| `llms.txt` + schema rollout | A | C | R | C | I |
| Comparison page content | A | C | I | R | C |
| Integration page templates | A | R | R | C | I |
| Case-study schema | A | C | R | R | C |
| Authority citations / PR | A | I | I | C | R |
| KPI reporting | A | I | I | C | I |

**R = Responsible, A = Accountable, C = Consulted, I = Informed**

---

## 9. Files in This Project

| File | Purpose |
|------|---------|
| [`README.md`](README.md) | This file — the strategic playbook |
| [`llms.txt`](llms.txt) | Machine-readable AI-search site guide |
| [`forecast-model.md`](forecast-model.md) | 90-day traffic and citation forecast |
| [`schema-brief.md`](schema-brief.md) | Detailed Schema.org markup brief |
| [`aeo-content-map.md`](aeo-content-map.md) | Full question-to-page mapping |

---

*Built as a Director of SEO & AEO portfolio piece. All product context is based on publicly available information about Hevo Data.*

Built by Rajesh Kumar | Powered by [BrandOps Site](https://www.brandops.site)
