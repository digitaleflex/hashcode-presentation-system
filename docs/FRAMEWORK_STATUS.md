# HashCode Presentation Framework — Status

## Implemented now

### Brand System
- HashCode master brand
- HashCode Reboot campaign identity
- Community / Academy / Security / Labs contextual system
- reusable pole tokens and `HCPole`

### Presentation System
- reusable brand component
- reusable section component
- design tokens
- framework CSS
- existing layout system

### Workshop System
- live workshop timer
- challenge card
- exercise card
- presenter cue component
- workshop quality standard

### Content System
- stats component
- process component
- presentation recipes
- framework demo

### Future theme boundary
The `theme/` directory defines the internal foundation for a future distributable Slidev theme.

### Future addon boundary
The `addons/` directory prevents experimental integrations from contaminating the core.

## Deliberately deferred

These are not missing by accident:

- npm publication of `slidev-theme-hashcode`
- custom addons
- polling integrations
- session analytics
- external workshop services

They require repeated real-world usage before abstraction.

## Validation gate

Before extracting a standalone theme:

1. build three real presentations
2. reuse the same components
3. identify repeated patterns
4. remove unstable APIs
5. document the stable authoring workflow
6. then package the theme
