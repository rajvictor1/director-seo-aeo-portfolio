# SEO Product Brief — Photo Inspiration

## 1. Problem

The Photo inspiration section is a high-engagement visual discovery surface. It currently underperforms in image search and visual AI search because:
- Alt text is missing on ~60% of images.
- Image file names are auto-generated IDs, not descriptive.
- Structured data for `ImageObject` and `ImageGallery` is absent.
- Photo detail pages have thin textual context.
- Image sitemaps are not submitted to Google.

Estimated opportunity: image search traffic could grow 40–60% and support category / professional discovery.

---

## 2. Hypothesis

If we improve image metadata, add structured data, and enrich photo pages with descriptive context and related photos, then Google Images and visual search engines will surface our photos for high-intent queries and drive more sessions to category and directory pages.

---

## 3. Acceptance Criteria

- [ ] Every image has descriptive alt text (under 125 characters, sentence-style).
- [ ] Image file names use descriptive slugs (`modern-living-room-grey-sofa.jpg`).
- [ ] `ImageObject` schema is present on every photo detail page with `contentUrl`, `name`, `description`, `author`, `datePublished`, `license`, and `keywords`.
- [ ] `ImageGallery` schema is implemented on collection / room pages.
- [ ] Each photo detail page has 150+ words of descriptive context (room type, style, colors, materials, source credit).
- [ ] Related photos module links 6–12 relevant photos.
- [ ] Image XML sitemap is generated and submitted to Google Search Console.
- [ ] Images are served in WebP/AVIF with responsive `srcset`.

---

## 4. Engineering Tasks

### Backend
- Build alt-text generator using image tags, room type, style, and color.
- Store descriptive file names on upload; rename legacy images in batches.
- Add ImageObject schema fields to photo CMS.
- Generate image sitemap daily.

### Frontend
- Render `ImageObject` + `ImageGallery` JSON-LD in `<head>`.
- Implement lazy loading with native `loading="lazy"`.
- Add "Related photos" and "Save to idea board" modules.
- Add captions and source attribution below images.

### Media Pipeline
- Serve WebP by default, AVIF for supported browsers.
- Add responsive `srcset` for common breakpoints.

---

## 5. Success Metrics

| Metric | Baseline | Target (90 days) |
|--------|----------|------------------|
| Google Images sessions | 45,000/mo | 72,000/mo |
| Photo detail page organic sessions | 60,000/mo | 90,000/mo |
| Images with alt text | 40% | 95% |
| Image sitemap indexed ratio | — | 80% |
| Photo → category page CTR | 8% | 12% |

---

## 6. Dependencies

- **Design:** photo detail page layout with caption area.
- **Content:** alt-text style guide and keyword taxonomy.
- **Legal:** image licensing metadata requirements.

---

## 7. Risks

- Alt-text generation at scale may produce low-quality text; require human QA on top 10K images first.
- Image-heavy pages can hurt LCP; must pair with lazy loading and CDN optimization.

---

Built by Rajesh Kumar | Powered by [BrandOps Site](https://www.brandops.site)
