# Built by Testers — Benchmark Measurements

Comprehensive CLI/MCP performance measurements across 6 automation testing sites using bracket protocol v2.
All measurements on Vibium v26.5.31. Timing variance ±50% expected (I/O-bound operations).

---

## Summary Table

### Run 1 — 2026-06-06 (multi-step workflows)

| Site | CLI (ms) | MCP (ms) | Ratio |
|------|----------|----------|-------|
| testers.ai | 2,251 | 13,592 | **6.0×** |
| testtrack.org | 3,479 | 25,790 | **7.4×** |
| var.parts | 2,130 | 22,827 | **10.7×** |
| candymapper.net | 6,262 | 13,310 | **2.1×** |
| parabank | 4,032 | 30,261 | **7.5×** |
| automation-exercise | 2,202 | 27,947 | **12.7×** |
| **Total** | **20,356** | **133,727** | **avg 7.7×** |

**Workflow depth:** nav+map+interact+verify (multi-step).
**Parabank note (run 1):** john/demo returned "An internal error has occurred" — register page used as fallback.

---

### Run 2 — 2026-06-06 (second pass, same day)

| Site | CLI (ms) | MCP (ms) | Ratio |
|------|----------|----------|-------|
| testers.ai | 960 | 19,663 | **20.5×** |
| testtrack.org | 1,339 | 26,554 | **19.8×** |
| var.parts | 2,445 | 20,318 | **8.3×** |
| candymapper.net | 5,187 | 19,945 | **3.8×** |
| parabank | 2,446 | 25,540 | **10.4×** |
| automation-exercise | 1,583 | 38,807 | **24.5×** |
| **Total** | **13,960** | **150,827** | **avg 11.1×** |

**CLI faster in run 2:** warm daemon cache, not meaningful improvement. Ratios higher because CLI denominator is smaller.
**Parabank note (run 2):** john/demo login succeeded — dashboard with 11 accounts returned (37 elements). Login is intermittent server-side.

---

## Behavioral Observations by Site

### testers.ai (Jason Arbon)

- 59 elements on homepage (category cards + Checklist links)
- Category click navigates to testers.ai homepage (28 elements) — not a sub-category page
- Pure nav site — no forms, no inputs on the testing index page
- CLI and MCP behavior identical — no interaction pattern differences
- Clean DOM, good ratio calibration site

### testtrack.org (Jason Huggins)

- 19 elements on homepage (18 module links + theme toggle)
- Text Input Demo sub-page: 13 elements (6 inputs + textarea + 2 buttons + nav)
- Element count drops from 19 → 13 on sub-page (expected — scoped DOM)
- Dialog pre-stub required before alert-firing modules: `eval 'window.alert=function(){};window.confirm=function(){return true;}'`
- CLI and MCP fill textareas identically (MB7 fixed in v26.5.31)

### var.parts (Jason Huggins)

- 41 elements on shop page (12 products × 2 elements each + 5 nav)
- "Add to Cart" button becomes "In Cart" after click — state change confirmed in map
- Toast notification visible in map output: `[li] "Added to cartVibium Battery Pack"`
- browser_click on Add to Cart works reliably (no obstruction issues)
- CLI and MCP behavior identical on cart state update

### candymapper.net (Paul Grossman)

- 51–54 element count variance (Wix lazy-loads duplicate nav elements)
- County picker (@e16 "Select a County") blocked by overlay in both CLI and MCP — use contact form as fallback
- Contact form fields: @e28 (First name), @e30 (Email) — fill reliably in both modes
- Slow nav dominated by Wix page load (~5s CLI, ~20s MCP) — not interaction overhead
- reCAPTCHA present but skipped (human interaction required)

### parabank (Parasoft)

- Login page: 34 elements consistently
- john/demo login: **intermittent** — server-side issue, not credentials. Retry if "An internal error" appears
- When login succeeds: 37 elements on dashboard, 11 account number links (@e17–@e27)
- BiDi map error may fire after login submit — transient, self-resolves on retry
- Register page (8-field form) works as fallback when login blocked

### automation-exercise (custom)

- Products page: 18 elements (12 product links + 2 selects + 1 search + 3 nav)
- Product detail: 7 elements (3 nav + back + qty − + qty + + Add to Cart)
- Add to Cart confirms via cart count increment and button label "✓ Added to Cart"
- MB10 (browser_click false obstruction) is intermittent — use `browser_evaluate` unconditionally
- CLI `vibium eval` + `vibium map` to verify — same reliable pattern as MCP evaluate

---

## Ratio Interpretation

CLI/MCP ratio is **workflow-depth dependent**:

| Workflow depth | Expected ratio |
|----------------|----------------|
| nav+map only | 2–5× |
| nav+map+click+map | 5–10× |
| nav+map+fill+click+verify | 8–15× |
| nav+map+interact+verify (multi-step) | 10–25× |

High ratios (>15×) indicate MCP inter-turn overhead dominates. CLI executes all commands in a single shell call; MCP has one tool call per action with inter-turn Claude processing time between each.

**candymapper stays low** (2–4×) because Wix page load (~5s) dominates both modes equally — the CLI/MCP overhead is compressed by constant load time.

---

## Measurement Confidence

| Site | CLI | MCP | Notes |
|------|-----|-----|-------|
| testers.ai | ✅ Actual × 2 | ✅ Actual × 2 | Both runs 2026-06-06 |
| testtrack.org | ✅ Actual × 2 | ✅ Actual × 2 | Both runs 2026-06-06 |
| var.parts | ✅ Actual × 2 | ✅ Actual × 2 | Both runs 2026-06-06 |
| candymapper.net | ✅ Actual × 2 | ✅ Actual × 2 | Both runs 2026-06-06 |
| parabank | ✅ Actual × 2 | ✅ Actual × 2 | Both runs 2026-06-06; login intermittent |
| automation-exercise | ✅ Actual × 2 | ✅ Actual × 2 | Both runs 2026-06-06; MB10 workaround used |

**Last updated:** 2026-06-06 · **Vibium:** v26.5.31 · **Protocol:** Bracket v2
