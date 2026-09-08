<script setup lang="ts">
defineProps<{ value: string | number; label: string; detail?: string }>()
</script>
<template>
  <div class="hc-stat"><div class="value">{{ value }}</div><div class="label">{{ label }}</div><small v-if="detail">{{ detail }}</small></div>
</template>
<style scoped>
.hc-stat{padding:1rem;border:1px solid var(--hc-line);border-radius:1rem}.value{font-size:2.8rem;font-weight:900;color:var(--hc-lime)}.label{font-weight:700}.hc-stat small{color:var(--hc-muted)}
</style>
