# Slidev Integration Strategy

## Current approach

HashCode uses Slidev as the presentation runtime and Vue as the component system.

The framework adds HashCode-specific structure on top of that runtime:

- layouts define slide structure
- components define reusable content
- tokens define visual rules
- poles define contextual identity
- recipes define narrative structure
- workshop components define participant interaction

## Recommended authoring workflow

```
1. Choose the HashCode pole
2. Choose a presentation recipe
3. Assemble layouts
4. Insert reusable components
5. Add presenter notes
6. Run the workshop quality gate
7. Build and review
```

## Technical presentations

For technical sessions, prefer:

- code blocks for explanation
- progressive code examples when teaching evolution
- Mermaid-compatible diagrams where appropriate
- live demos only when the environment has been rehearsed

A live demo should always have a fallback screenshot or static explanation.

## Presenter workflow

Use presenter notes for:

- timing
- speaking cues
- questions
- demonstrations
- transitions

The visible slide should remain focused on the participant. Animation instructions belong to the presenter workflow, not the main slide.
