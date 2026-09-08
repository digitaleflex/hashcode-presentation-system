<script setup lang="ts">
defineProps<{ steps: string[] }>()
</script>
<template>
  <div class="hc-process">
    <template v-for="(step,index) in steps" :key="step">
      <div class="step"><span>{{ String(index + 1).padStart(2,'0') }}</span><strong>{{ step }}</strong></div>
      <div v-if="index < steps.length - 1" class="arrow">→</div>
    </template>
  </div>
</template>
<style scoped>
.hc-process{display:flex;align-items:center;gap:.6rem;flex-wrap:wrap}.step{min-width:120px;padding:1rem;border:1px solid var(--hc-line);border-radius:.8rem;background:var(--hc-surface)}.step span{display:block;color:var(--hc-lime);font-size:.65rem}.arrow{color:var(--hc-muted);font-size:1.4rem}
</style>
