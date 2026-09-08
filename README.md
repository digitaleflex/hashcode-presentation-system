# ⚡ HashCode Presentation System

Reusable presentation infrastructure for HashCode workshops, training and technical sessions.

## Design system

### Brand principles
- Dark-first interface
- HashCode lime: `#C5F441`
- Strong typography and generous whitespace
- One dominant idea per slide
- Reusable components instead of copy/paste design
- Motion only when it improves comprehension

### Core layouts
- `hash-cover`
- `hash-section`
- `hash-content`
- `hash-workshop`

### Core components
- `HCBrand`
- `HCSection`
- `HCCard`
- `HCMetric`
- `HCQuote`

## Repository

```text
components/        Reusable Vue components
layouts/           Slidev layouts
styles/            Tokens and visual rules
slides/
  design-system/   Visual system showcase
  session-01-ai-productivity-agents/
public/brand/      Approved HashCode brand assets
docs/              System documentation
```

## Brand assets

The approved production logo should be stored in `public/brand/`. The current `HCBrand` component provides a vector fallback.

## Pilot session

**Session 01 — IA, Productivité & AI Agents**

08 September 2026 · 21:30–23:00 · UTC+1

## Status

Design system foundation is in place. Next: integrate the approved logo asset, migrate Session 01 to the new layouts, then preview and refine the visual result.
