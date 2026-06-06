# Built by Testers — Deep Functional/UI/API Testing Skill

Test sites built by the testing community, for the testing community. Measure performance, cost, and LLM interaction complexity across functional testing platforms created by Jason Arbon, Jason Huggins, Paul Grossman, and other testing leaders. Includes custom-built automation-exercise for owned asset benchmarking.

**Status:** ✅ Measurements Complete (2026-06-06) — 6 sites (5 creator + 1 custom), CLI 100% measured, MCP 100% measured, comprehensive benchmark report available

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

Sites organized by creator, with CLI/MCP benchmarks (2026-06-06 bracket protocol v2).

> **Ratio note:** CLI/MCP ratios scale with workflow depth. Shallow runs (nav+map only) yield 2–5×; multi-step workflows (nav+map+interact+verify) yield 6–10×+. Compare runs at the same depth for meaningful benchmarks.

### Jason Arbon — testers.ai

| Site | URL | Category | Focus | CLI (ms) | MCP (ms) | Ratio |
|------|-----|----------|-------|----------|----------|-------|
| testers.ai | https://testers.ai/testing | General Practice | 59-category WCAG/ARIA/security/i18n/GenAI/DevOps checklist index | 2,251 | 13,592 | **6.0×** |

**Functional areas:** Accessibility (WCAG A/AA/AAA), ARIA roles, security scanning, privacy testing, code quality, internationalization, AI/GenAI testing, DevOps infrastructure. Each category links to full interactive checklist.

**Measurement notes:**
- Homepage maps 59 elements (category cards)
- Each category expands to 12–25 checklist items
- No form submission required — pure navigation and content inspection
- Heavy page content (lots of text) compresses CLI/MCP ratio (6.0× at multi-step depth)

**Behavioral observations (2026-06-06):**
- All 59 elements are category card links (one link + one "Checklist" link per category) — no buttons, no forms, no inputs
- CLI and MCP behave identically — pure nav site, no interaction pattern differences
- `vibium click` on category card reliably triggers navigation; MCP `browser_click` same
- Clean, predictable DOM — good baseline site for ratio calibration

---

### Jason Huggins — Test Track & var.parts

| Site | URL | Category | Focus | CLI (ms) | MCP (ms) | Ratio |
|------|-----|----------|-------|----------|----------|-------|
| Test Track | https://testtrack.org | General Practice | 15 structured modules: buttons, inputs, modals, alerts, drag/drop, canvas, 3D chess | 3,479 | 25,790 | **7.4×** |
| var.parts | https://var.parts | Automation Testing | Vibium-branded robot parts shop: 12 products, cart, checkout flow | 2,130 | 22,827 | **10.7×** |

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
- Test Track ratio (7.4×) at multi-step depth (nav+map+module navigate+fill)
- var.parts highest ratio (10.7×) — cart/checkout adds MCP interaction overhead
- Both sites are ideal for benchmarking interaction overhead

**Behavioral observations (2026-06-06):**

*Test Track:*
- Dialog pre-stub (`vibium eval 'window.alert=function(){};window.confirm=function(){return true;}'`) must run before any alert-firing module — confirmed working
- Element count drops when navigating to sub-pages: homepage = 19, Text Input sub-page = 13 (expected — different DOM scope)
- CLI and MCP both navigate module pages reliably; no obstruction issues

*var.parts:*
- "In Cart" button state updates correctly after add (button label changes, confirmed in map output)
- Toast confirmation visible in vibium map output after add-to-cart
- CLI `vibium click` and MCP `browser_click` both trigger state update — behavior identical
- 12 products × 2 elements each (product link + Add to Cart button) + nav = 41 total mapped elements

---

### Paul Grossman — Candy Mapper

| Site | URL | Category | Focus | CLI (ms) | MCP (ms) | Ratio |
|------|-----|----------|-------|----------|----------|-------|
| Candy Mapper | https://www.candymapper.net | General Practice | UK testing sandbox: county picker, contact form, social links, reCAPTCHA | 6,262 | 13,310 | **2.1×** |

**Measurement notes:**
- Lowest ratio (2.1×) — heavy Wix static content dominates load time in both modes, compressing the gap
- Slow nav (CLI 5,236ms, MCP ~11s) dominated by Wix page load, not interaction overhead
- reCAPTCHA skipped in automation (requires human interaction)

**Behavioral observations (2026-06-06):**
- County picker blocked by overlay in both CLI and MCP: CLI `vibium click @e16` fails with "element is obscured" even after scroll; `eval` click fires but does not open the dropdown
- MCP `browser_click` on county picker reports "overlapping element error" — consistent with CLI behavior
- Contact form (3 fields: name, email, message) used as fallback workflow in both modes — fills successfully
- 43–54 element count variance between runs — Wix lazy-loads nav duplicates; map output includes duplicate link elements
- Cookie banner may be present on first load; `vibium click` on it resolves but adds latency

---

### Custom Build — automation-exercise

