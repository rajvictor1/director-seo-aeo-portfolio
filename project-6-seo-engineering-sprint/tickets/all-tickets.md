# Ticket SEO-101 — Fix Canonical Self-Reference on Product Pages

**Type:** Bug  
**Priority:** P0  
**Story Points:** 3  
**Assignee:** Backend Engineer  
**Reporter:** Director of SEO  

## Problem
Approximately 52,000 product pages are using non-canonical URLs in their `rel="canonical"` tag, pointing to URLs with session IDs, tracking parameters, or sort parameters. This splits ranking signals and wastes crawl budget.

## Acceptance Criteria
- [ ] Every product page canonical URL matches the clean, parameter-free URL.
- [ ] Canonical tags are generated server-side, not injected via JS.
- [ ] A whitelist of allowed parameters (e.g., `?color=`) is documented.
- [ ] Existing canonical errors are reduced to < 1% in the next crawl.

## Implementation Notes
- Update canonical helper in product template.
- Strip `session_id`, `utm_*`, `sort`, `ref` parameters.
- Add unit tests for canonical helper.

## Definition of Done
- Code reviewed and merged.
- Schema/Rich Results Test: N/A.
- Crawl validation: < 1% canonical error rate.
- No CWV regression.

---

# Ticket SEO-102 — Add Article Schema to Editorial Template

**Type:** Feature  
**Priority:** P0  
**Story Points:** 5  
**Assignee:** Frontend Engineer  
**Reporter:** Director of SEO  

## Problem
Editorial articles lack structured data, missing rich result opportunities in Google and citation signals for AI search engines.

## Acceptance Criteria
- [ ] `Article` schema is rendered on every article page.
- [ ] Required fields: `headline`, `author` (Person/Organization), `datePublished`, `dateModified`, `image`, `publisher`, `description`.
- [ ] Fallbacks exist for missing fields without breaking markup.
- [ ] Schema is validated in Rich Results Test for 50 sample articles.

## Implementation Notes
- Build reusable `ArticleSchema` component.
- Pull author info from CMS `author` relation.
- Use article hero image as `image` value.

## Definition of Done
- Component merged and deployed to 100% of article pages.
- 50 sample pages pass Rich Results Test.
- No invalid markup errors in GSC.

---

# Ticket SEO-103 — Implement FAQPage Schema Block for AEO Content

**Type:** Feature  
**Priority:** P0  
**Story Points:** 5  
**Assignee:** Frontend Engineer + CMS  
**Reporter:** Director of SEO  

## Problem
Comparison and capability pages are not marked up as FAQ pages, reducing their chance of being cited in AI search answers and featured snippets.

## Acceptance Criteria
- [ ] CMS supports an FAQ block content type.
- [ ] FAQ block renders visible HTML question/answer pairs.
- [ ] `FAQPage` JSON-LD is auto-generated from the FAQ block.
- [ ] FAQ block can be added to comparison, category, and editorial pages.
- [ ] 20 high-priority pages receive FAQ blocks in this sprint.

## Implementation Notes
- Extend CMS with FAQ collection type.
- Build frontend FAQ component with schema output.
- Validate no duplicate question text on same page.

## Definition of Done
- FAQ component merged.
- 20 target pages published with FAQ blocks.
- All 20 pass Rich Results Test.

---

# Ticket SEO-104 — Improve LCP on Photo Gallery Pages

**Type:** Performance  
**Priority:** P0  
**Story Points:** 8  
**Assignee:** Frontend Engineer + CDN  
**Reporter:** Director of SEO  

## Problem
Photo gallery pages have LCP > 4s on mobile, primarily due to unoptimized hero images and render-blocking JS. This impacts rankings and user experience.

## Acceptance Criteria
- [ ] Mobile LCP on photo gallery pages < 2.0s for 75th percentile.
- [ ] Hero images are served in WebP/AVIF with responsive `srcset`.
- [ ] Non-critical JS is deferred.
- [ ] Preload hint added for hero image.

## Implementation Notes
- Use image CDN transformation URLs.
- Audit with Lighthouse and WebPageTest.
- Monitor CrUX data after release.

## Definition of Done
- LCP target met in Lighthouse for 10 sample pages.
- No visual regression on desktop/mobile.
- CrUX regression alert does not fire.

---

# Ticket SEO-105 — Add BreadcrumbList Schema to Category Pages

**Type:** Feature  
**Priority:** P1  
**Story Points:** 3  
**Assignee:** Frontend Engineer  
**Reporter:** Director of SEO  

## Problem
Category pages lack breadcrumb structured data, missing a rich result opportunity and reducing contextual clarity for crawlers.

## Acceptance Criteria
- [ ] `BreadcrumbList` schema is rendered on all category pages.
- [ ] Visible breadcrumb navigation matches schema.
- [ ] Schema includes `Home`, `Category root`, and current category.

## Implementation Notes
- Reuse existing breadcrumb UI if present.
- Build `BreadcrumbSchema` component from page context.

## Definition of Done
- Deployed to all category pages.
- Rich Results Test passes for sample.
- Breadcrumb errors in GSC = 0.

---

# Ticket SEO-106 — Build Internal Link Module for Related Professionals

**Type:** Feature  
**Priority:** P1  
**Story Points:** 5  
**Assignee:** Backend Engineer + Data  
**Reporter:** Director of SEO  

## Problem
Professional directory profile pages are orphans or have weak internal linking, hurting crawlability and ranking for local service queries.

## Acceptance Criteria
- [ ] Every professional profile page links to 3–6 related professionals.
- [ ] Related professionals are selected by service type + location proximity.
- [ ] Module is server-rendered.
- [ ] Links use descriptive anchor text.

## Implementation Notes
- Query related professionals by `service_type` and `city_id`.
- Exclude profiles with noindex or low review count.

