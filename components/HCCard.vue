<script setup>
defineProps({
  icon: { type: String, default: '' },
  title: { type: String, required: true },
  text: { type: String, default: '' },
  accent: { type: Boolean, default: false }
})
</script>

<template>
  <article class="hc-card" :class="{ accent }">
    <div v-if="icon" class="hc-card-icon">{{ icon }}</div>
    <h3>{{ title }}</h3>
    <p v-if="text">{{ text }}</p>
    <slot />
  </article>
</template>