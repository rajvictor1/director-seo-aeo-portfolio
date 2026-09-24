# Project 6 — SEO Engineering Sprint Simulation

## Executive Summary

This project simulates a 2-week SEO engineering sprint for a global marketplace. It includes a full backlog of realistic SEO tickets, a RACI chart, Definition of Done, sprint planning one-pager, and a retro template.

The artifact demonstrates Director-level SEO product management: translating SEO strategy into engineering work, partnering with PMs, and running agile execution.

---

## Sprint Goal

Improve technical SEO health and AI-search readiness by resolving canonical issues, rolling out schema markup, improving Core Web Vitals, and launching AEO-friendly FAQ blocks on high-traffic page templates.

---

## Sprint Backlog

| ID | Ticket | Type | Priority | Story Points | Status |
|----|--------|------|----------|--------------|--------|
| SEO-101 | Fix canonical self-reference on product pages | Bug | P0 | 3 | To Do |
| SEO-102 | Add Article schema to editorial template | Feature | P0 | 5 | To Do |
| SEO-103 | Implement FAQPage schema block for AEO content | Feature | P0 | 5 | To Do |
| SEO-104 | Improve LCP on photo gallery pages | Performance | P0 | 8 | To Do |
| SEO-105 | Add BreadcrumbList schema to category pages | Feature | P1 | 3 | To Do |
| SEO-106 | Build internal link module for related professionals | Feature | P1 | 5 | To Do |
| SEO-107 | Create XML sitemap for forum threads | Feature | P1 | 5 | To Do |
| SEO-108 | Fix redirect chains over 2 hops | Bug | P1 | 3 | To Do |
| SEO-109 | Add noindex flag for thin forum threads | Feature | P1 | 3 | To Do |
| SEO-110 | Roll out ImageObject schema on photo detail pages | Feature | P2 | 5 | To Do |
| SEO-111 | Implement hreflang self-referencing on all market domains | Feature | P2 | 8 | To Do |
| SEO-112 | Build SEO health check dashboard endpoint | Feature | P2 | 5 | To Do |

Full ticket details: [`tickets/`](tickets/)

---

## RACI

| Activity | SEO (You) | Product | Engineering | Design | QA |
|----------|-----------|---------|-------------|--------|-----|
| Backlog prioritization | A | C | C | I | I |
| Ticket writing | A | C | R | I | I |
| Schema implementation | A | I | R | C | R |
| Performance fixes | A | C | R | I | R |
| QA / validation | A | I | C | I | R |
| Release communication | A | C | C | I | I |

**R = Responsible, A = Accountable, C = Consulted, I = Informed**

---

## Definition of Done

A ticket is only "Done" when:
- [ ] Code is reviewed and merged to `main`.
- [ ] Schema markup passes Google's Rich Results Test (where applicable).
- [ ] Changes are validated on staging with a crawl sample.
- [ ] No new 404s, redirect chains, or canonical errors introduced.
- [ ] Core Web Vitals regressions are ruled out.
- [ ] Product Manager and SEO Lead sign off.
- [ ] Documentation / runbook updated if needed.

---

## Sprint Planning One-Pager

### Capacity
- Engineering team: 2 backend, 1 frontend, 1 QA
- Total capacity: 55 story points
- Committed scope: 53 story points

### Risks
- Schema rollout may conflict with existing JSON-LD; require CMS migration.
- LCP fix on photo pages depends on CDN image format rollout.
- Hreflang change touches all 14 domains; needs coordinated release.

### Release Plan
- Day 1–5: Bugs and small schema tickets.
- Day 6–8: FAQ block and internal link module.
- Day 9–10: Performance + QA / staging validation.
- Day 10 release with SEO regression check.

---

## Sprint Retro Template

### What Went Well
- _

### What Could Improve
- _

### Action Items
| Item | Owner | Due |
|------|-------|-----|
| _ | _ | _ |

---

## Files in This Project

| File | Purpose |
|------|---------|
| [`README.md`](README.md) | Sprint overview |
| [`tickets/`](tickets/) | 12 detailed SEO engineering tickets |
| [`raci.md`](raci.md) | Full RACI matrix |
| [`definition-of-done.md`](definition-of-done.md) | Definition of Done |
| [`sprint-planning.md`](sprint-planning.md) | Planning one-pager |
| [`retro-template.md`](retro-template.md) | Sprint retro template |

---

*Built as a Director of SEO & AEO portfolio piece.*

Built by Rajesh Kumar | Powered by [BrandOps Site](https://www.brandops.site)
