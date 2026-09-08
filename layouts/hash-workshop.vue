<script setup lang="ts">
import HCTheme from '../components/HCTheme.vue'

type Pole = 'community' | 'academy' | 'security' | 'labs'

withDefaults(defineProps<{ pole?: Pole }>(), { pole: 'academy' })
</script>

<template>
  <HCTheme :pole="pole" mode="workshop">
    <div class="hc-layout hc-workshop-layout">
      <div class="hc-workshop-tag">HANDS-ON WORKSHOP</div>
      <div class="hc-workshop-content"><slot /></div>
      <div class="hc-workshop-footer">BUILD · TEST · SHARE</div>
    </div>
  </HCTheme>
</template>

<style scoped>
.hc-workshop-layout{min-height:100%;display:flex;flex-direction:column;gap:1.4rem}
.hc-workshop-tag{color:var(--hc-pole);font-size:.75rem;font-weight:800;letter-spacing:.16em}
.hc-workshop-content{flex:1}
.hc-workshop-footer{color:var(--hc-muted);font-size:.65rem;letter-spacing:.14em;border-top:1px solid var(--hc-line);padding-top:1rem}
</style>