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
      <div class="hc-eyebrow"><span v-if="number">{{ number }}</span>{{ eyebrow }}</div>
      <h1 v-html="title"></h1>
      <p v-if="description">{{ description }}</p>
    </div>
    <div class="hc-section-index">{{ number }}</div>
  </div>
</template>