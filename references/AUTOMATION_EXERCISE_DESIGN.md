# automation-exercise.daisyladybug.com — Design Specification

E-commerce testing sandbox design with detailed wireframes, component specs, and test workflow mappings.

## Design System

**Based on:** Daisy Lady Bug design system  
**Colors:**
- Primary: #0f1a2a (dark blue)
- Accent: #d4552a (coral)
- Success: #4aa8a5 (mint)
- Error: #c53030 (red)
- Neutral: #f5f0eb (off-white)

**Typography:**
- Display: Playfair Display (serif)
- Body: Inter (sans-serif)
- Mono: JetBrains Mono (code)

**Components:** Buttons, cards, forms, navigation, alerts

---

## Page Designs

### 1. Homepage `/`

**Purpose:** Browse products, introduce the site

**Layout:**
```
┌─────────────────────────────────────────┐
│  automation-exercise          [Cart: 0] │
├─────────────────────────────────────────┤
│                                         │
│  Welcome to automation-exercise         │
│  Test e-commerce workflows             │
│                                         │
├─────────────────────────────────────────┤
│  Search: [_________________] [Search]   │
│                                         │
│  Category: [All ▼]  Sort: [Popular ▼]  │
│                                         │
├─────────────────────────────────────────┤
│                                         │
│  [Product 1]  [Product 2]  [Product 3] │
│  $49.99       $29.99       $199.99     │
│  [Add to Cart][Add to Cart][Add to Cart]│
│                                         │
│  [Product 4]  [Product 5]  [Product 6] │
│  $15.99       $89.99       $59.99      │
│  [Add to Cart][Add to Cart][Add to Cart]│
│                                         │
└─────────────────────────────────────────┘
```

**Interactive Elements:**
- Search bar (text input)
- Category filter dropdown (All, Electronics, Apparel, Home, Books)
- Sort dropdown (Popular, Price: Low→High, Price: High→Low, Newest)
- Product cards (6-12 visible, clickable)
- Add to Cart buttons (per product)
- Cart icon in header (shows item count)

**Test Scenarios:**
- ✅ Search by product name (case-insensitive)
- ✅ Filter by category
- ✅ Sort by price/popularity
- ✅ Add to cart (single item)
- ✅ Add duplicate items to cart
- ✅ View cart via header icon

**Edge Cases:**
- Search with no results → "No products found"
- Add to cart when stock = 0 → "Out of stock" message
- Add to cart when cart is full → "Cart limit reached"

---

### 2. Product Detail `/products/:id`

**Purpose:** View product details, add to cart

**Layout:**
```
┌─────────────────────────────────────────┐
│  automation-exercise          [Cart: N] │
│  [← Back to Products]                   │
├─────────────────────────────────────────┤
│                                         │
│  [Product Image (large)]     Details:   │
│                              Category:  │
│                              Electronics│
│                              Stock:     │
│                              [In Stock] │
│                              Price:     │
│                              $49.99     │
│                              Rating:    │
│                              ★★★★☆     │
│                              Quantity:  │
│                              [1] ▲▼     │
│                              [Add to Cart]
│                                         │
│  Product Name                          │
│  (40 characters max)                   │
│                                         │
│  Description                           │
│  Lorem ipsum dolor sit amet, consectetur│
│  adipiscing elit. Sed do eiusmod tempor│
│  incididunt ut labore et dolore magna. │
│  (up to 500 chars)                     │
│                                         │
│  Specs:                                │
│  • Weight: 2.5 lbs                     │
│  • Dimensions: 10"×6"×3"               │
│  • Color: Available in 3 colors        │
│  • Warranty: 1 year                    │
│                                         │
└─────────────────────────────────────────┘
```

**Interactive Elements:**
- Back button (navigates to /products)
- Quantity selector (spinner: 1-99 range)
- Add to Cart button
- Color/option selector (if available)
- Related products section (clickable)

**Test Scenarios:**
- ✅ View product details
- ✅ Adjust quantity
- ✅ Add to cart
- ✅ Select different product option
- ✅ View related products

**Edge Cases:**
- Product not found → 404 page
- Product out of stock → "Out of stock" button (disabled)
- Quantity selector boundaries: min 1, max 99
- Select max quantity → shows remaining stock

---

### 3. Shopping Cart `/cart`

**Purpose:** Review items, adjust quantities, proceed to checkout

