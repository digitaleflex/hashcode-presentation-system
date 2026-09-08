<script setup lang="ts">
type Pole = 'community' | 'academy' | 'security' | 'labs'

const props = withDefaults(defineProps<{
  pole: Pole
  mode?: 'label' | 'signature' | 'badge'
}>(), {
  mode: 'label'
})

const meta: Record<Pole, { name: string; tagline: string; icon: string }> = {
  community: { name: 'Community', tagline: 'Connect · Share · Build Together', icon: '◌' },
  academy: { name: 'Academy', tagline: 'Learn · Practice · Master', icon: '◆' },
  security: { name: 'Security', tagline: 'Understand · Defend · Investigate', icon: '⬡' },
  labs: { name: 'Labs', tagline: 'Explore · Experiment · Ship', icon: '✦' },
}
</script>

<template>
  <div class="hc-pole" :data-pole="props.pole" :class="'mode-' + props.mode">
    <template v-if="props.mode === 'signature'">
      <div class="brand">HASHCODE</div>
      <div class="hc-pole-label">{{ meta[props.pole].name }}</div>
      <div class="tagline">{{ meta[props.pole].tagline }}</div>
    </template>

    <template v-else-if="props.mode === 'badge'">
      <span class="icon">{{ meta[props.pole].icon }}</span>
      <span>{{ meta[props.pole].name }}</span>
    </template>

    <template v-else>
      <span class="hc-pole-label">{{ meta[props.pole].name }}</span>
      <span class="hc-pole-line"></span>
    </template>
  </div>
</template>

<style scoped>
.hc-pole { --hc-pole: var(--hc-lime); }
.hc-pole[data-pole="community"] { --hc-pole: var(--hc-community); }
.hc-pole[data-pole="academy"] { --hc-pole: var(--hc-academy); }
.hc-pole[data-pole="security"] { --hc-pole: var(--hc-security); }
.hc-pole[data-pole="labs"] { --hc-pole: var(--hc-labs); }

.mode-label { display:flex; align-items:center; gap:.7rem; }
.mode-signature { display:flex; flex-direction:column; gap:.25rem; }
.mode-badge { display:inline-flex; align-items:center; gap:.45rem; padding:.35rem .7rem; border:1px solid color-mix(in srgb, var(--hc-pole) 55%, transparent); color:var(--hc-pole); border-radius:999px; font-weight:700; }

.brand { color:var(--hc-text); font-size:1.1rem; font-weight:900; letter-spacing:.08em; }
.tagline { color:var(--hc-muted); font-size:.58rem; letter-spacing:.08em; }
.icon { font-size:1rem; }
</style>