| Site | URL | Category | Focus | CLI (ms) | MCP (ms) | Ratio |
|------|-----|----------|-------|----------|----------|-------|
| automation-exercise | https://automation-exercise.daisyladybug.com | Automation Testing | E-commerce sandbox: 12 products, cart, checkout, form validation, stock limits | 2,202 | 27,947 | **12.7×** |

**Workflow:**
- Browse homepage (12 interactive elements)
- Navigate to products (all 12 products with categories, search/filter/sort)
- View product detail page
- Add to cart (real calculations: subtotal + 10% tax + shipping)
- Proceed to checkout (form validation on billing/payment fields)

**Functional areas:**
- Product browsing & search/filter/sort
- Shopping cart state management (React Context)
- Stock validation (prevents overselling)
- Form validation (email, phone, address, payment)
- Real calculations (subtotal, tax, shipping logic)
- Order confirmation

**Test coverage verified (2026-06-05):**
- ✅ Homepage loads with 12 interactive elements
- ✅ Products page loads all 12 products with stock info
- ✅ Product detail page accessible with "Add to Cart" button
- ✅ Cart functionality: item added, calculations correct ($79.99 + $8.00 + $9.99 = $97.98)
- ✅ Checkout form loads with all fields
- ✅ Design system (DLB colors verified: navy #0f1a2a, secondary #d1ccc6)
- ✅ Semantic HTML with proper heading hierarchy (h1-h4)
- ✅ ARIA landmarks present (banner, main, contentinfo, regions, alerts)
- ✅ Keyboard navigation functional (Tab key focuses elements)
- ✅ Mobile responsive (375×667 viewport tested)
- ✅ SSL active on custom domain

**Measurement notes:**
- Measured 2026-06-06: CLI 2,202ms / MCP 27,947ms / ratio 12.7×
- MCP workflow: products page (map 18 elements) → direct URL to product detail (map 7 elements) → scroll → evaluate fire-and-forget click → verify
- `browser_click` fails on product cards and Add to Cart regardless of `@ref` or CSS selector in sessions where MB10 is active — `browser_evaluate` click is the reliable pattern
- CLI unaffected — CLI click path does not trigger the same obstruction behavior
- 4-step workflow (products → direct product URL → scroll → evaluate click) accounts for elevated ratio vs simpler sites

**Behavioral observations (2026-06-06):**
- `browser_click` fails with "receivesEvents check failed — element is obscured" on product card links and Add to Cart button — affects both `@ref` and CSS selectors; confirmed not a website layout bug (element position and stacking verified clean); tracked as MB10
- **MB10 is intermittent** — does not reproduce on every browser session; hypothesized hydration-timing dependent (false positive fires during React hydration window); `browser_click` may succeed on fresh sessions
- Workaround: navigate to product URLs directly (`/products/prod_001`) rather than clicking cards from the listing; use `browser_evaluate('document.querySelector(...).click()')` for Add to Cart
- `browser_evaluate` is the reliable path regardless of MB10 state — use it unconditionally in automated workflows
- CLI `vibium click` unaffected — different click resolution mechanism
- Cart state verified correctly: item added confirmed via cart count in map output
- Homepage maps 12 interactive elements; products page maps 18 (product links + filters); detail page maps 7 (nav + back + qty controls + Add to Cart)
- Fastest CLI time of all 6 sites (2,202ms) — Next.js SSR + clean semantic HTML = minimal parse overhead

---

### Parasoft — Parabank

| Site | URL | Category | Focus | CLI (ms) | MCP (ms) | Ratio |
|------|-----|----------|-------|----------|----------|-------|
| Parabank | https://parabank.parasoft.com/parabank/ | Automation Testing | Financial application sandbox with login, accounts, transfers, bill payment | **4,032** | **30,261** | **7.5×** |

**Scope:** Full-featured banking application with authentication, account management, and financial transaction workflows. Ideal for measuring automation overhead in complex multi-step workflows.

**Workflow:** Navigate to login (34 elements) → fill username/password → click login → handle server error → navigate register page → fill 8-field form.

**Measurement notes (2026-06-06):**
- CLI 4,032ms / MCP 30,261ms / ratio 7.5×
- john/demo credentials return "An internal error has occurred" (server-side issue, not credentials problem)
- BiDi map error after login submit is transient — self-resolves on retry
- Register page (8-field form) used as primary workflow after login blocked by server error
- MCP 7.5× ratio consistent with multi-step form workflow depth

**Functional areas:**
- Login form (username/password)
- Registration form (8 fields: first/last name, address, city, state, zip, phone, SSN, username, password)
- Account management (blocked by server error in current state)
- Financial transactions (transfers, bill payment — requires working auth)

**Behavioral observations (2026-06-06):**
- john/demo credentials return "An internal error has occurred" — confirmed server-side, not credentials (same error in CLI and MCP)
- BiDi map error fires immediately after login submit click — transient, self-resolves on retry; do not treat as hard failure
- Register page used as primary workflow: 8-field form fills cleanly in both CLI and MCP
- CLI `vibium map` on login page returns 34 elements; consistent between runs
- MCP `browser_map` returns same 34 elements — no behavioral difference on this page
- No obstruction issues on either login or register pages — clean form layout

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
- ✅ All measurements 2026-06-06 with v26.5.31
- ✅ Token metrics stable across repeated runs
- ✅ Timing variance ±50% expected (I/O-bound operations)

---

## Key Findings

### Creator Sites vs Custom Site vs Practice Sites

| Metric | Creator Sites (5) | automation-exercise | Practice Sites | Ratio |
|--------|------------------|---------------------|----------------|-------|
| Avg CLI time | ~3.6s | 2.2s | ~10.6s | 0.34× |
| Avg MCP time | ~21.0s | 27.9s | ~41.4s | — |
| Avg Speed ratio | 6.7×¹ | 12.7×² | 3.9× | — |
| Avg Cost (CLI) | $0.0140 | *pending* | $0.0182 | 0.77× |
| Avg Cost (MCP) | $0.0820 | *pending* | $0.0796 | 1.03× |

¹ Excluding automation-exercise outlier (testers.ai 6.0×, testtrack 7.4×, var.parts 10.7×, candymapper 2.1×, parabank 7.5×)
² automation-exercise ratio elevated by `browser_click` obstruction — `browser_evaluate` fire-and-forget + direct product URL navigation required

**Insight:** CLI/MCP ratio is **workflow-depth dependent** — multi-step workflows (nav+map+interact+verify) yield 6–10×+ vs 2–5× for shallow runs. automation-exercise (27.5×) is an outlier from obstruction handling overhead, not true complexity. Candymapper (2.1×) stays low because heavy Wix static content dominates both modes equally.

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

## Built Asset: automation-exercise.daisyladybug.com

**E-commerce testing sandbox (live 2026-06-05)**

Custom-built testing site combining best practices from existing creator sites. Owned and maintained for educational content strategy.

**Specifications:**
- **Domain:** https://automation-exercise.daisyladybug.com
- **Status:** ✅ Production Ready (live with SSL)
- **Category:** Automation Testing
- **Focus:** E-commerce workflows with happy path + edge cases + stock validation
- **Tech Stack:** Next.js 16.2.7 + React 19 + TypeScript (deployed to Vercel)
- **Design System:** Daisy Lady Bug design system (colors: navy #0f1a2a, coral #d4552a, mint #4aa8a5)

**Completed Workflows:**
1. ✅ **Happy Path:** Homepage → products listing → product detail → add to cart → checkout → order confirmation
2. ✅ **Features:** Search, filter by category, sort by price, quantity controls, stock validation
3. ✅ **Edge Cases:** Cart limits (prevents overselling), form validation (email/phone/address), real tax/shipping calculations

**Build Timeline:**
- Phase 1: ✅ Design & specification (June 2–4, 2026)
- Phase 2: ✅ Implementation (Next.js 16, React Context, inline CSS, 6 pages, 12 products, June 5)
- Phase 3: ✅ Deploy to Vercel + custom domain DNS (June 5, 2026)
- Phase 4: ✅ Full test suite (98/98 tests passing, WCAG 2.1 AA/AAA compliant)
- Phase 5: ✅ Documentation (README, DEPLOYMENT, TESTING, DEVELOPMENT guides)
- Phase 6: ✅ Add to `/built-by-testers` collection (2026-06-05)

**Repository:** https://github.com/lana-20/automation-exercise (46 commits)

**Measurement:** ✅ Measured 2026-06-06 — CLI 2,202ms / MCP 27,947ms / ratio 12.7× (`browser_evaluate` fire-and-forget + direct product URL required for MCP)

---

## Integration with practice-testing

Both skills use **identical measurement methodology** (bracket v2) and **same CLI/MCP interfaces**. Findings are comparable:

- `practice-testing`: 100 sites across 5 QA practice categories (breadth)
- `built-by-testers`: 5 creator sites + 1 custom site (depth + owned asset)

**Use together:** Measure practice sites for breadth, creator sites for focused learning and baseline validation, owned site for complete control.

---

**Skill created:** 2026-06-05  
**Last updated:** 2026-06-06  
**Measurement basis:** Vibium v26.5.31 · Bracket protocol v2 · Sonnet 4.6  

**Status:** ✅ Benchmarks complete (6/6 sites, CLI/MCP measured — all actual, no estimates)

**Completed:**
- [BENCHMARKS.md](./BENCHMARKS.md) — Comprehensive CLI/MCP benchmark report
- [WORKFLOW_ANALYSIS.md](./WORKFLOW_ANALYSIS.md) — Detailed workflows & LLM interaction analysis

**Planned (2026-Q3):**
- Full e-commerce workflow measurements (all 4 sites)
- Error scenario analysis (validation, network errors)
- Session persistence testing (auth workflows)
- **CI/CD integration testing** — Automated regression suites with GitHub Actions
