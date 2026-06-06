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

| Owner | Site | URL | Category | Ratio | Status |
|-------|------|-----|----------|-------|--------|
| Jason Arbon | testers.ai | https://testers.ai/testing | General Practice | 4.7× | ✅ Measured |
| Jason Huggins | Test Track | https://testtrack.org | General Practice | 2.1× | ✅ Measured |
| Jason Huggins | var.parts | https://var.parts | Automation Testing | 3.8× | ✅ Measured |
| Paul Grossman | Candy Mapper | https://candymapper.net | General Practice | 1.9× | ✅ Measured |
| Parasoft | Parabank | https://parabank.parasoft.com | Automation Testing | ~3.0× | ✅ CLI Measured, MCP Pending |
| **User (Custom)** | **automation-exercise** | **https://automation-exercise.daisyladybug.com** | **Automation Testing** | **~3.0×** | **✅ Live (CLI tested)** |

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

## Key Findings

- Creator sites are **2.7× faster** than practice sites (3.9× overall ratio)
- CLI requires **7.0× fewer turns** than MCP (164 vs 1,146 turns across creators)
- Parabank is ideal for banking/finance domain testing
- Measurement variance ±50% expected (I/O-bound operations)

## Documentation

- **[SKILL.md](SKILL.md)** — Full skill documentation, site details, workflows
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

**Status:** 6/6 sites (5 creator CLI 100% measured, MCP pending, automation-exercise live + tested)  
**Last Updated:** 2026-06-05  
**Protocol:** Bracket Protocol v2 (three-bash token isolation)  
**Vibium:** v26.5.31  
**Next:** CLI/MCP benchmark measurements on automation-exercise  
