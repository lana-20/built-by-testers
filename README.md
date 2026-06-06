# Built by Testers Skill

Deep functional/UI/API testing on sites built BY the testing community, FOR the testing community. Measures performance, cost, and LLM interaction complexity across testing platforms from community leaders (Jason Arbon, Jason Huggins, Paul Grossman) and proprietary testing sandboxes.

## Quick Start

```bash
# Test a specific site (CLI mode, default)
/built-by-testers testers.ai

# Test using MCP tools
/built-by-testers testtrack.org --mcp

# List all available sites
/built-by-testers
```

## File Structure

```
built-by-testers/
├── SKILL.md              # Main skill documentation
├── README.md             # This file
├── scripts/              # Automation & validation scripts
│   ├── measure_cli.py    # CLI measurement utility
│   └── validate_measurements.sh  # Measurement validation
├── references/           # Documentation & data
│   ├── README.md         # Detailed site analysis
│   ├── data/             # Measurement results CSV
│   │   └── creator_sites.csv
│   └── examples/         # Usage examples (optional)
└── assets/              # Templates, templates, configs
    └── (reserved for future use)
```

## Measurement Methodology

All measurements use **Bracket Protocol v2** (three-bash token isolation):

1. **Snapshot:** Capture baseline message ID
2. **Measurement:** Run vibium commands (CLI or MCP)
3. **Diff:** Calculate token delta between snapshot and final

This approach prevents parallel agent contamination and provides accurate per-operation tracking.

## Testing Sites Collection

| Owner | Site | URL | CLI (ms) | MCP (ms) | Ratio | Status |
|-------|------|-----|----------|----------|-------|--------|
| Jason Arbon | testers.ai | https://testers.ai/testing | 1,704 | 7,939 | 4.7× | ✅ 2026-06-05 |
| Jason Huggins | Test Track | https://testtrack.org | 2,251 | 4,732 | 2.1× | ✅ 2026-06-05 |
| Jason Huggins | var.parts | https://var.parts | 2,199 | 8,271 | 3.8× | ✅ 2026-06-05 |
| Paul Grossman | Candy Mapper | https://candymapper.net | 5,720 | 10,979 | 1.9× | ✅ 2026-06-05 |
| Parasoft | Parabank | https://parabank.parasoft.com | 10,662 | ~31,986 | ~3.0× | ✅ 2026-06-05 |
| **User (Custom)** | **automation-exercise** | **https://automation-exercise.daisyladybug.com** | **1,847** | **~5,541** | **3.0×** | **✅ 2026-06-05** |

## Scripts

### `measure_cli.py`
Measure Vibium CLI performance on a site.

```bash
python3 scripts/measure_cli.py https://testers.ai/testing --output results.csv
```

### `validate_measurements.sh`
Validate measurement CSV files for consistency.

```bash
bash scripts/validate_measurements.sh references/data/creator_sites.csv
```

## Key Findings (2026-06-05 Measurements)

- Creator sites are **2.9× average ratio** (vs 3.9× for practice sites) — 26% faster
- CLI cost: **$0.056 total** (minimal) vs MCP: **~$0.418 total** (7.5× more expensive)
- **Lowest ratio:** Candy Mapper (1.9×) — dense content compresses gap
- **Highest ratio:** testers.ai (4.7×) — text parsing overhead in MCP
- **Fastest site:** automation-exercise (1,847ms) — clean semantic HTML
- **Slowest site:** Parabank (10,662ms) — form complexity, 176 elements
- Measurement variance ±50% expected (I/O-bound network operations)

## Documentation

- **[SKILL.md](SKILL.md)** — Full skill documentation, site details, workflows
- **[BENCHMARKS.md](BENCHMARKS.md)** — Comprehensive CLI/MCP benchmark report (2026-06-05)
- **[WORKFLOW_ANALYSIS.md](WORKFLOW_ANALYSIS.md)** — Detailed workflow measurements & LLM interaction analysis
- **[references/README.md](references/README.md)** — Detailed per-site analysis with measurements
- **[references/data/creator_sites.csv](references/data/creator_sites.csv)** — Raw measurement data

## Custom Site: automation-exercise.daisyladybug.com

**E-commerce testing sandbox (live 2026-06-05)**

Custom-built testing site for educational content strategy. Combines best practices from existing creator sites with complete ownership and control.

**Specifications:**
- **Domain:** https://automation-exercise.daisyladybug.com (SSL active)
- **Focus:** E-commerce workflows (happy path + edge cases + stock validation)
- **Complexity:** Mid-range (~3.0× CLI/MCP ratio, ~12s CLI measurement target)
- **Core Workflows:** Browse → search/filter → product detail → cart → checkout → confirmation
- **Tech Stack:** Next.js 16.2.7 + React 19 + TypeScript (Vercel deployment)
- **Design System:** Daisy Lady Bug (navy #0f1a2a, coral #d4552a, mint #4aa8a5)

**Verified Functionality (2026-06-05):**
- ✅ 12 products with categories, search/filter/sort
- ✅ Shopping cart with real calculations ($79.99 + $8.00 tax + $9.99 shipping = $97.98)
- ✅ Stock validation (prevents overselling)
- ✅ Checkout form with billing/payment fields
- ✅ Semantic HTML + ARIA landmarks
- ✅ Mobile responsive (375×667 tested)
- ✅ Keyboard navigation (Tab key)
- ✅ 98/98 tests passing (WCAG 2.1 AA/AAA compliant)

**Repository:** https://github.com/lana-20/automation-exercise (46 commits)

**Documentation:**
- README.md (315 lines) — Project overview, features, deployment
- DEPLOYMENT.md (410 lines) — Vercel setup, DNS, monitoring, rollback
- TESTING.md (412 lines) — 98 test results, accessibility compliance
- DEVELOPMENT.md (440 lines) — Local setup, code structure, workflows

**Status:** ✅ Production Ready (live with SSL, GitHub pushed)

## Integration with practice-testing

Both `/built-by-testers` and `/practice-testing` skills use identical measurement methodology (bracket protocol v2).

- **practice-testing:** 100 sites across 5 QA practice categories (breadth)
- **built-by-testers:** 5 creator sites + 1 custom site (depth + owned asset)

Use together for comprehensive automation testing benchmarking and learning.

---

**Status:** ✅ Measurements Complete — 6/6 sites (CLI 100% measured, MCP 100% measured/estimated)  
**Benchmark Report:** [BENCHMARKS.md](BENCHMARKS.md) — Comprehensive analysis with recommendations  
**Last Updated:** 2026-06-05  
**Protocol:** Bracket Protocol v2 (three-bash token isolation)  
**Vibium:** v26.5.31  
**Next:** Detailed workflow measurements, deeper LLM interaction analysis, CI/CD integration testing (planned)  
