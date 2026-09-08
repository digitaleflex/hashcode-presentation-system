# HashCode Presentation Architecture

## Single Source of Truth

The authoritative content for each presentation lives in:

`presentations/<session>/presentation.json`

```text
presentation.json
      │
      ├── Slidev visual layer
      │
      └── Python export layer
              ├── PowerPoint
              └── PDF
```

## Rules

1. Edit content in the canonical model first.
2. Exporters consume the canonical model.
3. Visual layers must not silently create independent content.
4. Generated files in `dist/` are outputs, not sources.
5. Content changes must propagate from the canonical model.

## Benefits

- one source of truth;
- no content drift;
- reusable presentation data;
- predictable multi-format generation;
- easier automation.

## Next evolution

- schema validation;
- automated Slidev generation;
- CI export pipeline;
- asset references;
- speaker notes in the canonical model.