**Layout:**
```
┌─────────────────────────────────────────┐
│  automation-exercise          [Cart: 3] │
├─────────────────────────────────────────┤
│  Shopping Cart                          │
│                                         │
│  Product Name      Qty  Price  Remove  │
│  ─────────────────────────────────────  │
│  Electronics Gadget  1  $49.99  [×]   │
│  Blue Apparel Shirt  2  $29.99  [×]   │
│  Home Decor Item     1  $199.99 [×]   │
│                                         │
│  ─────────────────────────────────────  │
│  Subtotal:              $309.96        │
│  Tax (8%):              $24.80         │
│  Shipping:              $10.00         │
│  ─────────────────────────────────────  │
│  Total:                 $344.76        │
│                                         │
│              [Continue Shopping]       │
│              [Proceed to Checkout]     │
│                                         │
│  Promo Code: [______________] [Apply] │
│                                         │
└─────────────────────────────────────────┘
```

**Interactive Elements:**
- Quantity spinners (per item)
- Remove buttons (delete from cart)
- Continue Shopping button (back to /products)
- Proceed to Checkout button
- Promo code input + apply button

**Test Scenarios:**
- ✅ View cart items with totals
- ✅ Adjust quantity (increase/decrease)
- ✅ Remove items
- ✅ Calculate tax and shipping
- ✅ Apply promo code
- ✅ Continue shopping
- ✅ Proceed to checkout

**Edge Cases:**
- Empty cart → "Your cart is empty" + Continue Shopping button
- Cart limit exceeded → Show warning
- Quantity becomes 0 → Auto-remove item
- Promo code invalid → Show error message
- Promo code valid → Apply discount, recalculate total

---

### 4. Checkout `/checkout`

**Purpose:** Collect shipping/payment info, confirm order

**Layout:**
```
┌─────────────────────────────────────────┐
│  automation-exercise          [Cart: 3] │
│  Checkout (Step 1 of 2)                 │
├─────────────────────────────────────────┤
│                                         │
│  Shipping Information                   │
│  ─────────────────────────────────────  │
│  First Name: [__________________]       │
│  Last Name:  [__________________]       │
│  Email:      [__________________]       │
│  Phone:      [__________________]       │
│  Address:    [__________________]       │
│  City:       [__________________]       │
│  State:      [CA ▼]  Zip: [_______]   │
│                                         │
│  [ ] Same as shipping                  │
│                                         │
│  Shipping Method:                      │
│  ◉ Standard (5-7 days) - FREE          │
│  ○ Express (2-3 days) - $15.00         │
│  ○ Overnight - $25.00                  │
│                                         │
│  Payment Method:                       │
│  ◉ Credit Card    ○ PayPal             │
│                                         │
│  Card Number: [________________]       │
│  Exp Date:    [__]  CVV: [___]         │
│                                         │
│              [Continue]  [Cancel]      │
│                                         │
└─────────────────────────────────────────┘
```

**Interactive Elements:**
- Text inputs: first name, last name, email, phone, address, city, zip
- State dropdown (all US states)
- Checkbox: Same as shipping
- Shipping method radios (with prices)
- Payment method radios
- Card input fields
- Continue & Cancel buttons

