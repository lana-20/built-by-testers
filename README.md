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
| **You** | **automation-exercise** | **automation-exercise.daisyladybug.com** | **Automation Testing** | **~3.0× (target)** | **📋 Planning** |

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

**E-commerce testing sandbox (in development)**

Custom-built testing site for educational content strategy. Combines best practices from existing creator sites with complete ownership and control.

**Specifications:**
- **Focus:** E-commerce workflows (happy path + edge cases + negative scenarios)
- **Complexity Target:** Mid-range (~3.0× CLI/MCP ratio, ~12s CLI)
- **Core Workflows:** Browse → search → product detail → cart → checkout
- **Tech Stack:** TBD (Next.js or static HTML+JS)
- **Design System:** Daisy Lady Bug (via `/dlb-page` skill)

**Build Phases:**
1. Design & specification (workflow diagrams, test scenarios)
2. Implementation (frontend + backend if needed)
3. Deploy to daisyladybug.com + measure (CLI + MCP)
4. Add to collection

**Status:** Planning phase (design in progress)

## Integration with practice-testing

Both `/built-by-testers` and `/practice-testing` skills use identical measurement methodology (bracket protocol v2).

- **practice-testing:** 100 sites across 5 QA practice categories (breadth)
- **built-by-testers:** 5 creator sites + 1 custom site (depth + owned asset)

Use together for comprehensive automation testing benchmarking and learning.

---

**Status:** 5/6 sites (4 creator CLI 100% measured, 1 MCP pending, 1 custom in planning)  
**Last Updated:** 2026-06-05  
**Protocol:** Bracket Protocol v2 (three-bash token isolation)  
**Vibium:** v26.5.31  
**Next:** automation-exercise design phase  
