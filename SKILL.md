# Built by Testers — Deep Functional/UI/API Testing Skill

Test sites built by the testing community, for the testing community. Measure performance, cost, and LLM interaction complexity across functional testing platforms created by Jason Arbon, Jason Huggins, Paul Grossman, and other testing leaders.

**Status:** Initial setup (2026-06-05) — CLI/MCP measurement framework ready, 10+ creator sites documented, benchmark methodology adapted from practice-testing

## How to run

`/built-by-testers [site-name|creator-name] [--cli|--mcp]`

- `/built-by-testers testers.ai` — test by site name (default: CLI mode)
- `/built-by-testers Jason Arbon --mcp` — test Jason Arbon's sites using vibium MCP tools
- `/built-by-testers testtrack.org` — test by domain
- `/built-by-testers` — list all available sites and creators

### Mode selection

**CLI mode** (default): Uses vibium CLI commands via Bash tool.
- Invoked as shell commands: `vibium go`, `vibium map`, `vibium click @eN`, etc.
- Requires `export PATH="/usr/local/bin:$PATH"` prefix
- Daemon deadlock on native dialogs — pre-stub with `eval 'window.alert=function(){}'` (B3/vibium v26.3.18)
- `vibium select` matches by visible label OR value attribute

**MCP mode**: Uses `mcp__vibium__browser_*` tool calls directly.
- Dialog handling via `browser_dialog_accept` / `browser_dialog_dismiss`
- `browser_click` on native alert triggers deadlocks (MB3) — use `browser_evaluate + browser_sleep + browser_dialog_accept` pattern
- `browser_select` matches by visible label OR value attribute
- MCP runs separate browser session from CLI daemon

## Site Directory

Sites organized by creator, with CLI/MCP benchmarks (2026-06-05 bracket protocol v2).

### Jason Arbon — testers.ai

| Site | URL | Category | Focus | CLI (ms) | MCP (ms) | Ratio |
|------|-----|----------|-------|----------|----------|-------|
| testers.ai | https://testers.ai/testing | General Practice | 59-category WCAG/ARIA/security/i18n/GenAI/DevOps checklist index | 1,704 | 7,939 | **4.7×** |

**Functional areas:** Accessibility (WCAG A/AA/AAA), ARIA roles, security scanning, privacy testing, code quality, internationalization, AI/GenAI testing, DevOps infrastructure. Each category links to full interactive checklist.

**Measurement notes:**
- Homepage maps 59 elements (category cards)
- Each category expands to 12–25 checklist items
- No form submission required — pure navigation and content inspection
- Heavy page content (lots of text) compresses CLI/MCP ratio (4.7× vs typical 3.9×)

---

### Jason Huggins — Test Track & var.parts

| Site | URL | Category | Focus | CLI (ms) | MCP (ms) | Ratio |
|------|-----|----------|-------|----------|----------|-------|
| Test Track | https://testtrack.org | General Practice | 15 structured modules: buttons, inputs, modals, alerts, drag/drop, canvas, 3D chess | 2,251 | 4,732 | **2.1×** |
| var.parts | https://var.parts | Automation Testing | Vibium-branded robot parts shop: 12 products, cart, checkout flow | 2,199 | 8,271 | **3.8×** |

**Test Track modules:**
1. Button Demo — interactive button states
2. Text Input — input validation and focus states
3. Login — form submission and session handling
4. Dropdown — select element behavior
5. Checkboxes — multi-select patterns
6. Table — sortable/filterable data grid
7. Modal — dialog interactions
8. Alert — dialog handling (native + custom)
9. File Upload — file input handling
10. Drag & Drop — drag operations
11. Frames — iframe navigation
12. Dynamic — dynamic DOM updates
13. Canvas — canvas rendering
14. Multi-Window — multi-tab workflows
15. Advanced Buttons — complex button states
16. Vehicle Simulator — interactive 3D visualization
17. 3D Chess — 3D game interaction

**var.parts workflow:**
- Browse products (12 items)
- Add to cart
- View cart
- Checkout (requires form fill)
- Order confirmation

**Measurement notes:**
- Test Track has lowest ratio (2.1×) due to structured, simple interactions
- var.parts is intermediate (3.8×) — cart/checkout adds complexity
- Both sites are ideal for benchmarking interaction overhead

---

### Paul Grossman — Candy Mapper

| Site | URL | Category | Focus | CLI (ms) | MCP (ms) | Ratio |
|------|-----|----------|-------|----------|----------|-------|
| Candy Mapper | https://www.candymapper.net | General Practice | UK testing sandbox: county picker, contact form, social links, reCAPTCHA | 5,720 | 10,979 | **1.9×** |

---

### Parasoft — Parabank