**Test Scenarios:**
- ✅ Fill all required fields
- ✅ Validate email format
- ✅ Validate phone format (###-###-####)
- ✅ Select shipping method (updates total)
- ✅ Select payment method
- ✅ Fill card details
- ✅ Form submission

**Validation Rules:**
- First/Last Name: required, max 50 chars
- Email: required, valid email format
- Phone: required, ###-###-#### format
- Address: required, max 100 chars
- City: required, max 50 chars
- State: required, dropdown selection
- Zip: required, 5-digit format (##### or #####-####)
- Card: required, 16 digits
- Exp Date: MM/YY format
- CVV: 3-4 digits

**Edge Cases:**
- Missing required field → Show inline error "This field is required"
- Invalid email → "Please enter a valid email"
- Invalid phone format → "Please use ###-###-#### format"
- Invalid zip → "Please enter 5 digit zip code"
- Card validation failure → "Invalid card number"

---

### 5. Order Confirmation `/order-confirmation`

**Purpose:** Confirm order, show order details

**Layout:**
```
┌─────────────────────────────────────────┐
│  automation-exercise          [Cart: 0] │
├─────────────────────────────────────────┤
│                                         │
│  ✓ Order Confirmed!                    │
│                                         │
│  Order Number: ORD-2024-001234          │
│  Expected Delivery: June 10, 2024       │
│                                         │
│  Order Summary:                         │
│  ─────────────────────────────────────  │
│  Electronics Gadget    ×1    $49.99    │
│  Blue Apparel Shirt    ×2    $29.99    │
│  Home Decor Item       ×1    $199.99   │
│                                         │
│  Subtotal:              $309.96        │
│  Tax:                   $24.80         │
│  Shipping (Express):    $15.00         │
│  Discount:              -$30.97        │
│  ─────────────────────────────────────  │
│  Total:                 $313.79        │
│                                         │
│  Shipping To:                          │
│  John Doe                              │
│  123 Main St                           │
│  San Francisco, CA 94105               │
│                                         │
│  Confirmation sent to: john@example.com│
│                                         │
│  [ Continue Shopping ]  [ View Order ] │
│                                         │
└─────────────────────────────────────────┘
```

**Elements:**
- Order number (format: ORD-YYYY-XXXXXX)
- Expected delivery date
- Itemized order summary
- Total calculation breakdown
- Shipping address display
- Confirmation email message
- Action buttons

**Test Scenarios:**
- ✅ Order confirmation displays correctly
- ✅ All items listed with quantities
- ✅ Totals calculated correctly
- ✅ Order number generated
- ✅ Shipping address shown
- ✅ Continue shopping navigates to /products
- ✅ View order shows details

---

## Component Library

### Button
- Primary: Coral background, white text, hover effect
- Secondary: Outlined coral, coral text
- Danger: Red background (remove item)
- Disabled state: Gray, no hover

```html
<button class="btn btn-primary">Add to Cart</button>
<button class="btn btn-secondary">Continue Shopping</button>
<button class="btn btn-danger">Remove</button>
<button class="btn" disabled>Out of Stock</button>
```

### Form Input
```html
<input type="text" placeholder="First Name" maxlength="50" required />
<input type="email" placeholder="Email" required />
<input type="tel" placeholder="Phone" pattern="\d{3}-\d{3}-\d{4}" />
<select required>
  <option value="">Select State</option>
  <option value="CA">California</option>
</select>
```

### Card
```html
<div class="product-card">
  <img src="product.jpg" alt="Product" />
  <h3>Product Name</h3>
  <p class="price">$49.99</p>
  <button class="btn btn-primary">Add to Cart</button>
</div>
```

### Alert
```html
<div class="alert alert-error">This field is required</div>
<div class="alert alert-success">Item added to cart!</div>
<div class="alert alert-warning">Only 2 items left in stock</div>
```

---

## Data Models

### Product
```json
{
  "id": "prod_001",
  "name": "Electronics Gadget",
  "price": 49.99,
  "category": "Electronics",
  "stock": 25,
  "description": "High-quality gadget...",
  "image": "/images/product-1.jpg",
  "specs": {
    "weight": "2.5 lbs",
    "dimensions": "10\"×6\"×3\"",
    "colors": ["Black", "Silver", "Gold"],
    "warranty": "1 year"
  }
}
```

### Cart Item
```json
{
  "productId": "prod_001",
  "name": "Electronics Gadget",
  "price": 49.99,
  "quantity": 1,
  "subtotal": 49.99
}
```

### Order
```json
{
  "id": "ORD-2024-001234",
  "items": [...],
  "subtotal": 309.96,
  "tax": 24.80,
  "shipping": 15.00,
  "discount": 30.97,
  "total": 313.79,
  "shippingAddress": {...},
  "status": "confirmed",
  "createdAt": "2024-06-05T10:30:00Z"
}
```

---

## Test Data: 12 Products

| ID | Name | Category | Price | Stock |
|--|--|--|--|--|
| 1 | Wireless Headphones | Electronics | $79.99 | 15 |
| 2 | Blue Cotton T-Shirt | Apparel | $24.99 | 50 |
| 3 | Desk Lamp | Home | $39.99 | 20 |
| 4 | Python Programming Book | Books | $34.99 | 30 |
| 5 | USB-C Cable 6ft | Electronics | $12.99 | 100 |
| 6 | Running Shoes | Apparel | $89.99 | 25 |
| 7 | Coffee Maker | Home | $49.99 | 12 |
| 8 | Yoga Mat | Home | $19.99 | 40 |
| 9 | Laptop Stand | Electronics | $29.99 | 18 |
| 10 | Winter Jacket | Apparel | $129.99 | 8 |
| 11 | Cookbook: Italian Recipes | Books | $28.99 | 35 |
| 12 | Desk Organizer | Home | $15.99 | 60 |

**Edge Case Products:**
- Out of stock (0 inventory)
- Low stock (1-3 items)
- High price (>$100)
- Low price (<$15)

---

## Measurement Workflow Mapping

**CLI Test Flow (target: ~12s):**
1. Navigate to homepage (2s)
2. Map products (1s)
3. Search/filter (1s)
4. Click product detail (1.5s)
5. Map detail page (1s)
6. Add to cart (1s)
7. Navigate to cart (1.5s)
8. Click checkout (1s)
9. Fill form fields (1.5s)
10. Submit checkout (1s)
11. Verify confirmation (1s)
12. Navigate back (0.5s)

**Total: ~12.5 seconds** ✓

**MCP Test Flow (target: ~36s @ 3.0× ratio):**
- Same workflow with additional validation verifications
- Form error handling (invalid inputs)
- Edge case navigation (out of stock, etc.)

---

**Status:** Design specification complete (2026-06-05)  
**Next:** Implementation phase (build frontend)
