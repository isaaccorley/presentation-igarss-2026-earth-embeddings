<script setup>
// Poster frame until the slide's first click (mouse, spacebar, or
// presenter clicker — anything that advances Slidev's click counter),
// then plays and loops. Pair with `clicks: 1` in the slide frontmatter
// so the slide has a click stop to consume.
//
// Leaving the slide pauses and rewinds the clip, so coming back
// restarts it from the first frame (backward navigation re-enters at
// the final click state, so it plays immediately; a fresh forward
// visit waits for the click again). Visibility is tracked through
// Slidev's nav state — inactive slides are only `visibility: hidden`,
// which fools IntersectionObserver.
//
// In PDF export (?print) a base64 poster frame painted via CSS class
// .fig-<name>, which renders synchronously and can't lose a network
// race during export.
import { useSlideContext } from '@slidev/client'
import { onMounted, ref, unref, watch } from 'vue'

defineProps({
  name: { type: String, required: true },
})

const base = import.meta.env.BASE_URL
const isPrint =
  typeof window !== 'undefined' && window.location.search.includes('print')

const el = ref(null)
const started = ref(false)

const play = () => el.value?.play().catch(() => {})
const stop = () => {
  const v = el.value
  if (!v) return
  v.pause()
  v.currentTime = 0
}

if (!isPrint) {
  const { $slidev, $page, $clicks } = useSlideContext()
  const sync = () => {
    const active = $slidev.nav.currentSlideNo === unref($page)
    if (active && unref($clicks) >= 1) {
      if (!started.value) {
        started.value = true
        play()
      }
    } else {
      started.value = false
      stop()
    }
  }
  watch([() => $slidev.nav.currentSlideNo, () => unref($clicks)], sync)
  onMounted(sync)
}

onMounted(() => {
  const v = el.value
  if (!v) return

  // Slidev and autoplay policies like to pause media; resume if the
  // clip has been started and the tab is visible
  v.addEventListener('pause', () => {
    if (!started.value) return
    if (document.visibilityState !== 'visible') return
    setTimeout(() => {
      if (started.value) play()
    }, 80)
  })

  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible' && started.value) play()
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
    :data-started="started"
    class="loop-media"
    preload="auto"
    loop
    muted
    playsinline
  />
</template>
