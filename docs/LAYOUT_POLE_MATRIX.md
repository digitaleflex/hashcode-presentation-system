# HashCode Presentation Layout × Pole Matrix

The presentation system uses a single layout library with contextual pole themes.

## Recommended combinations

| Layout | Community | Academy | Security | Labs |
|---|---|---|---|---|
| Hero / Cover | Community events | Training opening | Security briefing | Project launch |
| Comparison | Ideas / options | Concepts | Threat comparisons | Technical choices |
| Timeline | Community roadmap | Learning journey | Incident / methodology | Experiment roadmap |
| Diagram | Ecosystem | Mental model | Attack / defense model | Architecture |
| Code | Optional | Guided examples | Security snippets | Engineering demos |
| Stats | Engagement | Learning outcomes | Security metrics | Experiment results |
| Quote | Member voices | Expert insight | Principles | Builder mindset |
| Workshop | Collaboration | Hands-on training | Investigation exercise | Prototype sprint |

## Usage rule

The **layout communicates structure**.

The **pole theme communicates context**.

Do not duplicate layouts just to change colors.

Example:

```vue
<template>
  <HCAcademyTheme>
    <div class="hc-layout">
      <!-- hash-workshop content -->
    </div>
  </HCAcademyTheme>
</template>
```

## Default mapping

- Academy → workshops, courses, learning sessions
- Security → cybersecurity, OSINT, intelligence
- Community → events, onboarding, collaboration
- Labs → prototypes, architecture, engineering projects
