// Layout QA for the deck: title wrapping, orphan bullet lines, cite collisions,
// and LoopVideo rects in PDF points (for scripts/embed_videos.py).
// Usage: node scripts/measure_slides.mjs [baseUrl]
import { chromium } from 'playwright-chromium'

const BASE = process.argv[2] || 'http://localhost:3030'
const SLIDES = 21

const browser = await chromium.launch()
const page = await browser.newPage({ viewport: { width: 1280, height: 800 } })

for (let n = 1; n <= SLIDES; n++) {
  await page.goto(`${BASE}/${n}`, { waitUntil: 'domcontentloaded' })
  await page.waitForTimeout(600)
  const report = await page.evaluate((slideNo) => {
    const layout = document.querySelector(`[data-slidev-no="${slideNo}"] .slidev-layout`)
    if (!layout) return { error: 'no layout' }
    const L = layout.getBoundingClientRect()
    const out = { titleLines: 0, orphans: [], overflow: null, clips: [] }
    const h1 = layout.querySelector('h1')
    if (h1) {
      const r = new Range()
      r.selectNodeContents(h1)
      out.titleLines = new Set(
        [...r.getClientRects()].filter((x) => x.width > 1).map((x) => Math.round(x.top)),
      ).size
      out.title = h1.textContent.trim()
    }
    for (const li of layout.querySelectorAll('li')) {
      const r = new Range()
      r.selectNodeContents(li)
      const rects = [...r.getClientRects()].filter((x) => x.width > 1)
      const tops = [...new Set(rects.map((x) => Math.round(x.top)))].sort((a, b) => a - b)
      if (tops.length > 1) {
        const w = (t) => rects.filter((x) => Math.round(x.top) === t).reduce((s, x) => s + x.width, 0)
        const frac = w(tops[tops.length - 1]) / w(tops[0])
        if (frac < 0.22)
          out.orphans.push({ frac: +frac.toFixed(2), text: li.textContent.trim().split(/\s+/).slice(0, 7).join(' ') })
      }
    }
    // lowest content bottom vs cite top
    const cite = layout.querySelector('.cite')
    if (cite) {
      const cT = cite.getBoundingClientRect().top
      let maxB = -1
      for (const el of layout.children) {
        if (el === cite || !el.getBoundingClientRect) continue
        maxB = Math.max(maxB, el.getBoundingClientRect().bottom)
      }
      out.gapToCitePx = +(((cT - maxB) * 552.25) / L.height).toFixed(1)
    }
    for (const v of layout.querySelectorAll('video.loop-media')) {
      const V = v.getBoundingClientRect()
      const sx = 980 / L.width
      const sy = 552.25 / L.height
      const k = 735.12 / 980
      out.clips.push({
        src: (v.currentSrc || v.querySelector('source')?.src || '').split('/').pop(),
        rectPt: [
          (V.left - L.left) * sx * k,
          414 - (V.bottom - L.top) * sy * k,
          (V.right - L.left) * sx * k,
          414 - (V.top - L.top) * sy * k,
        ].map((x) => +x.toFixed(1)),
      })
    }
    return out
  }, n)
  const flags = []
  if (report.titleLines > 1) flags.push(`TITLE ${report.titleLines} LINES`)
  if (report.orphans?.length) flags.push(`${report.orphans.length} orphan(s)`)
  if (report.gapToCitePx !== undefined && report.gapToCitePx < 4) flags.push(`cite gap ${report.gapToCitePx}px`)
  console.log(
    `slide ${String(n).padStart(2)}: ${flags.length ? `⚠ ${flags.join(', ')}` : 'ok'}` +
      (report.title ? `  | ${report.title.slice(0, 60)}` : ''),
  )
  for (const o of report.orphans || []) console.log(`    orphan(${o.frac}): ${o.text}…`)
  for (const c of report.clips || []) console.log(`    clip ${c.src}: rect ${JSON.stringify(c.rectPt)}`)
}
await browser.close()
