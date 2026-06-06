# Built by Testers Skill

Deep functional/UI/API testing on sites built BY the testing community, FOR the testing community. Measures performance, cost, and LLM interaction complexity across testing platforms created by Jason Arbon, Jason Huggins, Paul Grossman, and other testing leaders.

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

## Creator Sites

| Creator | Site | Category | Ratio | Status |
|---------|------|----------|-------|--------|
| Jason Arbon | testers.ai | General Practice | 4.7× | ✅ Measured |
| Jason Huggins | Test Track | General Practice | 2.1× | ✅ Measured |
| Jason Huggins | var.parts | Automation Testing | 3.8× | ✅ Measured |
| Paul Grossman | Candy Mapper | General Practice | 1.9× | ✅ Measured |
| Parasoft | Parabank | Automation Testing | ~3.0× | ✅ CLI Measured, MCP Pending |

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

## Integration with practice-testing

Both `/built-by-testers` and `/practice-testing` skills use identical measurement methodology (bracket protocol v2).

- **practice-testing:** 100 sites across 5 QA practice categories (breadth)
- **built-by-testers:** 5 sites by testing leaders (depth + learning focus)

Use together for comprehensive automation testing benchmarking.

---

**Status:** 4/5 sites measured CLI (100%) | MCP measurement in progress  
**Last Updated:** 2026-06-05  
**Protocol:** Bracket Protocol v2 (three-bash token isolation)  
**Vibium:** v26.5.31  
