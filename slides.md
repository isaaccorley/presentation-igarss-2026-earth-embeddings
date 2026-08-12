---
theme: default
title: 'Earth Embeddings as Products — IGARSS 2026'
colorSchema: light
highlighter: shiki
lineNumbers: false
fonts:
  serif: 'Source Serif 4'
  mono: JetBrains Mono
  italic: true
transition: none
controls: false
progress: false
layout: cover
class: cover
---

<span class="kicker">IGARSS 2026</span>

# Earth Embeddings as Products

<div style="font-size:1.25rem; font-weight:500; line-height:1.3; margin:0.4rem 0 0; color:var(--ink);">
Taxonomy, Ecosystem, and Standardized Access
</div>

<div class="rule"></div>

<div style="font-size:0.92rem; line-height:1.75;">
Heng Fang<span class="muted">* — KTH Royal Institute of Technology</span><br>
Adam J. Stewart<span class="muted">* — Technical University of Munich</span><br>
<u>Isaac Corley</u><span class="muted"> — Taylor Geospatial</span><br>
Xiao Xiang Zhu<span class="muted"> — Technical University of Munich</span><br>
Hossein Azizpour<span class="muted"> — KTH Royal Institute of Technology</span>
</div>

<div class="note" style="margin-top:1.1rem;">
*equal contribution &nbsp;·&nbsp; since expanded into the book chapter <em>Earth Embeddings</em> (arXiv, August 2026)
</div>

<PdfLink />

---
layout: default
clicks: 1
---

<span class="kicker">Motivation</span>

# Run the model once, reuse the vectors

NASA's EOSDIS alone holds <span class="hl">178.7 PB</span> of imagery and grows by 160 TB per day. Every team re-downloads the same pixels and re-pays the same preprocessing and GPU inference. Embedding products run the model once and distribute the vectors as reusable data.

<div style="width:88%; margin:0.7rem auto 0;">
<LoopVideo name="pipeline" />
</div>

<div class="cite">NASA ESDS annual metrics, FY2025 · Bommasani et al., 2021 — foundation model framing.</div>

---
layout: default
clicks: 1
---

<span class="kicker">Motivation · retrieval</span>

# The Earth is one large document

<div class="cols2" style="grid-template-columns: 1.15fr 1fr; margin-top:0.5rem; align-items:center;">
<div>

Embedding retrieval matured in image search and in document retrieval for LLMs (RAG). The recipe is to chunk, embed, index, and retrieve. The Earth archive is one enormous document.

But there is no obvious chunk:

<div class="qgrid">
<div>What is the <strong>spatial extent</strong> of a chunk?</div>
<div>What is the <strong>resolution</strong> of each point in it?</div>
<div>One <strong>timestamp</strong>, or a time series?</div>
<div>Which <strong>signal</strong> (MSI band, SAR, elevation)?</div>
</div>

</div>
<div style="margin-top:0.2rem;">
<LoopVideo name="search" />
</div>
</div>

<div class="cite">Lewis et al., 2020 — retrieval-augmented generation · clip: query-by-example over a patch embedding product.</div>

---
layout: default
---

<span class="kicker">Motivation · practice</span>

# The model is not the map

<div class="cols2" style="margin-top:0.6rem; align-items:center;">
<div>

<div class="plot fig-ren-post" style="width:92%;"></div>

<p style="margin-top:0.9rem;">Ren corrupts one land cover map four ways. Every version scores <span class="hl">F1 ≈ 0.73–0.74</span>, but each error is obvious on the map. Release predictions and embeddings alongside checkpoints. Nobody knows a model better than the team that trained it.</p>

</div>
<div class="plot fig-ren-quartet" style="height:19rem;"></div>
</div>

<div class="cite">Ren — The Model is not the Map, christopherren.substack.com, Jun 2025 · Dynamic World built-area maps over Santa Fe, NM.</div>

---
layout: default
---

<span class="kicker">Scope</span>

# A foundation model is not an embedding product

<div class="cols2" style="margin-top:0.9rem;">
<div>

## Foundation models (dynamic inference)

