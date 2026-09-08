# Slidev Layout Strategy

Production decks currently use Slidev's built-in `default` layout plus the HashCode CSS design system. This is intentional: CI demonstrated that the custom layouts outside the deck-local resolution path were not reliably discovered in Slidev v52. Production builds must remain deterministic and must never emit `Unknown layout`.

The Vue files in `layouts/` remain prototypes until packaged as a proper Slidev theme.
