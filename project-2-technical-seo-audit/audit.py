"""
Technical SEO Audit Simulator — 1M+ URL Global Marketplace
Generates a realistic crawl dataset, analyzes issues, prioritizes fixes,
and exports an HTML report.
"""
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

random.seed(42)

# CONFIG
TOTAL_URLS = 1_050_000
DOMAINS = [
    "example.com", "example.co.uk", "example.de", "example.fr",
    "example.com.au", "example.ca", "example.es", "example.it",
    "example.jp", "example.in", "example.mx", "example.br",
    "example.nl", "example.sg"
]

PAGE_TYPES = ["home", "category", "product", "photo", "forum", "editorial", "directory"]
TYPE_WEIGHTS = [0.001, 0.12, 0.45, 0.20, 0.10, 0.08, 0.049]

ISSUE_PROBABILITIES = {
    "orphan": 0.08,
    "noindex": 0.03,
    "duplicate_title": 0.12,
    "missing_meta_description": 0.18,
    "hreflang_missing": 0.15,
    "slow_lcp": 0.22,
    "faceted_duplicate": 0.06,
    "broken_internal_link": 0.04,
    "redirect_chain": 0.03,
    "non_canonical_self": 0.05,
}

SEVERITY = {
    "orphan": "High",
    "noindex": "High",
    "duplicate_title": "Medium",
    "missing_meta_description": "Low",
    "hreflang_missing": "High",
    "slow_lcp": "Medium",
    "faceted_duplicate": "Medium",
    "broken_internal_link": "High",
    "redirect_chain": "Low",
    "non_canonical_self": "Medium",
}

ESTIMATED_IMPACT = {
    "orphan": 45000,
    "noindex": 60000,
    "duplicate_title": 22000,
    "missing_meta_description": 8000,
    "hreflang_missing": 38000,
    "slow_lcp": 15000,
    "faceted_duplicate": 18000,
    "broken_internal_link": 25000,
    "redirect_chain": 5000,
    "non_canonical_self": 14000,
}

ESTIMATED_EFFORT_HOURS = {
    "orphan": 120,
    "noindex": 40,
    "duplicate_title": 80,
    "missing_meta_description": 60,
    "hreflang_missing": 160,
    "slow_lcp": 200,
    "faceted_duplicate": 100,
    "broken_internal_link": 80,
    "redirect_chain": 60,
    "non_canonical_self": 70,
}

def generate_url(index, domain, page_type):
    slug_map = {
        "home": "/",
        "category": f"/category/{page_type}-{index % 18000}",
        "product": f"/product/{page_type}-{index % 350000}",
        "photo": f"/photo/{index % 200000}",
        "forum": f"/discussion/{index % 100000}",
        "editorial": f"/magazine/{page_type}-article-{index % 80000}",
        "directory": f"/professional/{page_type}-{index % 50000}",
    }
    base = f"https://{domain}{slug_map[page_type]}"
    if page_type == "category" and random.random() < 0.3:
        facets = ["color=red", "price=low", "material=wood", "style=modern"]
        base += "?" + "&".join(random.sample(facets, k=random.randint(1, 3)))
    return base

def simulate_crawl():
    urls = []
    issues_by_url = defaultdict(list)

    for i in range(TOTAL_URLS):
        domain = DOMAINS[i % len(DOMAINS)]
        page_type = random.choices(PAGE_TYPES, weights=TYPE_WEIGHTS)[0]
        url = generate_url(i, domain, page_type)

        url_issues = []
        for issue, prob in ISSUE_PROBABILITIES.items():
            # Increase probability for certain types
            if issue == "hreflang_missing" and domain != "example.com":
                prob = 0.55
            if issue == "slow_lcp" and page_type in ["photo", "editorial"]:
                prob = 0.35
            if issue == "faceted_duplicate" and page_type == "category":
                prob = 0.35
            if random.random() < prob:
                url_issues.append(issue)

        if url_issues:
            issues_by_url[url] = url_issues

        urls.append({
            "url": url,
            "domain": domain,
            "type": page_type,
            "issues": url_issues,
        })

    return urls, issues_by_url

def analyze(urls, issues_by_url):
    total = len(urls)
    issue_counts = Counter()
    issue_by_type = defaultdict(Counter)
    issue_by_domain = defaultdict(Counter)

    for u in urls:
        for issue in u["issues"]:
            issue_counts[issue] += 1
            issue_by_type[u["type"]][issue] += 1
            issue_by_domain[u["domain"]][issue] += 1

    # Priority score = impact / effort
    priority = []
    for issue, count in issue_counts.items():
        impact = ESTIMATED_IMPACT[issue] * count
        effort = ESTIMATED_EFFORT_HOURS[issue]
        roi = round(impact / effort, 2)
        priority.append({
            "issue": issue,
            "count": count,
            "pct": round(count / total * 100, 2),
            "severity": SEVERITY[issue],
            "impact": impact,
            "effort_hours": effort,
            "roi_score": roi,
        })

    priority.sort(key=lambda x: (-x["roi_score"], -x["count"]))

    return {
        "total_urls": total,
        "issue_counts": issue_counts,
        "issue_by_type": dict(issue_by_type),
        "issue_by_domain": dict(issue_by_domain),
        "priority": priority,
    }

def export_sample_csv(urls, path="sample_crawl.csv", n=100000):
    import csv
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["url", "domain", "type", "issues"])
        for u in urls[:n]:
            writer.writerow([u["url"], u["domain"], u["type"], "|".join(u["issues"])])

def main():
    out_dir = Path("results")
    out_dir.mkdir(exist_ok=True)

    print("Simulating crawl of", TOTAL_URLS, "URLs across", len(DOMAINS), "domains...")
    urls, issues_by_url = simulate_crawl()

    print("Analyzing issues...")
    results = analyze(urls, issues_by_url)

    # Save JSON results
    with open(out_dir / "audit_results.json", "w") as f:
        json.dump(results, f, indent=2)

    # Export sample CSV
    export_sample_csv(urls, out_dir / "sample_crawl.csv")

    # Priority table
    print("\nPriority Backlog (ROI-sorted):")
    print(f"{'Issue':<22} {'Count':<10} {'%':<6} {'Severity':<8} {'ROI':<8}")
    print("-" * 60)
    for p in results["priority"]:
        print(f"{p['issue']:<22} {p['count']:<10,} {p['pct']:<6.2f} {p['severity']:<8} {p['roi_score']:<8.1f}")

    print("\nResults saved to:", out_dir)

if __name__ == "__main__":
    main()
