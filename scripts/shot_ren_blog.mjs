// One-off: capture slide assets from Ren's "The Model is Not the Map" post.
// Usage: node scripts/shot_ren_blog.mjs
import { chromium } from 'playwright-chromium'

const URL = 'https://christopherren.substack.com/p/the-model-is-not-the-map'

const browser = await chromium.launch()
const page = await browser.newPage({
  viewport: { width: 1400, height: 2400 },
  deviceScaleFactor: 2,
})
await page.goto(URL, { waitUntil: 'domcontentloaded' })
await page.waitForSelector('h1.post-title')
await page.waitForTimeout(2500)

// kill subscribe modals / popups
await page.evaluate(() => {
  for (const sel of ['[class*="modal"]', '[class*="popup"]', '[data-testid*="modal"]', '.fancy-portal'])
    document.querySelectorAll(sel).forEach((el) => el.remove())
  document.body.style.overflow = 'auto'
})

// 1) post header card: title through the TLDR bullet list
const h1 = page.locator('h1.post-title').first()
const box = await h1.boundingBox()
const tldrEnd = await page.evaluate(() => {
  const lists = [...document.querySelectorAll('.available-content ul')]
  return lists.length ? lists[0].getBoundingClientRect().bottom + window.scrollY : null
})
await page.screenshot({
  path: 'assets/ren-post-header.png',
  clip: { x: box.x - 8, y: box.y - 10, width: box.width + 16, height: tldrEnd - box.y + 18 },
})

// 2) the Santa Fe Quartet figure (largest content image on the page)
const imgs = page.locator('.available-content img')
const n = await imgs.count()
let best = null
let bestArea = 0
for (let i = 0; i < n; i++) {
  const b = await imgs.nth(i).boundingBox()
  const alt = (await imgs.nth(i).getAttribute('src')) || ''
  if (b && b.width * b.height > bestArea && b.height > b.width * 0.5) {
    bestArea = b.width * b.height
    best = i
  }
}
// grab the original CDN asset instead of screenshotting page pixels
// (substack's lightbox dims the whole page while it is armed)
const src = await imgs.nth(best).getAttribute('src')
const resp = await page.request.get(src)
const { writeFileSync } = await import('node:fs')
writeFileSync('assets/ren-quartet.png', await resp.body())

console.log('saved assets/ren-post-header.png and assets/ren-quartet.png')
await browser.close()
