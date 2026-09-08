<script setup>
defineProps({
  value: { type: String, required: true },
  label: { type: String, required: true }
})
</script>

<template>
  <div class="hc-metric">
    <strong>{{ value }}</strong>
    <span>{{ label }}</span>
  </div>
</template>