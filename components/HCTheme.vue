<script setup lang="ts">
type Pole = 'community' | 'academy' | 'security' | 'labs'

const props = defineProps<{
  pole: Pole
  label?: string
  mode?: 'default' | 'immersive' | 'workshop'
}>()

const defaults: Record<Pole, { label: string; tagline: string }> = {
  community: { label: 'HashCode Community', tagline: 'CONNECT · SHARE · BUILD TOGETHER' },
  academy: { label: 'HashCode Academy', tagline: 'LEARN · PRACTICE · MASTER' },
  security: { label: 'HashCode Security', tagline: 'UNDERSTAND · DEFEND · INVESTIGATE' },
  labs: { label: 'HashCode Labs', tagline: 'EXPLORE · EXPERIMENT · SHIP' },
}
</script>

<template>
  <div class="hc-theme" :data-pole="props.pole" :data-mode="props.mode || 'default'">
    <div class="hc-theme-header">
      <span class="hc-theme-label">{{ props.label || defaults[props.pole].label }}</span>
      <span class="hc-theme-tagline">{{ defaults[props.pole].tagline }}</span>
    </div>
    <div class="hc-theme-content"><slot /></div>
    <div class="hc-theme-footer">
      <img src="/brand/hashcode-reboot-mark.svg" alt="HashCode" class="hc-theme-mark" />
      <span>{{ defaults[props.pole].label }}</span>
    </div>
  </div>
</template>

<style scoped>
.hc-theme{
  --hc-pole:var(--hc-lime);
  min-height:100%;
  display:flex;
  flex-direction:column;
  position:relative;
  background:
    radial-gradient(circle at 90% 10%, color-mix(in srgb,var(--hc-pole) 12%,transparent), transparent 30%),
    var(--hc-bg);
}
.hc-theme[data-pole="community"]{--hc-pole:var(--hc-community)}
.hc-theme[data-pole="academy"]{--hc-pole:var(--hc-academy)}
.hc-theme[data-pole="security"]{--hc-pole:var(--hc-security)}
.hc-theme[data-pole="labs"]{--hc-pole:var(--hc-labs)}

.hc-theme-header,.hc-theme-footer{display:flex;align-items:center;justify-content:space-between}
.hc-theme-header{padding:.7rem 1rem;border-bottom:1px solid color-mix(in srgb,var(--hc-pole) 35%,transparent)}
.hc-theme-label{color:var(--hc-pole);font-size:.65rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase}
.hc-theme-tagline{color:var(--hc-muted);font-size:.48rem;letter-spacing:.1em}
.hc-theme-content{flex:1;min-height:0}
.hc-theme-footer{padding:.55rem 1rem;color:var(--hc-muted);font-size:.5rem;letter-spacing:.08em}
.hc-theme-mark{width:22px;height:22px;object-fit:contain}
.hc-theme[data-mode="immersive"] .hc-theme-header{background:color-mix(in srgb,var(--hc-pole) 8%,transparent)}
.hc-theme[data-mode="workshop"] .hc-theme-footer{border-top:2px solid var(--hc-pole)}
</style>