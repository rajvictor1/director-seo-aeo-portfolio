# Architecture Recommendations — Multi-Million URL Global Marketplace

## 1. URL Taxonomy Principles

### Rules
- Keep URLs lowercase, hyphen-separated, and under 75 characters.
- Avoid query parameters in canonical URLs except for pagination and faceted filters.
- Every market gets a clear ccTLD or language-folder path.
- Canonical pages never include session IDs, tracking parameters, or sort parameters.

### Recommended Structure

```
https://{market-domain}/
├── /category/{category-slug}/
│   ├── /category/{category-slug}/?page=2                    (paginated)
│   └── /category/{category-slug}/?color=red&style=modern   (faceted)
├── /product/{product-slug}/
├── /photo/{photo-id}-{descriptive-slug}/
├── /discussion/{topic-id}-{slug}/
├── /magazine/{article-slug}/
├── /professional/{professional-id}-{slug}/
└── /sitemap.xml  → sitemap index per market
```

## 2. Hreflang Implementation

### Pattern
```html
<link rel="alternate" hreflang="en-us" href="https://example.com/product/{slug}/" />
<link rel="alternate" hreflang="en-gb" href="https://example.co.uk/product/{slug}/" />
<link rel="alternate" hreflang="de"     href="https://example.de/product/{slug}/" />
<link rel="alternate" hreflang="x-default" href="https://example.com/product/{slug}/" />
```

### Implementation Notes
- Place tags in `<head>` AND include in XML sitemaps as backup.
- Use self-referencing hreflang on every canonical page.
- Implement a shared ID (`page_uuid`) in the CMS to link equivalent pages across markets.
- Audit weekly via Screaming Frog / custom crawler for return-tag errors.

## 3. Faceted Navigation Rules

### Canonical Behavior
- Default category page is canonical.
- Faceted pages use `rel="canonical"` to the default category page.
- For high-value facet combinations (e.g., `/sofas/material-leather/`), create clean URL and canonicalize to itself.

### Pagination
- Use `rel="next"` / `rel="prev"` historically, but primarily rely on canonical to root category.
- Include `?page=N` in sitemaps only if paginated pages rank independently.

## 4. Internal Linking Model

### Page Type Linking Rules

| Source Type | Links To | Count |
|-------------|----------|-------|
| Home | Top categories, trending products, latest magazine | 20–30 |
| Category | Products, subcategories, related photos | 24–36 |
| Product | Parent category, related products, relevant articles | 4–8 |
| Photo | Source product/category, related photos, magazine | 3–5 |
| Editorial | Relevant categories, products, professionals | 3–5 |
| Directory | Categories served, portfolio photos, articles | 3–5 |
| Forum | Related articles, products, categories | 2–4 |

### Orphan Page Elimination
- Generate automatic "Related" modules for every page type.
- Build XML sitemaps and submit to GSC, but do not rely on sitemaps alone for discovery.
- Run weekly crawl comparing sitemap vs. internal link reachability.

## 5. Sitemap Strategy

### Sitemap Index
- One sitemap index per domain.
- Segregate sitemaps by page type:
  - `sitemap-products.xml`
  - `sitemap-categories.xml`
  - `sitemap-photos.xml`
  - `sitemap-editorial.xml`
  - `sitemap-forums.xml`
  - `sitemap-professionals.xml`

### URL Limits
- Keep individual sitemaps under 50,000 URLs / 50MB.
- Use lastmod date from CMS `updated_at`.
- Include only canonical, indexable URLs.

## 6. Performance (Core Web Vitals)

### Template-Level Targets
| Template | LCP Target | Priority |
|----------|-----------|----------|
| Home | ≤ 1.2s | High |
| Category | ≤ 1.5s | High |
| Product | ≤ 1.5s | High |
| Photo gallery | ≤ 2.0s | High |
| Editorial | ≤ 1.5s | Medium |
| Forum | ≤ 2.0s | Medium |

### Tactics
- Lazy-load photos and forum avatars.
- Preload hero image on home/category/editorial.
- Defer non-critical JS on photo-heavy pages.
- Use responsive images with modern formats (WebP/AVIF).

## 7. Internationalization Beyond Hreflang

- Localize title and meta description templates per market.
- Use local currency, units, and spelling.
- Host media on a CDN edge close to each market.
- Ensure local review signals for directory professionals.

---

Built by Rajesh Kumar | Powered by [BrandOps Site](https://www.brandops.site)
