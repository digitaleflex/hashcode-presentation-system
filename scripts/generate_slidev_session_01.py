#!/usr/bin/env python3
import html, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; MODEL=ROOT/"presentations/session-01/presentation.json"; OUT=ROOT/"slides/generated/session-01.md"
LAYOUTS={"cover":"default","statement":"default","cards":"default","split":"default","flow":"default","comparison":"default"}
def e(v): return html.escape(str(v),quote=False)
def fm(s,l): return "\n".join(["---",f"layout: {l}",f'sourceId: "{e(s["id"])}"',"---","",f'<div class="hc-eyebrow">{e(s.get("eyebrow",""))}</div>' if s.get("eyebrow") else "",f'# {e(s.get("title",""))}',""])
def render(s):
 t=s.get("type","statement"); p=[fm(s,LAYOUTS.get(t,"default"))]
 if t=="cards":
  p.append('<div class="hc-card-grid">'+"".join(f'<div class="hc-card"><div class="hc-card-label">{e((list(c)+["","",""])[0])}</div><h3>{e((list(c)+["","",""])[1])}</h3><p>{e((list(c)+["","",""])[2])}</p></div>' for c in s.get("cards",[]))+"</div>")
 elif t=="split":
  l=s.get("left",["",[]]);r=s.get("right",["",[]]); p.append(f'<div class="hc-split"><div class="hc-panel"><div class="hc-panel-title">{e(l[0])}</div><ul>{"".join(f"<li>{e(x)}</li>" for x in l[1])}</ul></div><div class="hc-multiply">×</div><div class="hc-panel"><div class="hc-panel-title">{e(r[0])}</div><ul>{"".join(f"<li>{e(x)}</li>" for x in r[1])}</ul></div></div><div class="hc-result">{e(s.get("result",""))}</div>')
 elif t=="flow": p.append('<div class="hc-flow">'+"".join(f'<div class="hc-step"><div class="hc-step-number">{e(n)}</div><div><h3>{e(a)}</h3><p>{e(b)}</p></div></div>' for n,a,b in s.get("steps",[]))+"</div>")
 elif t=="comparison":
  l=s.get("left",["","",[]]);r=s.get("right",["","",[]]); side=lambda a:f'<div class="hc-compare-side"><div class="hc-side-title">{e(a[0])}</div><h3>{e(a[1])}</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in a[2])}</ul></div>';p.append(f'<div class="hc-comparison-grid">{side(l)}<div class="hc-versus">VS</div>{side(r)}</div>')
 elif s.get("subtitle"): p.append(f'<p class="hc-lead">{e(s["subtitle"])}</p>')
 footer=s.get("footer",s.get("meta",""))
 if footer:p.append(f'<div class="hc-footer">{e(footer)}</div>')
 return "\n".join(x for x in p if x)
def main():
 d=json.loads(MODEL.read_text(encoding="utf-8")); OUT.parent.mkdir(parents=True,exist_ok=True)
 OUT.write_text(f'---\ntheme: default\ntitle: {e(d["meta"].get("title","HashCode Presentation"))}\n---\n\n'+"\n\n---\n\n".join(render(s) for s in d.get("slides",[]))+"\n",encoding="utf-8")
 text=OUT.read_text(encoding="utf-8")
 bad=[x for x in ["undefined","layout: hash-content"] if x in text]
 if bad: raise SystemExit("Forbidden generated tokens: "+", ".join(bad))
 print(f"Generated {len(d.get("slides",[]))} Slidev slides: {OUT}")
if __name__=="__main__": main()
