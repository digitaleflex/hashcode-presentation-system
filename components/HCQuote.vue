<script setup>
defineProps({
  quote: { type: String, required: true },
  kicker: { type: String, default: 'KEY IDEA' }
})
</script>

<template>
  <div class="hc-quote">
    <div class="hc-eyebrow">{{ kicker }}</div>
    <blockquote>“{{ quote }}”</blockquote>
    <div class="hc-quote-line"></div>
  </div>
</template>