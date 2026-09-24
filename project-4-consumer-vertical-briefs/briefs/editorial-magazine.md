# SEO Product Brief — Editorial Magazine

## 1. Problem

The Editorial Magazine is the authority and topical cluster hub for the marketplace. It currently:
- Lacks consistent Article schema.
- Has weak internal linking to category and product pages.
- Publishes standalone articles without supporting cluster content.
- Does not target AI-search question formats.
- Has outdated content that is not refreshed or redirected.

Estimated opportunity: 30–50% organic traffic increase by turning the magazine into a structured content engine.

---

## 2. Hypothesis

If we restructure editorial content into topic clusters with `Article` schema, internal links to transactional pages, and AEO-friendly question-answer formatting, then magazine pages will rank for more informational and comparison queries and pass more qualified traffic to category and directory pages.

---

## 3. Acceptance Criteria

- [ ] Every article uses `Article` schema with `headline`, `author`, `datePublished`, `dateModified`, `image`, `publisher`, `description`.
- [ ] Each article belongs to a topic cluster with a pillar page.
- [ ] Every article links internally to 3–7 relevant category / product / directory pages.
- [ ] Articles target AI-search questions with H2/H3 mirror format and direct answers.
- [ ] Pillar pages include FAQPage schema for cluster questions.
- [ ] Articles older than 12 months are reviewed quarterly; outdated articles are refreshed or 301 redirected.
- [ ] Editorial XML sitemap is segmented by topic cluster.

---

## 4. Engineering Tasks

### Backend
- Add topic cluster taxonomy to CMS.
- Auto-generate Article schema from CMS fields.
- Build internal link recommendation engine based on topic similarity.
- Add content review workflow with aging alerts.

### Frontend
- Implement pillar page template with cluster navigation.
- Add FAQPage schema component.
- Add "Related articles" and "Shop the look" modules.
- Ensure article pages pass Core Web Vitals.

### Content
- Define 10 core topic clusters (e.g., kitchen design, bathroom renovation, home office).
- Create editorial brief templates with AEO question targets.

---

## 5. Success Metrics

| Metric | Baseline | Target (90 days) |
|--------|----------|------------------|
| Editorial organic sessions | 95,000/mo | 140,000/mo |
| Indexed articles | 42,000 | 50,000 |
| Avg ranking for target queries | Position 12 | Position 7 |
| Article → category page CTR | 4% | 7% |
| Articles in top 3 positions | 3,200 | 5,500 |

---

## 6. Dependencies

- **Editorial team:** cluster briefs and refresh workflow.
- **Design:** pillar page template and article layout.
- **Product:** internal link module integration.

---

## 7. Risks

- Topic clusters require ongoing content commitment; plan editorial calendar before launch.
- Over-optimization of internal links can appear manipulative; keep them contextually relevant.

---

Built by Rajesh Kumar | Powered by [BrandOps Site](https://www.brandops.site)