Distributed as public weights (DOFA, OlmoEarth). Users manage preprocessing and GPU inference themselves. This is flexible but raises a hardware and engineering barrier.

</div>
<div>

## Embedding products (static data)

Distributed as pre-computed vector archives (Google Satellite Embedding). The assets are frozen and versioned, so analysis proceeds without the model or its compute.

</div>
</div>

<p style="margin-top:1.2rem;">
A product is pinned to the data snapshot it was computed on, so <span class="hl">treating a product as a proxy for its model invites invalid generalization claims</span>.
</p>

<div class="cite">Fang, Stewart, Corley, Zhu, Azizpour — Earth Embeddings as Products, IGARSS 2026, §II.</div>

---
layout: default
---

<span class="kicker">Scope · reproducibility</span>

# Paper metrics do not reproduce from the products

The AlphaEarth and Tessera papers report benchmark numbers from internal pipelines. The same tasks, evaluated on the <span class="hl">released annual embedding products</span>, give different numbers.

- The papers embed **exact input stacks**. The products are **annual composites** over reprocessed archives.
- Benchmark numbers for a product should describe the **downloadable data**, not the model behind it.

<div class="cite">Earth Embeddings (book chapter, 2026), §5 · Corley et al., 2026 — EuroSAT-Embed re-evaluation of AlphaEarth, Tessera, OlmoEarth.</div>

---
layout: default
---

<span class="kicker">Taxonomy</span>

# Three families of Earth embeddings

<div class="plot fig-types" style="height:19.5rem; margin-top:0.4rem;"></div>

<div class="cite">Stewart, Fang, Corley, Zhu — Earth Embeddings (book chapter, 2026), Fig. 1; figure design adapted from Klemmer et al., 2025 (EarthArXiv).</div>

---
layout: default
---

<span class="kicker">Landscape · 1 of 2</span>

# Patch products summarize km-scale tiles

<div class="note">All known patch embedding products as of July 2026. *sparse spatial or temporal coverage.</div>

| Product | Extent | Resolution | Years | Dim. | Dtype |
|---------|--------|-----------:|------:|-----:|:------|
| MOSAIKS (2021–25) | USA / Global | 1 km / 0.01° | 2018 / 2019 | 8192 / 4000 | float32 |
| Clay v0 / v1.5 (2024–26) | USA / Global | 154 m – 5.12 km | 2010–2025* | 768–1024 | float32 |
| Major TOM (2024–26) | Global* | 120 m – 3.84 km | 2016–2024* | 256–2048 | float32 |
| Earth Index (2025) | Global | 320 m | 2024 | 384 | float32 |
| Copernicus-Embed (2025) | Global | 0.25° | 2021 | 768 | float32 |

**Major TOM** is the largest family, with more than a dozen model variants on one shared grid. Every product stores float32. One vector summarizes an entire mosaic tile, which suits retrieval more than dense mapping.

<div class="cite">Earth Embeddings (book chapter, 2026), Table 2 — abridged to family level.</div>

---
layout: default
---

<span class="kicker">Landscape · 2 of 2</span>

# Pixel products store a vector per pixel-year

<div class="note">All known pixel embedding products as of July 2026. Every product is built from annual time series. *sparse coverage.</div>

| Product | Extent | Resolution | Years | Dim. | Dtype |
|---------|--------|-----------:|------:|-----:|:------|
| Presto Embeddings (2025) | Togo | 10 m | 2019–2020 | 128 | uint16 |
| Tessera Embeddings (2025) | Global* | 10 m | 2017–2025* | 128 | int8 → float32 |
| Google Satellite Embedding (2025) | Global | 10 m | 2017–2025 | 64 | int8 → float64 |
| Embedded Seamless Data (2026) | Global | 30 m | 2000–2024 | 12 | uint16 → float32 |

**Google Satellite Embedding** covers the full Sentinel era at 64 dimensions. **Embedded Seamless Data** trades resolution for 25 years of Landsat history. Storage pressure drives the int8 and uint16 dtypes.

<div class="cite">Earth Embeddings (book chapter, 2026), Table 3.</div>

