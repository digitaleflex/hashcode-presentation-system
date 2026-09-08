#!/usr/bin/env python3
"""Generate Slidev content from presentations/session-01/presentation.json."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
MODEL=ROOT/"presentations/session-01/presentation.json"
OUT=ROOT/"slides/generated/session-01.md"
data=json.loads(MODEL.read_text(encoding="utf-8"))
parts=[]
for s in data["slides"]:
    parts.append(f"<!-- AUTO-GENERATED | SOURCE ID: {s['id']} -->\n\n# {s['title']}\n")
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text("\n\n---\n\n".join(parts),encoding="utf-8")
print(f"Generated {OUT}")
