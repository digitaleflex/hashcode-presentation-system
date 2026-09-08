<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
const props = withDefaults(defineProps<{ minutes?: number; label?: string; autoStart?: boolean }>(), {
  minutes: 15, label: 'EXERCICE EN COURS', autoStart: false
})
const remaining = ref(props.minutes * 60)
const running = ref(false)
let timer: ReturnType<typeof setInterval> | undefined
const formatted = computed(() => {
  const m = Math.floor(remaining.value / 60).toString().padStart(2, '0')
  const s = (remaining.value % 60).toString().padStart(2, '0')
  return `${m}:${s}`
})
function tick(){ if (remaining.value > 0) remaining.value-- }
function start(){ if (!timer) { running.value = true; timer = setInterval(tick, 1000) } }
function pause(){ if (timer) clearInterval(timer); timer = undefined; running.value = false }
function reset(){ pause(); remaining.value = props.minutes * 60 }
onMounted(() => { if (props.autoStart) start() })
onBeforeUnmount(pause)
</script>

<template>
  <div class="hc-timer">
    <div class="eyebrow">⏱ {{ label }}</div>
    <div class="time">{{ formatted }}</div>
    <div class="controls">
      <button @click="start">Start</button>
      <button @click="pause">Pause</button>
      <button @click="reset">Reset</button>
    </div>
  </div>
</template>

<style scoped>
.hc-timer{padding:1.2rem 1.5rem;border:1px solid var(--hc-line);border-radius:1.25rem;background:var(--hc-surface);width:max-content}
.eyebrow{color:var(--hc-lime);font-size:.65rem;font-weight:800;letter-spacing:.14em}.time{font-size:2.8rem;font-weight:900;margin:.4rem 0}
.controls{display:flex;gap:.5rem}.controls button{background:transparent;color:var(--hc-text);border:1px solid var(--hc-line);padding:.35rem .6rem;border-radius:.5rem;cursor:pointer}
</style>
