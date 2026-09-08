<script setup lang="ts">
defineProps<{ time?: string; action: string; type?: 'say'|'ask'|'demo'|'transition' }>()
</script>
<template>
  <aside class="hc-cue" :data-type="type || 'say'">
    <strong v-if="time">{{ time }}</strong>
    <span>{{ action }}</span>
  </aside>
</template>
<style scoped>
.hc-cue{display:flex;gap:.7rem;padding:.6rem .8rem;border-left:3px solid var(--hc-lime);background:rgba(197,244,65,.08);font-size:.8rem}.hc-cue strong{color:var(--hc-lime)}
</style>
