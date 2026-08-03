<script setup>
// Autoplaying loop in the browser; in PDF export (?print) a base64
// poster frame painted via CSS class .fig-<name>, which renders
// synchronously and can't lose a network race during export.
//
// Slidev (and browser autoplay policies) like to pause media, so the
// clip re-plays itself whenever it is paused while visible on screen.
import { onMounted, ref } from 'vue'

defineProps({
  name: { type: String, required: true },
})

const base = import.meta.env.BASE_URL
const isPrint =
  typeof window !== 'undefined' && window.location.search.includes('print')

const el = ref(null)

onMounted(() => {
  const v = el.value
  if (!v) return
  const play = () => v.play().catch(() => {})

  const io = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (e.isIntersecting) play()
      else v.pause()
    }
  })
  io.observe(v)

  v.addEventListener('pause', () => {
    if (document.visibilityState !== 'visible') return
    const r = v.getBoundingClientRect()
    const visible =
      r.width > 0 &&
      r.bottom > 0 &&
      r.top < window.innerHeight &&
      r.right > 0 &&
      r.left < window.innerWidth
    if (visible) setTimeout(play, 80)
  })

  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible') play()
  })
})
</script>

<template>
  <div v-if="isPrint" :class="['plot', `fig-${name}`]" style="width: 100%" />
  <video
    v-else
    ref="el"
    :src="`${base}loop-${name}.mp4`"
    :poster="`${base}poster-${name}.png`"
    class="loop-media"
    autoplay
    loop
    muted
    playsinline
  />
</template>
