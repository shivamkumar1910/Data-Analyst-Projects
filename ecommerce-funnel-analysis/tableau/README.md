# Tableau Dashboard Guide

This project is designed to be simple enough for a beginner analyst to build in Tableau.

## Dashboard Goal

The dashboard should help a business answer one question clearly:

Where are users dropping off in the e-commerce funnel?

## Recommended Dashboard Layout

### Page 1: Funnel Overview

#### KPI Cards
- Total Users
- Add-to-Cart Rate
- Checkout Rate
- Purchase Conversion Rate

#### Visuals
- Funnel chart showing Signup → Product View → Add to Cart → Checkout → Purchase
- Conversion rate by stage
- Drop-off chart by stage

#### Filters
- Date
- Device Type
- Traffic Source
- Country

### Page 2: Conversion by Segment

#### Visuals
- Conversion by Device Type
- Conversion by Traffic Source
- Conversion by Country

#### Filters
- Date
- Device Type
- Traffic Source
- Country

### Page 3: Trend Analysis

#### Visuals
- Daily conversion trend
- Weekly conversion trend

#### Filters
- Date
- Device Type
- Traffic Source

## Suggested Tableau Workflow

1. Connect Tableau to the MySQL table.
2. Import the `ecommerce_events` table.
3. Create a calculated field for `Stage` if needed.
4. Use `user_id` as the primary customer count unit.
5. Build a funnel chart using stage-by-stage user counts.
6. Create calculated fields for:
   - Add-to-Cart Rate
   - Checkout Rate
   - Purchase Conversion Rate
   - Stage Drop-off Rate
7. Add date filters and segmentation filters.
8. Keep the layout simple and readable.

## Example Calculated Fields

### Total Users
COUNTD([user_id])

### Stage Users
COUNTD(IF [event_type] = 'signup' THEN [user_id] END)

### Add-to-Cart Rate
COUNTD(IF [event_type] = 'add_to_cart' THEN [user_id] END) /
COUNTD(IF [event_type] = 'product_view' THEN [user_id] END)

### Checkout Rate
COUNTD(IF [event_type] = 'checkout' THEN [user_id] END) /
COUNTD(IF [event_type] = 'add_to_cart' THEN [user_id] END)

### Purchase Conversion Rate
COUNTD(IF [event_type] = 'purchase' THEN [user_id] END) /
COUNTD(IF [event_type] = 'signup' THEN [user_id] END)

## Design Tips

- Use a clean color palette
- Keep the dashboard uncluttered
- Use consistent labels and spacing
- Highlight the largest drop-off point
- Make filters easy to use

This is a realistic dashboard for a beginner project and should be easy to explain in an interview.
