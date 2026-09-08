# HashCode Presentation Exporter

## Session #01 — IA, Productivité & AI Agents

This script generates two distribution formats from a structured slide definition:

- `.pptx` for Microsoft PowerPoint and compatible presentation tools;
- `.pdf` for distribution and printing.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install python-pptx reportlab
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
pip install python-pptx reportlab
```

## Generate

```bash
python scripts/generate_session_01.py
```

Generated files:

```text
dist/
├── hashcode-session-01-ia-productivite-ai-agents.pptx
└── hashcode-session-01-ia-productivite-ai-agents.pdf
```

## Design principle

The exporter uses the HashCode visual language:

- dark technology background;
- HashCode lime accent;
- strong typography;
- geometric cards and flows;
- no decorative emojis;
- presentation-first information hierarchy.

## Important

The script is intentionally based on structured slide data rather than attempting to parse arbitrary Slidev HTML/CSS.

This makes PowerPoint and PDF generation predictable and editable.

The next evolution should centralize the content in a shared JSON/YAML source so that Slidev, PPTX and PDF are generated from the same presentation model.
