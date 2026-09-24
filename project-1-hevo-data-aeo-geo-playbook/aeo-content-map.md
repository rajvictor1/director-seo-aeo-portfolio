# AEO Content Map — Hevo Data

This file maps high-value AI-search questions to the pages Hevo should own or create.

## Comparison Questions

| Question | Existing / Proposed Page | Content Type | Priority |
|----------|--------------------------|--------------|----------|
| Hevo vs Fivetran — which is easier? | `/vs/fivetran` | Comparison + FAQ | P0 |
| Hevo vs Airbyte for no-code teams? | `/vs/airbyte` | Comparison + FAQ | P0 |
| Hevo vs Stitch for startups? | `/vs/stitch` | Comparison + FAQ | P1 |
| Cheaper alternative to Fivetran | `/vs/fivetran` + blog | Blog + comparison | P1 |
| Best no-code ETL tool for Snowflake | `/best-no-code-etl-snowflake` | Guide + FAQ | P0 |

## Integration Questions

| Question | Existing / Proposed Page | Content Type | Priority |
|----------|--------------------------|--------------|----------|
| How do I sync Salesforce to Snowflake? | `/integrations/salesforce-to-snowflake` | HowTo + FAQ | P0 |
| Load Stripe data into BigQuery | `/integrations/stripe-to-bigquery` | HowTo + FAQ | P0 |
| Connect HubSpot to Redshift | `/integrations/hubspot-to-redshift` | HowTo + FAQ | P1 |
| PostgreSQL CDC to BigQuery | `/integrations/postgresql-cdc-bigquery` | HowTo + FAQ | P1 |
| Replicate MySQL to Databricks | `/integrations/mysql-to-databricks` | HowTo + FAQ | P1 |

## Capability Questions

| Question | Existing / Proposed Page | Content Type | Priority |
|----------|--------------------------|--------------|----------|
| What is reverse ETL and do I need it? | `/blog/reverse-etl-guide` | Blog + FAQ | P1 |
| How to handle schema drift in ETL | `/blog/schema-drift-etl` | Blog + FAQ | P0 |
| No-code data pipeline monitoring tools | `/no-code-pipeline-monitoring` | Solution page | P1 |
| How to replicate SaaS data to warehouse | `/blog/saas-to-warehouse-replication` | Blog + FAQ | P1 |
| Best ETL tool without data engineer | `/best-etl-no-data-engineer` | Guide + FAQ | P0 |

## Brand / Trust Questions

| Question | Existing / Proposed Page | Content Type | Priority |
|----------|--------------------------|--------------|----------|
| Is Hevo Data HIPAA compliant? | `/security` or `/compliance` | Trust page | P1 |
| Hevo Data pricing | `/pricing` | Pricing page | P0 |
| Hevo Data reviews | G2 + `/reviews` | Social proof | P1 |
| Hevo Data case studies | `/success-stories` | Case studies | P1 |

## Content Format Rules

For every page in this map, structure the content so AI models can cite it:
1. Title and H1 match the natural question
2. First 100 words give a direct, unambiguous answer
3. Include a comparison table where relevant
4. Add a real customer or G2 quote for trust
5. Link internally to product, docs, and pricing
6. Markup with `FAQPage`, `HowTo`, or `SoftwareApplication` schema

## Update Cadence

Review and refresh this map quarterly based on:
- New competitor launches
- New connector releases
- AI answer gap analysis
- Keyword / prompt research from ChatGPT, Gemini, Claude
