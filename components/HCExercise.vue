<script setup lang="ts">
defineProps<{ mission: string; objective: string; deliverable?: string }>()
</script>
<template>
  <section class="hc-exercise">
    <div class="mission">MISSION {{ mission }}</div>
    <h2>{{ objective }}</h2>
    <div class="grid">
      <div><h3>Instructions</h3><slot /></div>
      <div v-if="deliverable"><h3>Livrable attendu</h3><p>{{ deliverable }}</p></div>
    </div>
  </section>
</template>
<style scoped>
.hc-exercise{padding:1.6rem;border:1px solid var(--hc-line);border-radius:1.25rem;background:linear-gradient(135deg,var(--hc-surface),var(--hc-bg))}
.mission{color:var(--hc-lime);font-size:.7rem;font-weight:900;letter-spacing:.18em}.hc-exercise h2{font-size:2.1rem}.grid{display:grid;grid-template-columns:2fr 1fr;gap:1.5rem}.grid h3{color:var(--hc-text);font-size:.9rem}.grid p{color:var(--hc-muted)}
</style>
