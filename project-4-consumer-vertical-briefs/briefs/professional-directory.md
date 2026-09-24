# SEO Product Brief — Professional Directory

## 1. Problem

The Professional Directory is the primary monetization surface for the marketplace. Today, individual professional profile pages underperform in organic search because:
- Page titles are auto-generated and keyword-poor.
- Structured data for local businesses / service providers is missing.
- Profile pages have weak internal linking from category and editorial pages.
- Review content is not surfaced in HTML for crawlers.
- Geo-modifiers are inconsistent across markets.

Estimated organic opportunity: 35–50% traffic increase to directory pages within 90 days.

---

## 2. Hypothesis

If we optimize professional profile pages with entity-rich structured data, localized titles, and stronger internal links, then Google will rank these pages higher for "{service} + {location}" queries and drive more qualified leads to professionals.

---

## 3. Acceptance Criteria

- [ ] Every professional profile page has a unique, descriptive `<title>` following the template: `{Profession Name} in {City} — {Company Name} | Marketplace`.
- [ ] Every profile page has a unique, useful meta description (150–160 characters) summarizing services, location, and reviews.
- [ ] `LocalBusiness` or `Service` schema is implemented with: `@id`, `name`, `url`, `telephone`, `address`, `geo`, `aggregateRating`, `review` array, `priceRange`, `areaServed`.
- [ ] BreadcrumbList markup is present on profile pages.
- [ ] Review text is rendered in HTML (not loaded only via JS).
- [ ] Each profile page is linked from at least 3 other indexable pages (category, related professionals, editorial).
- [ ] Geo-landing pages (`/professionals/{service}/{city}/`) exist for top 200 service + city combinations.

---

## 4. Engineering Tasks

### Backend
- Add SEO fields to professional profile CMS.
- Build title/meta description generator with override capability.
- Expose review data in server-rendered HTML.
- Generate geo-landing pages from service + city taxonomy.

### Frontend
- Implement LocalBusiness schema component.
- Add BreadcrumbList component to profile template.
- Build "Related professionals" and "Also viewed" modules.
- Ensure profile pages pass Core Web Vitals (LCP < 1.5s).

### Data
- Create service + city taxonomy (top 200 combos).
- Identify internal linking opportunities from category and editorial pages.

---

## 5. Success Metrics

| Metric | Baseline | Target (90 days) |
|--------|----------|------------------|
| Directory organic sessions | 85,000/mo | 120,000/mo |
| Avg ranking for "{service} in {city}" | Position 14 | Position 8 |
| Indexed profile pages | 320,000 | 400,000 |
| Rich result appearances | 0 | 15,000/mo |
| Profile-page leads | 4,200/mo | 5,800/mo |

---

## 6. Dependencies

- **Design:** profile page redesign for review prominence.
- **Content:** taxonomy curation for services and cities.
- **Product:** lead attribution model to connect SEO traffic to leads.
- **PR:** review acquisition campaign to increase review volume.

---

## 7. Risks

- Schema markup errors could cause rich result loss; validate before release.
- Geo-landing pages may compete with category pages; canonical and internal link strategy must be clear.
- Review content moderation must remain strict to avoid UGC policy issues.

---

Built by Rajesh Kumar | Powered by [BrandOps Site](https://www.brandops.site)
