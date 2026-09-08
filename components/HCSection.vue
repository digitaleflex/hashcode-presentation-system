<script setup>
defineProps({
  number: { type: String, default: '' },
  eyebrow: { type: String, default: 'HASHCODE TECH SESSION' },
  title: { type: String, required: true },
  description: { type: String, default: '' }
})
</script>

<template>
  <div class="hc-section">
    <HCBrand compact />
    <div class="hc-section-body">
      <div class="hc-eyebrow"><span v-if="number">{{ number }} · </span>{{ eyebrow }}</div>
      <h1 v-html="title"></h1>
      <p v-if="description">{{ description }}</p>
    </div>
    <div v-if="number" class="hc-section-index">{{ number }}</div>
  </div>
</template>

<style scoped>
.hc-section{min-height:100%;padding:2.5rem 3.4rem;display:flex;flex-direction:column;justify-content:space-between;background:var(--hc-bg)}
.hc-section-body{max-width:1000px;margin:auto 0}.hc-section h1{font-size:4.4rem;line-height:1.02;margin:.8rem 0}.hc-section p{font-size:1.25rem;color:var(--hc-muted);max-width:760px}.hc-section-index{font-size:7rem;font-weight:900;color:rgba(197,244,65,.08);align-self:flex-end}
</style>