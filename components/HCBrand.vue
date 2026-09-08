<script setup>
defineProps({
  compact: { type: Boolean, default: false },
  subtitle: { type: String, default: 'REBOOT' }
})
</script>

<template>
  <div class="hc-brand" :class="{ compact }">
    <div class="hc-mark" aria-hidden="true">
      <span></span><span></span><span></span><span></span>
    </div>
    <div class="hc-wordmark">
      <strong>HASHCODE</strong>
      <small>{{ subtitle }}</small>
    </div>
  </div>
</template>