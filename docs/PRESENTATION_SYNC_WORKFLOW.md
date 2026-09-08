# Presentation Sync Workflow

## Single source of truth
`presentations/session-01/presentation.json`

## Workflow
1. Review and update the canonical model.
2. Generate the Slidev content layer.
3. Generate PowerPoint and PDF.
4. Review all visual outputs.
5. Approve or iterate.

## Commands
```bash
python scripts/generate_slidev_session_01.py
python scripts/build_session_01.py
```

Generated files are outputs. Presentation wording is changed in the canonical model first.