---
layout: default
---

<span class="kicker">Landscape · industry</span>

# Industry is selling embeddings as the product

<div class="cols3 industry" style="margin-top:1.3rem;">
<div>

## Descartes Labs <span class="muted">2017</span>

**GeoVisual Search** was the first planet-scale visual search over satellite imagery features. A query patch of a wind turbine returns wind turbines worldwide. It predates the current products by eight years.

</div>
<div>

## Earth Genome <span class="muted">2025</span>

**Earth Index** packages Clay embeddings on Source Cooperative into a search service for investigative journalists and conservation teams, who use it to find mining sites, airstrips, and feedlots.

</div>
<div>

## LGND <span class="muted">2025</span>

Raised **$9M** in 2025 to build services on geographic embeddings, and published the full global Clay v1.5 float32 corpus on Source Cooperative.

</div>
</div>

<p style="margin-top:1.3rem;">All three build their products on the embeddings rather than the model weights.</p>

<div class="cite">TechCrunch, Mar 2017 — GeoVisual Search · Ingold — Embeddings for All, Earth Genome, 2025 · LGND seed round, PR Newswire, Jul 2025.</div>

---
layout: default
---

<span class="kicker">Ecosystem</span>

# Formats, grids, and hosting differ per product

- Products are scattered across **Source Cooperative** (Clay, Earth Index), Hugging Face (Major TOM), Earth Engine (Google, Presto), and private servers (Tessera).
- Formats span **GeoParquet**, GeoTIFF with implicit CRS assumptions, and raw NumPy arrays with no CRS or bounds ("numbers and a prayer").
- Each product defines its own **tiling grid**, so any cross-product comparison starts with reprojection.
- **One flipped coordinate** in the Google rasters required patches to <span class="hl">GDAL, rasterio, and TorchGeo</span>.

Every team solves distribution independently. The integration tax is paid once per product, per user.

<div class="cite">Corley — The Technical Debt of Earth Embedding Products, cloudnativegeo.org, Feb 2026.</div>

---
layout: default
clicks: 1
---

<span class="kicker">Ecosystem · cost</span>

# Storage costs span five orders of magnitude

<div style="width:57%; margin:0.1rem auto 0;">
<LoopVideo name="storage" />
</div>

Patch products stay in the MB–GB range, while dense 10 m pixel products reach tens of TB. A single full download of Presto's Africa coverage adds ~<span class="hl">$6.9k in egress</span> on top of storage.

<div class="cite">Earth Embeddings (book chapter, 2026), Table 8 — AWS S3 Standard, us-west-2 · egress from Corley, 2026.</div>

---
layout: default
---

<span class="kicker">Ecosystem · access</span>

# Hosting and format choices decide usability

- **Hugging Face** enforces storage caps and API rate limits, so bulk pulls of TB-scale products throttle or fail.
- **Tessera** distributes `.npy` tiles plus a metadata sidecar. NumPy has no HTTP range requests, so reads pull whole tiles that a <span class="hl">COG or Zarr would stream</span>. It is GeoTIFF without the streaming or the metadata.
- The **AlphaEarth embeddings** were available only through Earth Engine or a requester-pays bucket, where the reader pays the egress. **Taylor Geospatial rehosted them in a non-requester-pays bucket on Source Cooperative**, with free egress, HTTP range reads, and CORS for browser streaming.
- Several products are so **sparse in space and time** that no common footprint exists for comparison.

<div class="cite">Corley — The Technical Debt of Earth Embedding Products, cloudnativegeo.org, Feb 2026 · AEF rehost: source.coop, 2026.</div>

---
layout: default
---

<span class="kicker">Ecosystem · reproducibility</span>

# No product is fully reproducible

- **Clay, Earth Index, and Copernicus-Embed** release code, weights, and data under permissive licenses.
- **Tessera** releases code, weights, and embeddings openly, but records <span class="hl">no metadata about which inputs built each tile</span>, so its outputs cannot be audited.
- **Major TOM**'s CC-BY-SA pretraining data makes its embeddings copyleft, deterring commercial users.
- **AlphaEarth and ESDNet** keep code and weights proprietary. The embeddings are CC-BY, but no one outside can regenerate them.
- **No product provides checksums.** Archives keep reprocessing imagery; exact inputs are unrecoverable.

