# SEO Product Brief — Forums & Discussions

## 1. Problem

Forums and discussions contain valuable user-generated content that captures long-tail questions. However, they are underperforming because:
- Thread titles are user-written and often vague.
- Duplicate and thin content is common (short answers, follow-up questions).
- Pagination and parameterized URLs create crawl bloat.
- E-E-A-T signals (author reputation, moderation) are not visible to crawlers.
- Canonicalization is inconsistent across thread pages.

Estimated opportunity: 25–40% organic traffic increase to forum pages after governance fixes.

---

## 2. Hypothesis

If we improve thread titles, canonicalize pagination, surface author authority signals, and prune low-quality threads, then forum pages will rank for more long-tail questions and appear as cited sources in AI search answers.

---

## 3. Acceptance Criteria

- [ ] Thread pages have canonical URLs without pagination parameters.
- [ ] Paginated replies use `rel="canonical"` to page 1 or a "view all" canonical strategy.
- [ ] Top contributors receive `Person` schema with `name`, `url`, `image`, `jobTitle`, `knowsAbout`.
- [ ] Question / answer threads implement `QAPage` schema with `acceptedAnswer` where applicable.
- [ ] Threads with fewer than 100 words of useful content are noindexed after 90 days.
- [ ] Duplicate threads (same question) are merged and 301 redirected.
- [ ] Internal links from editorial articles to relevant forum threads are added at scale.
- [ ] Forum URLs are included in a dedicated XML sitemap.

---

## 4. Engineering Tasks

### Backend
- Build thread title suggestion model using question extraction.
- Implement canonical logic for pagination and sort parameters.
- Add noindex flag for thin threads.
- Create thread merge tool for moderators.

### Frontend
- Add QAPage / Person JSON-LD markup.
- Render top contributor badges and authority signals.
- Add "Related threads" and "Related articles" modules.

### Content / Moderation
- Define thin-content threshold and auto-noindex rules.
- Train moderators on merge and redirect workflow.

---

## 5. Success Metrics

| Metric | Baseline | Target (90 days) |
|--------|----------|------------------|
| Forum organic sessions | 110,000/mo | 150,000/mo |
| Indexed forum threads | 520,000 | 620,000 |
| Thin/noindexed threads | — | 80,000 pruned |
| QAPage rich results | 0 | 25,000/mo |
| Long-tail keyword rankings (positions 1–10) | 18,000 | 28,000 |

---

## 6. Dependencies

- **Community:** moderator training and merge workflow.
- **ML / Data:** title suggestion model.
- **Legal:** UGC content policy compliance.

---

## 7. Risks

- Aggressive noindexing could remove useful content; review thresholds carefully.
- Forum content can attract spam; moderation must scale with traffic growth.
- QAPage markup errors could trigger manual actions; validate strictly.

---

Built by Rajesh Kumar | Powered by [BrandOps Site](https://www.brandops.site)