## Definition of Done
- Module live on all profile pages.
- Orphan page count reduced by 20% in crawl.
- No broken internal links introduced.

---

# Ticket SEO-107 — Create XML Sitemap for Forum Threads

**Type:** Feature  
**Priority:** P1  
**Story Points:** 5  
**Assignee:** Backend Engineer  
**Reporter:** Director of SEO  

## Problem
Forum threads are under-indexed because they are not included in any XML sitemap, relying only on internal links for discovery.

## Acceptance Criteria
- [ ] A dedicated `sitemap-forums.xml` is generated daily.
- [ ] Only canonical, indexable, non-thin threads are included.
- [ ] Sitemap is referenced from the sitemap index.
- [ ] URLs include `lastmod` from thread `updated_at`.

## Implementation Notes
- Add forum sitemap generation to existing sitemap job.
- Filter threads by word count and noindex flag.

## Definition of Done
- Sitemap submitted to GSC.
- Coverage report shows submitted URLs within 7 days.
- No increase in 5xx errors.

---

# Ticket SEO-108 — Fix Redirect Chains Over 2 Hops

**Type:** Bug  
**Priority:** P1  
**Story Points:** 3  
**Assignee:** Backend Engineer  
**Reporter:** Director of SEO  

## Problem
Crawl data shows 31,400 URLs with redirect chains longer than 2 hops, wasting crawl budget and diluting ranking signals.

## Acceptance Criteria
- [ ] All redirect chains reduced to ≤ 2 hops.
- [ ] Target is single redirect for 95% of affected URLs.
- [ ] Internal links updated to point to final URLs.

## Implementation Notes
- Export redirect chain report from crawl data.
- Update redirect rules in CDN / app layer.
- Fix source internal links in bulk.

## Definition of Done
- Re-crawl confirms < 1% of URLs have chains > 2 hops.
- No 404s created by redirect changes.

---

# Ticket SEO-109 — Add Noindex Flag for Thin Forum Threads

**Type:** Feature  
**Priority:** P1  
**Story Points:** 3  
**Assignee:** Backend Engineer  
**Reporter:** Director of SEO  

## Problem
Low-quality forum threads with < 100 words of useful content dilute the site's topical authority and consume crawl budget.

## Acceptance Criteria
- [ ] Threads with < 100 words of useful content receive `noindex`.
- [ ] Rule applies only to threads older than 90 days.
- [ ] Noindex flag is reversible via moderator action.
- [ ] 80,000 thin threads are noindexed in this sprint.

## Implementation Notes
- Compute useful word count excluding signatures and quoted text.
- Add `noindex` flag in thread meta template.

## Definition of Done
- 80K thin threads noindexed.
- GSC coverage report confirms reduction in indexed thin content.
- No high-value threads accidentally noindexed.

---

# Ticket SEO-110 — Roll Out ImageObject Schema on Photo Detail Pages

**Type:** Feature  
**Priority:** P2  
**Story Points:** 5  
**Assignee:** Frontend Engineer  
**Reporter:** Director of SEO  

## Problem
Photo detail pages lack image structured data, reducing visibility in Google Images and visual search engines.

## Acceptance Criteria
- [ ] `ImageObject` schema on every photo detail page.
- [ ] Fields: `contentUrl`, `name`, `description`, `author`, `datePublished`, `license`, `keywords`.
- [ ] `ImageGallery` schema on collection pages.
- [ ] Image sitemap updated to include photo pages.

## Implementation Notes
- Use existing photo metadata for schema fields.
- Build reusable `ImageObjectSchema` component.

## Definition of Done
- Photo pages pass Rich Results Test sample.
- Image sitemap includes photo URLs.
- No CWV regression.

---

# Ticket SEO-111 — Implement Hreflang Self-Referencing on All Market Domains

**Type:** Feature  
**Priority:** P2  
**Story Points:** 8  
**Assignee:** Backend Engineer + International PM  
**Reporter:** Director of SEO  

## Problem
Non-US market pages are missing hreflang annotations, causing Google to serve wrong regional versions and suppressing international organic traffic.

## Acceptance Criteria
- [ ] Every canonical page includes self-referencing hreflang.
- [ ] Equivalent pages across 14 domains are cross-linked via hreflang.
- [ ] `x-default` points to `example.com` version.
- [ ] Hreflang is included in both `<head>` and XML sitemaps.
- [ ] No return-tag errors in next crawl.

## Implementation Notes
- Add `page_uuid` to link equivalents across markets.
- Build hreflang generation service.
- Coordinate release across all 14 domains.

## Definition of Done
- Deployed to all domains.
- Hreflang error count in GSC = 0.
- No ranking cannibalization observed.

---

# Ticket SEO-112 — Build SEO Health Check Dashboard Endpoint

**Type:** Feature  
**Priority:** P2  
**Story Points:** 5  
**Assignee:** Backend Engineer  
**Reporter:** Director of SEO  

## Problem
SEO issues are discovered reactively via periodic crawls. We need a real-time health dashboard to catch regressions immediately after deploys.

## Acceptance Criteria
- [ ] New internal endpoint returns JSON with daily counts for:
  - canonical errors
  - noindexable pages
  - pages missing schema
  - 5xx/4xx errors
  - orphan pages
- [ ] Endpoint is queryable by domain and page type.
- [ ] Dashboard is accessible to SEO, Product, and Engineering.

## Implementation Notes
- Read from existing crawl + log data.
- Build lightweight aggregation query.
- Add basic alerting threshold.

## Definition of Done
- Endpoint live and documented.
- Dashboard accessible.
- Alerts trigger on canonical error spike.

---

Built by Rajesh Kumar | Powered by [BrandOps Site](https://www.brandops.site)