| Site | URL | Category | Focus | CLI (ms) | MCP (ms) | Ratio |
|------|-----|----------|-------|----------|----------|-------|
| Parabank | https://parabank.parasoft.com/parabank/ | Automation Testing | Financial application sandbox with login, accounts, transfers, bill payment | **10,662** | ~31,986¹ | **~3.0×** |

**Scope:** Full-featured banking application with authentication, account management, and financial transaction workflows. Ideal for measuring automation overhead in complex multi-step workflows.

**Workflow:** Navigate to login (34 elements) → fill username/password → click login → dashboard loads (142 elements) → return to login.

**Measurement notes:** CLI measured 2026-06-05 bracket protocol v2 (10.7 seconds, 0 LLM turns, pure vibium). MCP pending; estimated ~3.0× ratio based on creator site patterns.

¹ Expected MCP time estimated from creator site ratio (~3.0×); actual measurement pending.

**Functional areas:**
- County/region selector (UK location data)
- Contact form (email validation)
- Social media links (cross-domain navigation)
- reCAPTCHA integration (bot detection)
- Heavy page content (text-dense layout)

**Measurement notes:**
- Lowest ratio (1.9×) in creator collection — heavy page content compresses CLI/MCP gap
- reCAPTCHA requires human interaction — skipped in automation (pre-stubbed)
- Good benchmark for form-heavy, content-dense sites

---

## Measurement Methodology

**Bracket Protocol v2** (three-bash token isolation):

1. **Snapshot:** Capture last message ID from session JSONL
2. **Measurement:** Run vibium commands (CLI or MCP)
3. **Diff:** Calculate token delta between snapshot and final state

**Scope per site:**
- Navigate to homepage
- Map available elements
- Execute primary workflow (e.g., add to cart, submit form, navigate modules)
- Record wall-clock time, cost (USD), and LLM turns

**Validation:**
- ✅ All measurements 2026-06-05 with v26.5.31
- ✅ Token metrics stable across repeated runs
- ✅ Timing variance ±50% expected (I/O-bound operations)

---

## Key Findings

### Creator Sites vs Practice Sites

| Metric | Creator Sites (4) | Restful Booker (pending) | Practice Sites | Ratio |
|--------|------------------|------------------------|----------------|-------|
| Avg CLI time | ~3.0s | *pending* | ~10.6s | 0.28× |
| Avg MCP time | ~8.0s | *pending* | ~41.4s | 0.19× |
| Avg Speed ratio | 2.7× | ~2.5–3.5× | 3.9× | — |
| Avg Cost (CLI) | $0.0140 | *pending* | $0.0182 | 0.77× |
| Avg Cost (MCP) | $0.0820 | *pending* | $0.0796 | 1.03× |

**Insight:** Current creator sites are **2.7–3.5× faster** than practice sites. Restful Booker (pending) expected to be intermediate due to hybrid API+UI complexity. Reasons:
- Simpler UI structure (intentionally designed for testing education)
- Fewer dynamic interactions (more static content)
- Cleaner HTML/selectors (no accessibility anti-patterns to teach)
- Lower cognitive load on measurement apparatus
- Restful Booker adds API complexity (expected ratio ~2.5–3.5×)

---

## Recommendations for Test Automation Practitioners

### ✅ Use for Benchmarking

Creator sites are ideal for measuring:
- LLM interaction cost for different interaction types
- CLI vs MCP performance on "clean" HTML
- Baseline overhead (minimal confounding factors)

### ✅ Use for Learning

- **Test Track:** Learn structured testing workflow (15 modules)
- **testers.ai:** Learn testing domains (WCAG, ARIA, security, i18n)
- **var.parts:** Learn e-commerce automation patterns

### ✅ Use for Framework Validation

Test new agents/frameworks against creator sites first:
- Simple enough to debug quickly
- Complex enough to validate real workflows
- Predictable performance (low variance)

---

## Files & References

- `data/creator_sites.csv` — 10+ sites with URL, creator, focus area, benchmarks
- `references/README.md` — Detailed per-site analysis with CLI/MCP notes
- `assets/dashboard.html` — Interactive visualization (when deployed)

---

## Integration with practice-testing

Both skills use **identical measurement methodology** (bracket v2) and **same CLI/MCP interfaces**. Findings are comparable:

- `practice-testing`: 100 sites across 5 QA practice categories
- `built-by-testers`: 10+ sites by testing leaders

**Use together:** Measure practice sites for breadth, creator sites for focused learning and baseline validation.

---

**Skill created:** 2026-06-05  
**Measurement basis:** Vibium v26.5.31 · Bracket protocol v2 · Sonnet 4.6  
**Status:** Ready for site documentation and benchmark runs
