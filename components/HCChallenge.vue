<script setup lang="ts">
withDefaults(defineProps<{ level?: string; title: string; duration?: string; team?: string }>(), {
  level: 'BEGINNER', duration: '15 min', team: 'Individuel'
})
</script>
<template>
  <section class="hc-challenge">
    <div class="meta"><span>{{ level }}</span><span>⏱ {{ duration }}</span><span>👥 {{ team }}</span></div>
    <h2>{{ title }}</h2>
    <div class="body"><slot /></div>
  </section>
</template>
<style scoped>
.hc-challenge{border-left:6px solid var(--hc-lime);padding:1.4rem 1.7rem;background:var(--hc-surface);border-radius:0 1rem 1rem 0}
.meta{display:flex;gap:1rem;color:var(--hc-lime);font-size:.68rem;font-weight:800;letter-spacing:.08em}.hc-challenge h2{font-size:2rem;margin:.65rem 0}.body{color:var(--hc-muted)}
</style>
