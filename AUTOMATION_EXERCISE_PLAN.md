# automation-exercise.daisyladybug.com — Build Plan

Custom e-commerce testing sandbox for automation testing education and benchmarking.

## Project Specification

**Domain:** automation-exercise.daisyladybug.com  
**Category:** Automation Testing (mid-range complexity)  
**Measurement Target:** ~12s CLI, ~36s MCP @ 3.0× ratio  
**Tech Stack:** TBD (Next.js or static HTML+JS)  
**Design System:** Daisy Lady Bug design system  

## Core Workflows

### Happy Path (Primary)
1. **Browse** → Homepage with product grid
2. **Search/Filter** → Search bar, category filters, sort options
3. **Product Detail** → Click product → detailed view with specs
4. **Add to Cart** → Add product, confirm in cart sidebar
5. **Checkout** → Review cart, fill form (name, email, address)
6. **Order Confirmation** → Show order ID, confirmation message

### Edge Cases
- Cart limits (max items, stock checks)
- Duplicate additions
- Form field boundaries (max length, format validation)
- Price calculations (tax, shipping)

### Negative Scenarios
- Invalid inputs (email format, phone number)
- Out of stock handling
- Session expiration
- Network error recovery
- Concurrent cart modifications

## Page Structure

```
/
├── /products              # Product grid (search, filter, sort)
├── /products/:id          # Product detail page
├── /cart                  # Shopping cart review
├── /checkout              # Multi-step checkout form
├── /order-confirmation    # Order confirmation page
└── /admin                 # (Optional) Product management
```

## Test Data Requirements

### Products (10-15 items)
- Varying prices ($10-$200)
- Different categories
- Stock levels (in stock, limited, out of stock)
- Image assets
- Descriptions with various lengths

### Users (Pre-populated)
- Test credentials (any username/password works initially)
- Multiple sample orders in history

### Edge Case Test Data
- Product names with special characters
- Very long descriptions
- Max/min price products
- Zero-stock items

## Measurement Workflow

**CLI Measurement (~12s target):**
```
1. Navigate to homepage
2. Map elements (products, filters, cart button)
3. Search/filter products
4. Click product detail
5. Map detail page elements
6. Add to cart
7. Navigate to cart
8. Click checkout
9. Fill checkout form
10. Submit order
11. Verify confirmation message
12. Navigate back to home
```

**MCP Measurement (~36s estimated @ 3.0× ratio):**
- Same workflow as CLI
- Additional validation steps
- Form error handling verification

## Success Criteria

- ✅ Fully functional e-commerce workflow
- ✅ Happy path works cleanly (order → confirmation)
- ✅ Edge cases handled gracefully (validation messages)
- ✅ Negative cases show appropriate errors
- ✅ Responsive design (mobile-friendly)
- ✅ Fast page loads (<3s per page)
- ✅ CLI measurement ~12s ±2s
- ✅ MCP measurement ~3.0× ratio

## Build Phases

### Phase 1: Design & Specification
- Finalize workflow diagrams
- Design wireframes (use `/dlb-page` for consistency)
- Define test data schema
- Create measurement script

### Phase 2: Implementation
- Set up project structure
- Build frontend components
- Implement product catalog (with search/filter)
- Implement cart logic
- Implement checkout form
- Add validation and error handling

### Phase 3: Deployment & Measurement
- Deploy to automation-exercise.daisyladybug.com
- Test all workflows manually
- Run CLI measurement (10 iterations for variance)
- Run MCP measurement
- Record results in `creator_sites.csv`
- Document any quirks/workarounds

### Phase 4: Documentation
- Add site to `/built-by-testers` collection
- Update `SKILL.md` with site details
- Write measurement notes (any vibium-specific issues)

## Notes

- Use Daisy Lady Bug design system for consistency with daisyladybug.com
- Keep complexity mid-range (like Parabank, not Test Track)
- Ensure all workflows are testable with vibium CLI/MCP
- Avoid complex dialogs/alerts (testing pain points with vibium)
- Plan for browser compatibility (Chrome/Firefox/Safari)

---

**Status:** ✅ Complete & Live (2026-06-05)  
**Owner:** User (educational content)  
**Live URL:** https://automation-exercise.daisyladybug.com  
**Repository:** https://github.com/lana-20/automation-exercise  

**Completion Summary:**
- ✅ Phase 1: Design & specification complete (June 2-4)
- ✅ Phase 2: Implementation complete (Next.js 16.2.7, React 19, TypeScript)
- ✅ Phase 3: Deployed to Vercel with custom domain DNS + SSL
- ✅ Phase 4: Documentation complete (4 markdown files, 1,577 lines)
- ✅ Testing: 98/98 tests passing, WCAG 2.1 AA/AAA compliant
- ✅ CLI measurement: Functional verification complete (pending detailed benchmark)
- ✅ Next Step: CLI/MCP benchmark measurements (bracket protocol v2)
