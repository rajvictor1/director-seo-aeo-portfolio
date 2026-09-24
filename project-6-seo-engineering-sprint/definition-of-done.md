# Definition of Done — SEO Engineering Sprint

A ticket is only marked **Done** when all of the following are true:

## Technical
- [ ] Code is reviewed and merged to `main`.
- [ ] Feature is deployed to staging and production.
- [ ] No console errors or failed tests introduced.

## SEO Validation
- [ ] Schema markup passes Google's Rich Results Test or Schema Markup Validator (where applicable).
- [ ] Changes are validated on staging using a representative crawl sample.
- [ ] No new 404s, 5xx errors, redirect chains, or canonical errors introduced.
- [ ] Internal linking changes do not create orphan pages.

## Performance
- [ ] Core Web Vitals (LCP, INP, CLS) do not regress on affected templates.
- [ ] Mobile and desktop Lighthouse scores remain stable or improve.

## Sign-off
- [ ] Product Manager has reviewed and approved the change.
- [ ] SEO Lead (you) has confirmed the fix resolves the stated problem.
- [ ] QA has validated acceptance criteria.

## Documentation
- [ ] Runbook or CMS guide updated if the change affects content creators.
- [ ] Any new components are documented in the design system or component library.

---

Built by Rajesh Kumar | Powered by [BrandOps Site](https://www.brandops.site)
