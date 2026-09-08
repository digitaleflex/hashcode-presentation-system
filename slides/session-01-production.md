---
theme: default
title: "IA, Productivité & AI Agents"
info: "HashCode Workshop #01 — Production Deck"
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
---

<!--
SESSION #01 — PRODUCTION DECK
Current production scope: Slides 01–03.
Visual assets will be integrated once the PNG files are uploaded to public/assets/session-01/.
-->

---
layout: hash-cover
---

<div class="session-cover">

<div class="eyebrow">HASHCODE WORKSHOP #01</div>

# IA, Productivité<br><span>& AI Agents</span>

<p class="cover-lead">
Transformer l'intelligence artificielle en un véritable levier de travail.
</p>

<div class="cover-meta">
  <div>
    <strong>FORMAT</strong>
    <span>Workshop interactif</span>
  </div>
  <div>
    <strong>FOCUS</strong>
    <span>Comprendre · Pratiquer · Produire</span>
  </div>
</div>

<div class="cover-signal">
  <div class="signal-core">AI</div>
  <div class="signal-node n1"></div>
  <div class="signal-node n2"></div>
  <div class="signal-node n3"></div>
  <div class="signal-line l1"></div>
  <div class="signal-line l2"></div>
  <div class="signal-line l3"></div>
</div>

</div>

<!--
TIME: 0:00–0:03
SAY: Ce soir, nous ne faisons pas une présentation sur les outils IA à la mode. Nous allons parler de travail : où nous perdons du temps, où l'IA peut réellement aider et ce qui change avec les AI Agents.
ASK: Qui ici utilise déjà une IA chaque semaine ?
TRANSITION: Avant de parler de solutions, regardons notre problème.
-->

