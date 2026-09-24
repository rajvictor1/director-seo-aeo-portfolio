# Schema.org Brief — Hevo Data

## Global Entities

### Organization
Apply to every page via JSON-LD in `<head>`.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Hevo Data",
  "url": "https://hevodata.com",
  "logo": "https://hevodata.com/logo.png",
  "sameAs": [
    "https://www.linkedin.com/company/hevo-data",
    "https://www.g2.com/products/hevo-data/reviews",
    "https://www.capterra.com/p/213570/Hevo-Data/",
    "https://www.crunchbase.com/organization/hevo-data"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "sales",
    "email": "sales@hevodata.com",
    "url": "https://hevodata.com/schedule-demo"
  }
}
```

### SoftwareApplication
Apply to homepage and product pages.

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Hevo Data",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Any (SaaS / Cloud)",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD",
    "description": "Free tier up to 1 million events/month"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.4",
    "reviewCount": "271",
    "bestRating": "5",
    "worstRating": "1"
  },
  "featureList": [
    "150+ pre-built connectors",
    "No-code pipeline builder",
    "Near real-time data sync",
    "Automatic schema drift handling",
    "dbt transformations",
    "CDC database replication",
    "SOC 2, GDPR, CCPA, HIPAA compliant"
  ],
  "softwareVersion": "Cloud SaaS",
  "provider": {
    "@type": "Organization",
    "name": "Hevo Data"
  }
}
```

## Page-Level Schema

### Comparison Pages
Use `WebPage` + `FAQPage`.

```json
{
  "@context": "https://schema.org",
  "@type": ["WebPage", "FAQPage"],
  "name": "Hevo vs Fivetran: Which ETL Tool is Right for You?",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is Hevo easier to set up than Fivetran?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hevo is designed for no-code setup and typically gets first pipeline running in under 5 minutes. Fivetran offers broader enterprise governance but often requires more configuration and engineering involvement during onboarding."
      }
    }
  ]
}
```

### Integration Pages
Use `HowTo` + `FAQPage`.

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Connect Salesforce to Snowflake with Hevo",
  "description": "Set up a no-code Salesforce to Snowflake pipeline in minutes.",
  "totalTime": "PT10M",
  "tool": [
    { "@type": "HowToTool", "name": "Hevo Data account" },
    { "@type": "HowToTool", "name": "Salesforce credentials" },
    { "@type": "HowToTool", "name": "Snowflake warehouse" }
  ],
  "step": [
    {
      "@type": "HowToStep",
      "name": "Select Salesforce as source",
      "text": "In Hevo, choose Salesforce from the source catalog and authenticate with your credentials."
    },
    {
      "@type": "HowToStep",
      "name": "Select Snowflake as destination",
      "text": "Choose Snowflake as your destination and enter your warehouse connection details."
    },
    {
      "@type": "HowToStep",
      "name": "Map fields and activate",
      "text": "Map objects, set sync frequency, and activate the pipeline."
    }
  ]
}
```

### Case Study Pages
Use `CaseStudy` + `Organization`.

```json
{
  "@context": "https://schema.org",
  "@type": "CaseStudy",
  "name": "How ThoughtSpot Reduced Platform Costs 85% with Hevo",
  "about": {
    "@type": "Organization",
    "name": "ThoughtSpot"
  },
  "provider": {
    "@type": "Organization",
    "name": "Hevo Data"
  },
  "description": "ThoughtSpot used Hevo to modernize its data operations, achieving 85% platform cost reduction and 100% uptime."
}
```

### Pricing Page
Use `Offer` or `AggregateOffer`.

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Hevo Data Pricing",
  "mainEntity": {
    "@type": "AggregateOffer",
    "name": "Hevo Data Plans",
    "offers": [
      {
        "@type": "Offer",
        "name": "Free",
        "price": "0",
        "priceCurrency": "USD",
        "description": "Up to 1 million events/month"
      },
      {
        "@type": "Offer",
        "name": "Starter",
        "price": "239",
        "priceCurrency": "USD",
        "priceValidInterval": "P1M",
        "description": "Starting at $239/month for growing teams"
      }
    ]
  }
}
```

## Validation

- Run every page through Google Rich Results Test or Schema Markup Validator
- Maintain a schema inventory in a Google Sheet or SEO platform
- Track invalid markup errors weekly until zero critical issues remain
