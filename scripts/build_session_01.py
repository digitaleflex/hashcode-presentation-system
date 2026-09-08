#!/usr/bin/env python3
"""Generate PowerPoint and PDF from the canonical presentation model."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "presentations" / "session-01" / "presentation.json"
data = json.loads(MODEL.read_text(encoding="utf-8"))
sys.path.insert(0, str(ROOT / "scripts"))
import generate_session_01 as exporter
exporter.SLIDES = data["slides"]
exporter.build_pptx()
exporter.build_pdf()
print(f"Generated {len(data['slides'])} slides from {MODEL}")