<style>
.session-cover { position:relative; min-height:100%; padding:4.5rem 5.5rem; overflow:hidden; }
.session-cover:after { content:''; position:absolute; width:52rem; height:52rem; right:-18rem; top:-14rem; border:1px solid rgba(197,244,65,.18); border-radius:50%; box-shadow:0 0 140px rgba(197,244,65,.08); }
.eyebrow { color:var(--hc-lime); letter-spacing:.22em; font-size:.72rem; font-weight:700; margin-bottom:1.4rem; }
.session-cover h1 { font-size:3.9rem; line-height:.98; max-width:900px; margin:0; letter-spacing:-.045em; }
.session-cover h1 span { color:var(--hc-lime); }
.cover-lead { font-size:1.15rem; color:#a7adb5; max-width:640px; line-height:1.55; margin-top:1.8rem; }
.cover-meta { display:flex; gap:3.2rem; margin-top:3rem; }
.cover-meta div { display:flex; flex-direction:column; gap:.4rem; }
.cover-meta strong { color:var(--hc-lime); font-size:.58rem; letter-spacing:.16em; }
.cover-meta span { color:#e9edf0; font-size:.85rem; }
.cover-signal { position:absolute; right:8rem; bottom:6rem; width:240px; height:240px; }
.signal-core { position:absolute; inset:72px; display:grid; place-items:center; border:1px solid var(--hc-lime); border-radius:50%; color:var(--hc-lime); font-size:1.4rem; font-weight:800; box-shadow:0 0 40px rgba(197,244,65,.14); }
.signal-node { position:absolute; width:14px; height:14px; background:var(--hc-lime); border-radius:50%; box-shadow:0 0 16px rgba(197,244,65,.8); }
.n1 { top:14px; left:112px; }.n2 { bottom:28px; left:24px; }.n3 { bottom:28px; right:24px; }
.signal-line { position:absolute; height:1px; background:rgba(197,244,65,.45); transform-origin:left center; }
.l1 { width:86px; left:120px; top:75px; transform:rotate(-90deg); }.l2 { width:100px; left:70px; top:150px; transform:rotate(135deg); }.l3 { width:100px; left:170px; top:150px; transform:rotate(45deg); }
</style>

---
layout: hash-section
---

<div class="hook-slide">

<div class="hook-index">01 / LA QUESTION</div>

<h1>Sommes-nous vraiment<br><span>plus productifs…</span></h1>

<div class="hook-divider"></div>

<p class="hook-ending">…ou simplement <strong>plus occupés ?</strong></p>

<div class="noise">
  <span>NOTIFICATIONS</span>
  <span>MESSAGES</span>
  <span>RÉUNIONS</span>
  <span>OUTILS</span>
  <span>CONTEXT SWITCHING</span>
</div>

</div>

<!--
TIME: 0:03–0:07
SAY: Nous avons plus d'outils que jamais. Pourtant, beaucoup de personnes terminent leur journée avec la sensation d'avoir beaucoup travaillé sans avoir fait avancer ce qui compte réellement.
PAUSE: Laisser la question visible.
ASK: Dans votre journée, qu'est-ce qui vous donne le plus l'impression d'être occupé sans être réellement productif ?
TRANSITION: Regardons ce qui crée cette friction.
-->

<style>
.hook-slide { min-height:100%; padding:5.2rem 6rem; display:flex; flex-direction:column; justify-content:center; position:relative; }
.hook-index { position:absolute; top:4rem; left:6rem; color:var(--hc-lime); font-size:.68rem; letter-spacing:.18em; font-weight:700; }
.hook-slide h1 { font-size:4.6rem; line-height:1; letter-spacing:-.055em; margin:0; max-width:900px; }
.hook-slide h1 span { color:#5f6670; }
.hook-divider { width:110px; height:4px; background:var(--hc-lime); margin:2.2rem 0; box-shadow:0 0 22px rgba(197,244,65,.45); }
.hook-ending { font-size:2rem; color:#c9ced4; margin:0; }.hook-ending strong { color:white; }
.noise { position:absolute; right:5rem; bottom:3.5rem; display:flex; flex-direction:column; align-items:flex-end; gap:.55rem; }
.noise span { color:#535a63; font-size:.62rem; letter-spacing:.15em; border:1px solid rgba(255,255,255,.07); padding:.5rem .7rem; }
.noise span:nth-child(2), .noise span:nth-child(4) { color:#747b85; }
</style>

---
layout: hash-content
---

<div class="problem-slide">

<div class="problem-kicker">02 / LE PROBLÈME</div>

# La friction est devenue<br>une partie du travail.

<div class="problem-grid">

<div class="problem-card">
  <div class="problem-number">01</div>
  <h3>Trop chercher</h3>
  <p>L'information existe, mais elle est dispersée entre plusieurs outils et conversations.</p>
</div>

<div class="problem-card">
  <div class="problem-number">02</div>
  <h3>Trop répéter</h3>
  <p>Les mêmes tâches de lecture, synthèse, rédaction et organisation reviennent constamment.</p>
</div>

<div class="problem-card accent">
  <div class="problem-number">03</div>
  <h3>Trop basculer</h3>
  <p>Chaque changement de contexte consomme de l'attention et ralentit la production réelle.</p>
</div>

</div>

<div class="problem-bottom">
  <span class="lime-dot"></span>
  <strong>Être occupé n'est pas la même chose qu'être productif.</strong>
</div>

</div>

<!--
TIME: 0:07–0:12
SAY: Le problème n'est pas uniquement le manque de temps. Une grande partie du problème est la friction invisible : chercher, répéter et basculer.
EXPLAIN: L'IA devient intéressante lorsqu'elle réduit une friction identifiable.
ASK: Lequel de ces trois problèmes vous coûte le plus cher aujourd'hui ?
TRANSITION: Nous allons maintenant définir ce que nous voulons réellement obtenir de cette séance.
-->

<style>
.problem-slide { padding:1.5rem 0; }
.problem-kicker { color:var(--hc-lime); letter-spacing:.18em; font-size:.65rem; font-weight:700; margin-bottom:1rem; }
.problem-slide h1 { font-size:2.8rem; line-height:1.08; letter-spacing:-.04em; margin:0 0 2rem; }
.problem-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1rem; }
.problem-card { min-height:205px; padding:1.45rem; border:1px solid rgba(255,255,255,.09); background:rgba(255,255,255,.025); position:relative; }
.problem-card.accent { border-color:rgba(197,244,65,.35); box-shadow:inset 0 0 30px rgba(197,244,65,.035); }
.problem-number { color:var(--hc-lime); font-size:.7rem; letter-spacing:.14em; margin-bottom:1.5rem; }
.problem-card h3 { font-size:1.25rem; margin:0 0 .8rem; }
.problem-card p { color:#8d949d; font-size:.85rem; line-height:1.55; margin:0; }
.problem-bottom { margin-top:1.7rem; display:flex; align-items:center; gap:.7rem; color:#d8dde1; font-size:1rem; }
.lime-dot { width:9px; height:9px; border-radius:50%; background:var(--hc-lime); box-shadow:0 0 14px rgba(197,244,65,.7); }
</style>


---
layout: hash-content
---

<div class="objectives-slide">

<div class="slide-kicker">03 / LA DESTINATION</div>

# À la fin de cette séance,<br><span>vous devrez pouvoir agir.</span>

<div class="objective-grid">

<div class="objective-item">
  <span>01</span>
  <div>
    <h3>Identifier</h3>
    <p>Repérer les principales frictions dans votre propre travail.</p>
  </div>
</div>

<div class="objective-item">
  <span>02</span>
  <div>
    <h3>Comprendre</h3>
    <p>Distinguer les usages réellement utiles de l'IA des simples effets de mode.</p>
  </div>
</div>

<div class="objective-item">
  <span>03</span>
  <div>
    <h3>Concevoir</h3>
    <p>Imaginer un workflow augmenté et une première idée d'AI Agent.</p>
  </div>
</div>

</div>

<div class="objective-footer">
  <div class="objective-rule"></div>
  <p><strong>Comprendre → Voir → Pratiquer → Produire</strong></p>
</div>

</div>

<!--
TIME: 0:12–0:15
SAY: Notre objectif n'est pas de sortir d'ici avec une liste de 50 outils. Nous voulons repartir avec une meilleure manière de regarder notre travail.
EMPHASIZE: À la fin, chacun doit avoir identifié au moins une friction réelle et une piste concrète d'amélioration.
TRANSITION: Pour cela, il faut d'abord comprendre correctement le rôle de l'IA.
-->

<style>
.objectives-slide { padding:1.5rem 0; }
.slide-kicker { color:var(--hc-lime); letter-spacing:.18em; font-size:.65rem; font-weight:700; margin-bottom:1rem; }
.objectives-slide h1 { font-size:2.65rem; line-height:1.1; letter-spacing:-.045em; margin:0 0 2rem; }
.objectives-slide h1 span { color:var(--hc-lime); }
.objective-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.2rem; }
.objective-item { display:flex; gap:1rem; padding:1.2rem 0; border-top:1px solid rgba(255,255,255,.12); }
.objective-item > span { color:var(--hc-lime); font-size:.7rem; font-weight:700; letter-spacing:.1em; }
.objective-item h3 { margin:0 0 .55rem; font-size:1.15rem; }
.objective-item p { margin:0; color:#9098a1; font-size:.82rem; line-height:1.55; }
.objective-footer { margin-top:2rem; display:flex; align-items:center; gap:1rem; }
.objective-rule { width:48px; height:2px; background:var(--hc-lime); }
.objective-footer p { margin:0; color:#d9dde1; font-size:.95rem; }
</style>

---
layout: hash-section
---

<div class="amplifier-slide">

<div class="amplifier-label">04 / LE BON MODÈLE MENTAL</div>

<div class="equation">
  <div class="equation-side human">
    <small>HUMAN</small>
    <strong>+</strong>
    <span>Jugement<br>Contexte<br>Responsabilité</span>
  </div>

  <div class="equation-symbol">×</div>

  <div class="equation-side ai">
    <small>AI</small>
    <strong>+</strong>
    <span>Vitesse<br>Analyse<br>Première version</span>
  </div>

  <div class="equation-result">
    <small>RESULT</small>
    <h2>Capacité<br><span>augmentée.</span></h2>
  </div>
</div>

<p class="amplifier-warning">
  L'IA n'est pas une magie qui remplace la pensée.
  <strong>Elle amplifie un processus déjà compris.</strong>
</p>

</div>

<!--
TIME: 0:15–0:20
SAY: Le mauvais réflexe est de demander : qu'est-ce que l'IA peut faire à ma place ?
SAY: La meilleure question est : quelle capacité humaine puis-je augmenter, accélérer ou mieux structurer ?
EXPLAIN: L'IA est forte pour analyser, résumer, structurer et générer une première version. L'humain reste responsable du jugement et de la validation.
ASK: Quelle partie de votre travail exige absolument votre jugement humain ?
TRANSITION: Maintenant que nous avons le bon modèle mental, voyons comment l'utiliser méthodiquement.
-->

<style>
.amplifier-slide { min-height:100%; padding:5rem 6rem; display:flex; flex-direction:column; justify-content:center; }
.amplifier-label { color:var(--hc-lime); font-size:.65rem; letter-spacing:.18em; font-weight:700; margin-bottom:2.2rem; }
.equation { display:grid; grid-template-columns:1.1fr 70px 1.1fr 1.25fr; gap:1.2rem; align-items:center; }
.equation-side { min-height:235px; border:1px solid rgba(255,255,255,.12); padding:1.7rem; display:flex; flex-direction:column; }
.equation-side small, .equation-result small { color:#737b85; letter-spacing:.18em; font-size:.58rem; }
.equation-side strong { color:var(--hc-lime); font-size:2.3rem; margin:1.8rem 0 .8rem; }
.equation-side span { color:#c6ccd1; line-height:1.65; font-size:.9rem; }
.equation-symbol { text-align:center; color:#68717a; font-size:2.2rem; }
.equation-result { min-height:235px; padding:1.7rem; background:rgba(197,244,65,.06); border:1px solid rgba(197,244,65,.3); display:flex; flex-direction:column; justify-content:center; }
.equation-result h2 { font-size:2.4rem; line-height:1; margin:.8rem 0 0; letter-spacing:-.04em; }.equation-result h2 span { color:var(--hc-lime); }
.amplifier-warning { margin-top:2.2rem; max-width:800px; color:#949ba3; font-size:1rem; line-height:1.6; }.amplifier-warning strong { color:#f0f2f3; }
</style>

---
layout: hash-content
---

<div class="framework-slide">

<div class="framework-header">
  <div>
    <div class="slide-kicker">05 / LE FRAMEWORK HASHCODE</div>
    <h1>Avant d'automatiser,<br><span>il faut comprendre le travail.</span></h1>
  </div>
  <div class="framework-tag">4 STEPS</div>
</div>

<div class="framework-flow">

<div class="flow-step active">
  <div class="step-no">01</div>
  <h3>Identifier</h3>
  <p>Où perdez-vous réellement du temps ou de l'énergie ?</p>
</div>

<div class="flow-arrow">→</div>

<div class="flow-step">
  <div class="step-no">02</div>
  <h3>Simplifier</h3>
  <p>Le processus actuel est-il vraiment nécessaire ?</p>
</div>

<div class="flow-arrow">→</div>

<div class="flow-step">
  <div class="step-no">03</div>
  <h3>Augmenter</h3>
  <p>Comment l'IA peut-elle améliorer la réflexion ou la production ?</p>
</div>

<div class="flow-arrow">→</div>

<div class="flow-step">
  <div class="step-no">04</div>
  <h3>Automatiser</h3>
  <p>Quelles étapes répétitives peuvent être déléguées dans un cadre contrôlé ?</p>
</div>

</div>

<div class="framework-principle">
  <span>PRINCIPE</span>
  <strong>Automatiser un mauvais processus permet simplement de produire des erreurs plus vite.</strong>
</div>

</div>

<!--
TIME: 0:20–0:27
SAY: Voici le framework central de la séance.
STEP 1: Identifier la vraie friction.
STEP 2: Simplifier avant d'ajouter une technologie.
STEP 3: Augmenter avec l'IA.
STEP 4: Automatiser uniquement les étapes suffisamment comprises et répétitives.
ASK: Qui a déjà automatisé quelque chose avant d'avoir réellement compris le processus ?
TRANSITION: Ce framework nous permet maintenant de faire une distinction essentielle : assistant IA et AI Agent.
-->

<style>
.framework-slide { padding:1.5rem 0; }
.framework-header { display:flex; align-items:flex-end; justify-content:space-between; margin-bottom:2.1rem; }
.framework-slide h1 { font-size:2.5rem; line-height:1.08; margin:0; letter-spacing:-.045em; }.framework-slide h1 span { color:var(--hc-lime); }
.framework-tag { border:1px solid rgba(197,244,65,.35); color:var(--hc-lime); padding:.5rem .8rem; font-size:.6rem; letter-spacing:.15em; }
.framework-flow { display:grid; grid-template-columns:1fr 30px 1fr 30px 1fr 30px 1fr; gap:.3rem; align-items:stretch; }
.flow-step { min-height:215px; padding:1.25rem; border:1px solid rgba(255,255,255,.1); background:rgba(255,255,255,.018); }
.flow-step.active { border-color:rgba(197,244,65,.4); background:rgba(197,244,65,.045); }
.step-no { color:var(--hc-lime); font-size:.65rem; letter-spacing:.15em; margin-bottom:2rem; }
.flow-step h3 { margin:0 0 .8rem; font-size:1.1rem; }
.flow-step p { margin:0; color:#8d959e; font-size:.78rem; line-height:1.55; }
.flow-arrow { display:flex; align-items:center; justify-content:center; color:var(--hc-lime); font-size:1.2rem; }
.framework-principle { margin-top:1.5rem; display:flex; align-items:center; gap:1rem; border-left:3px solid var(--hc-lime); padding:.7rem 1rem; background:rgba(255,255,255,.02); }
.framework-principle span { color:var(--hc-lime); font-size:.58rem; letter-spacing:.15em; }.framework-principle strong { font-size:.85rem; color:#d9dde1; }
</style>

<!--
NEXT: Assistant IA vs AI Agent.
-->
