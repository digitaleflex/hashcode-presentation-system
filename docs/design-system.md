# HashCode Slidev Design System

## Design principles
1. **Dark by default** — focus and contrast.
2. **Lime as signal** — #C5F441 is reserved for emphasis, progress and calls to action.
3. **One idea per slide** — avoid document-like slides.
4. **Strong hierarchy** — eyebrow → headline → supporting message.
5. **Systems over decoration** — every visual pattern must be reusable.

## Tokens

| Token | Value | Use |
|---|---|---|
| Background | #080A0C | Main canvas |
| Surface | #111418 | Cards |
| Surface 2 | #171B20 | Elevated elements |
| Lime | #C5F441 | Accent |
| Text | #F5F7FA | Primary text |
| Muted | #9AA3AD | Secondary text |

## Core layouts
- `hash-cover`: opening / closing slides
- `hash-section`: section transitions
- `hash-content`: standard content
- `hash-workshop`: exercises and hands-on moments

## Components
- `HCBrand`
- `HCSection`
- `HCCard`
- `HCMetric`
- `HCQuote`

## Brand assets
The production HashCode logo should be placed in `public/brand/` as:
- `hashcode-logo-primary.png`
- `hashcode-logo-horizontal.png`
- `hashcode-mark.png`

The current `HCBrand` component is a resilient vector fallback so presentations still work before raster/vector brand assets are added.
