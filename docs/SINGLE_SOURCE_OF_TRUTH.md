# Single Source of Truth

## Canonical content

For Session 01, the only canonical presentation content is:

```
presentations/session-01/presentation.json
```

All presentation outputs must be generated from this file.

## Pipeline

```
presentation.json
      │
      ├── generate_slidev_session_01.py
      │        └── slides/generated/session-01.md
      │
      └── build_session_01.py
               ├── PowerPoint
               └── PDF
```

## Rule

Do not manually edit generated files.

Legacy Slidev files remain in the repository for historical reference but are not part of the production pipeline.