<div class="cite">Earth Embeddings (book chapter, 2026), Tables 4–6 — license provenance from data to weights to embeddings.</div>

---
layout: default
class: roomy left-table
---

<span class="kicker">Does it work?</span>

# Embeddings improve mapping, not spatial transfer

| Task | Embeddings | Finding |
|------|------------|---------|
| Cropland mapping, Togo | Presto, Google | Presto + Random Forest gives the best F1 |
| Tree species, Dutch forest inventory | Presto, Google, Tessera | +2–9 points over hand-designed time-series features |
| Landslide susceptibility, TW·HK·IT | Google | 64-d embeddings beat conventional conditioning factors |
| Poverty mapping, Sub-Saharan Africa | Google + GNN | large storage/preprocessing savings vs. raw Sentinel-2 |
| Scene classification, EuroSAT-Embed | Google, Tessera, OlmoEarth | pooling choice cuts the geographic gap by >50% |
| Fusion across six tasks | Google, Tessera, GeoCLIP, SatCLIP | fused embeddings beat the best single model in 4 of 6 |

Performance drops under **spatial transfer**, and annual composites wash out sub-annual dynamics. Validate with geographic splits and simple baselines before trusting any product.

<div class="cite">Zvonkov et al., 2025 · Ishikawa et al., 2025 · Cheng et al., 2026 · Pettersson & Daoud, 2025 · Corley et al., 2026 · van der Plas et al., 2026 · Ma et al., 2026.</div>

---
layout: default
---

<span class="kicker">Guidance · choosing</span>

# No one knows which product is best for your task

<div class="cols2" style="grid-template-columns: 1.35fr 1fr; margin-top:0.5rem; align-items:center;">
<div>

An audit of 152 geospatial foundation model papers found **46 cross-paper disagreements of ≥10 points** for the same model, benchmark, and protocol.

94 of 126 papers use a pretraining configuration no other paper uses. **39% release no weights**, so their results cannot be re-run at all.

We built **torchgeo-bench**, a maintained harness for frozen backbones with shared datasets, consistent probes, and bootstrapped confidence intervals.

</div>
<div class="plot paperpage fig-nooneknows" style="height:19rem;"></div>
</div>

<div class="cite">Corley et al., 2026 — No One Knows the SOTA in GFMs, arXiv:2605.12678 · torchgeo.org/torchgeo-bench.</div>

---
layout: default
---

<span class="kicker">Guidance · combining</span>

# Products are complementary

<div class="cols2" style="grid-template-columns: 1.35fr 1fr; margin-top:0.5rem; align-items:center;">
<div>

You do not have to pick one product.

Fusing AlphaEarth, Tessera, GeoCLIP, and SatCLIP beats the best single product on <span class="hl">4 of 6 downstream tasks</span>.

Complementarity is task- and location-dependent, so a concatenated probe is a cheap first experiment before committing to one product.

</div>
<div class="plot paperpage fig-bettertogether" style="height:19rem;"></div>
</div>

<div class="cite">van der Plas et al., 2026 — Better Together, arXiv:2605.18667.</div>

---
layout: default
---

<span class="kicker">Open problems</span>

# Smaller, sliceable vectors are underexplored

<div class="cols2" style="grid-template-columns: 1.2fr 1fr; margin-top:0.6rem; align-items:center;">
<div>

- **Quantization.** Google and Tessera use int8 at no measurable cost. Nothing goes lower, yet binary recovers ~65% of float32 nearest neighbors.
- **Disentangled representations.** VAE-style training gives each dimension a separate meaning. Untried for Earth embeddings.
- **Matryoshka learning.** Tessera v2, Clay, and our **MIND location encoder** train nested dimensions, so users truncate to their budget. No other products do.

