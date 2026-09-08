<script setup>
defineProps({
  compact: { type: Boolean, default: false },
  subtitle: { type: String, default: 'REBOOT' },
  markOnly: { type: Boolean, default: false }
})
</script>

<template>
  <div class="hc-brand" :class="{ compact }">
    <img
      v-if="markOnly"
      src="/brand/hashcode-reboot-mark.svg"
      alt="HashCode Reboot"
      class="hc-brand-mark"
    />
    <img
      v-else
      src="/brand/hashcode-reboot-logo.svg"
      alt="HashCode Reboot"
      class="hc-brand-logo"
    />
    <small v-if="subtitle && !markOnly" class="hc-brand-subtitle">{{ subtitle }}</small>
  </div>
</template>

<style scoped>
.hc-brand { display:flex; flex-direction:column; gap:.35rem; width:max-content; }
.hc-brand-logo { width:190px; height:auto; display:block; }
.hc-brand-mark { width:58px; height:auto; display:block; }
.hc-brand.compact .hc-brand-logo { width:120px; }
.hc-brand-subtitle { color:var(--hc-lime); font-size:.58rem; letter-spacing:.18em; }
</style>
