# Earth Embeddings as Products — IGARSS 2026

Slides for the IGARSS 2026 talk *Earth Embeddings as Products: Taxonomy,
Ecosystem, and Standardized Access* (Fang, Stewart, Corley, Zhu, Azizpour),
covering the expanded book chapter *Earth Embeddings* (Stewart, Fang, Corley,
Zhu; arXiv, August 2026) and the analysis in
[The Technical Debt of Earth Embedding Products](https://cloudnativegeo.org/blog/2026/02/the-technical-debt-of-earth-embedding-products/).

Built with [Slidev](https://sli.dev). The three looping illustration clips are
rendered with [Manim](https://www.manim.community/) from `clips/clips.py`.

## Develop

```bash
bun install
bun run dev        # live dev server
bun run lint       # biome
make clips         # re-render the manim loops (needs manim + ffmpeg)
```

## Deliverables

```bash
bun run export     # earth-embeddings-igarss2026.pdf (static, poster frames)
make pdf-animated  # earth-embeddings-igarss2026-animated.pdf (clips embedded)
```

The animated PDF carries the mp4 loops as RichMedia annotations: they
autoplay in Adobe Acrobat / Acrobat Reader; every other viewer (Preview,
browsers) falls back to the poster frame painted on the page.

The web deck deploys to GitHub Pages on push to `main`
(`.github/workflows/deploy.yml`), where the clips play as looping videos.
