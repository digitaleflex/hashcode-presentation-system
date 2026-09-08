# ⚡ HashCode Presentation Framework

Reusable presentation infrastructure for HashCode workshops, training, technical sessions and community events.

## Mission

This is not a collection of static templates.

The project is a **presentation framework** built on Slidev and Vue:

- Brand System
- Layout System
- Component Library
- Pole Context System
- Workshop System
- Technical Demo Patterns
- Presenter Workflow
- Presentation Recipes

## Brand architecture

HashCode uses a **branded house**:

- HashCode Community
- HashCode Academy
- HashCode Security
- HashCode Labs

All poles share the HashCode master identity. Pole accents provide context without creating competing logos.

**HashCode Reboot** remains a campaign / transformation identity.

See:

- `docs/BRAND_ARCHITECTURE.md`
- `docs/POLE_VISUAL_SYSTEM.md`

## Core components

### Brand & context
- `HCBrand`
- `HCPole`
- `HCSection`

### Content
- `HCStat`
- `HCProcess`

### Workshop
- `HCWorkshopTimer`
- `HCChallenge`
- `HCExercise`
- `HCPresenterCue`

## Presentation recipes

Standard structures are documented in:

`docs/PRESENTATION_RECIPES.md`

Supported formats:

- AI workshops
- Cybersecurity sessions
- Community events
- Technical / Labs demos

## Workshop system

Every HashCode workshop should contain:

1. a clear objective
2. an explanation
3. a demonstration
4. participant interaction
5. a practical exercise
6. a concrete deliverable
7. a debrief
8. a next action

See `docs/WORKSHOP_SYSTEM.md`.

## Repository

```
components/        Vue component library
layouts/           Slidev layouts
styles/            Design tokens and pole rules
theme/             Future Slidev theme foundation
addons/            Future addon boundary
slides/            Real presentation content
public/brand/      Approved HashCode brand assets
docs/              Architecture and usage documentation
```

## Strategic rule

The framework becomes a standalone distributable Slidev theme **only after it has been validated through at least three real HashCode presentations**.

That prevents premature abstraction and keeps the system grounded in real usage.

## Pilot session

**Session 01 — IA, Productivité & AI Agents**

08 September 2026 · 21:30–23:00 · UTC+1