</div>
<div class="matryoshka">
<div class="mrow"><div class="mbar" style="width:100%; background:#D95F0E;"></div><span>full width</span></div>
<div class="mrow"><div class="mbar" style="width:50%; background:#EC8C3C;"></div><span>1/2</span></div>
<div class="mrow"><div class="mbar" style="width:25%; background:#F7B26A;"></div><span>1/4</span></div>
<div class="mrow"><div class="mbar" style="width:12.5%; background:#FCD39E;"></div><span>1/8</span></div>
<div class="mnote">the leading dimensions form a usable embedding at any width</div>
</div>
</div>

<div class="cite">Kusupati et al., 2022 — Matryoshka representation learning · Corley & Robinson, 2026 — Compressing Earth Embeddings · MIND: Corley et al., 2026.</div>

---
layout: default
clicks: 1
class: demos
---

<span class="kicker">Demos</span>

# Compressed embeddings run in the browser

<div class="cols2" style="margin-top:0.3rem;">
<div>

<div style="width:88%; margin:0 auto;"><LoopVideo name="terrabit" /></div>

<p class="democap"><strong>TerraBit</strong> — 50M Clay v1.5 patches binarized to 128 bytes each, streamed from a static Source Cooperative bucket. Hamming search runs in a Web Worker with no backend or API.</p>

</div>
<div>

<div style="width:88%; margin:0 auto;"><LoopVideo name="deltabit" /></div>

<p class="democap"><strong>DeltaBit</strong> — AlphaEarth pixel differences at 8 bytes per pixel (PCA-8 + int8) as XYZ GeoTIFF tiles. The user labels, trains, and maps change in the browser (Seattle, 2020 → 2024).</p>

</div>
</div>

<div class="cite">Corley & Robinson — TerraBit · Robinson & Corley — DeltaBit, geospatialml.com, Apr 2026 · embeddings hosted on source.coop.</div>

---
layout: default
---

<span class="kicker">Guidance</span>

# Streamable formats, embedded metadata, and int8

<div class="cols2">
<div>

| Embedding type | Format |
|----------------|:-------|
| Location / implicit | ONNX or PyTorch |
| Patch / region | GeoParquet |
| Pixel, snapshot | GeoTIFF or GeoZarr |
| Pixel, time series | GeoZarr |

</div>
<div>

- Provide a **model card**: sensors, temporal window, CRS, grid, dtype, quantization, license.
- Store metadata **inside the files** rather than in separate docs.
- **int8 by default**; PCA to 64 dims costs <2% accuracy for 64× compression.
- **Runnable benchmarks**, not leaderboards.

</div>
</div>

<div class="cite">Earth Embeddings (book chapter, 2026), §7 · Corley & Robinson, 2026 — TerraBit compression study.</div>

---
layout: cover
class: cover
---

<span class="kicker">Closing</span>

# Takeaways and open problems

<div style="font-size:0.95rem; line-height:1.75; margin-top:0.6rem; max-width:44rem;">
Pick the family by task: implicit for location context, patch for retrieval, pixel for dense mapping. Validate under geographic splits against simple baselines, and consider fusing products instead of picking one. Open problems are standardized formats and provenance, ocean and atmosphere coverage, uncertainty layers, and shared benchmarks (identical models differ by more than ten points across papers).
</div>

<div class="rule"></div>

<div style="display:flex; align-items:center; gap:2.4rem;">
<div style="font-family:'JetBrains Mono'; font-size:0.82rem; line-height:2.0;">
Chapter &nbsp;<span style="color:var(--accent2)">arxiv.org/abs/2608.03410</span><br>
Survey &nbsp;&nbsp;<span style="color:var(--accent2)">github.com/hfangcat/Awesome-Geospatial-Embeddings</span><br>
Bench &nbsp;&nbsp;&nbsp;<span style="color:var(--accent2)">torchgeo.org/torchgeo-bench</span><br>
Contact &nbsp;<span style="color:var(--accent2)">isaac.corley@taylorgeospatial.org</span>
</div>
<div>
<div class="qr-slides"></div>
<div style="font-family:'JetBrains Mono'; font-size:0.68rem; margin-top:0.4rem; text-align:center;">these slides</div>
</div>
</div>
