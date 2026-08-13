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

# Embeddings as Reusable Data

NASA's EOSDIS alone holds <span class="hl">178.7 PB</span> of imagery and grows by 160 TB per day. Analyses of this archive each repeat the same download, preprocessing, and GPU inference. An embedding product runs the model once and distributes the output vectors as data.

<div style="width:88%; margin:0.7rem auto 0;">
<LoopVideo name="pipeline" />
</div>

<div class="cite">NASA ESDS annual metrics, FY2025 · Bommasani et al., 2021 — foundation model framing.</div>

---
layout: default
clicks: 1
---

# The Earth as One Large Document

<div class="cols2" style="grid-template-columns: 1.15fr 1fr; align-items:center;">
<div>

Embedding retrieval matured in image search and in document retrieval for LLMs (RAG). The pipeline splits a corpus into chunks, embeds each chunk, and indexes the vectors for search.

For the Earth archive, the chunk is not well defined:

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

# Three Families of Earth Embeddings

<div class="plot fig-types" style="height:19.5rem;"></div>

<div class="cite">Stewart, Fang, Corley, Zhu — Earth Embeddings (book chapter, 2026), Fig. 1; figure design adapted from Klemmer et al., 2025 (EarthArXiv).</div>

---
layout: default
---

# Patch Embedding Products

<div class="note">All known patch embedding products as of July 2026. *sparse spatial or temporal coverage.</div>

| Product | Extent | Resolution | Years | Dim. | Dtype |
|---------|--------|-----------:|------:|-----:|:------|
| MOSAIKS (2021–25) | USA / Global | 1 km / 0.01° | 2018 / 2019 | 8192 / 4000 | float32 |
| Clay v0 / v1.5 (2024–26) | USA / Global | 154 m – 5.12 km | 2010–2025* | 768–1024 | float32 |
| Major TOM (2024–26) | Global* | 120 m – 3.84 km | 2016–2024* | 256–2048 | float32 |
| Earth Index (2025) | Global | 320 m | 2024 | 384 | float32 |
| Copernicus-Embed (2025) | Global | 0.25° | 2021 | 768 | float32 |

**Major TOM** is the largest family, with more than a dozen model variants on one shared grid. All patch products store float32. One vector summarizes an entire mosaic tile, which suits retrieval more than dense mapping.

<div class="cite">Earth Embeddings (book chapter, 2026), Table 2 — abridged to family level.</div>

---
layout: default
---

# Pixel Embedding Products

<div class="note">All known pixel embedding products as of July 2026. Every product is built from annual time series. *sparse coverage.</div>

| Product | Extent | Resolution | Years | Dim. | Dtype |
|---------|--------|-----------:|------:|-----:|:------|
| Presto Embeddings (2025) | Togo | 10 m | 2019–2020 | 128 | uint16 |
| Tessera Embeddings (2025) | Global* | 10 m | 2017–2025* | 128 | int8 → float32 |
| Google Satellite Embedding (2025) | Global | 10 m | 2017–2025 | 64 | int8 → float64 |
| Embedded Seamless Data (2026) | Global | 30 m | 2000–2024 | 12 | uint16 → float32 |

**Google Satellite Embedding** covers the full Sentinel era at 64 dimensions. **Embedded Seamless Data** trades resolution for 25 years of Landsat history. The int8 and uint16 dtypes reduce storage at these volumes.

<div class="cite">Earth Embeddings (book chapter, 2026), Table 3.</div>

---
layout: default
---

# Commercial Embedding Products and Services

<div class="cols3 industry">
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

# Fragmented Formats, Grids, and Hosting

- Products are scattered across **Source Cooperative** (Clay, Earth Index), Hugging Face (Major TOM), Earth Engine (Google, Presto), and private servers (Tessera).
- Formats span **GeoParquet**, GeoTIFF with an assumed CRS, and ungeoreferenced NumPy arrays.
- Each product defines its own **tiling grid**, so any cross-product comparison starts with reprojection.
- **One flipped coordinate** in the Google rasters forced fixes in <span class="hl">GDAL, rasterio, and TorchGeo</span>.

Each producer distributes differently, so integration effort is repeated for each product and each user.

<div class="cite">Corley — The Technical Debt of Earth Embedding Products, cloudnativegeo.org, Feb 2026.</div>

---
layout: default
clicks: 1
---

# Storage and Egress Costs

<div style="width:57%; margin-left:auto; margin-right:auto;">
<LoopVideo name="storage" />
</div>

Patch products stay in the MB–GB range, while dense 10 m pixel products reach tens of TB. A single full download of Presto's Africa coverage adds ~<span class="hl">$6.9k in egress</span> on top of storage.

<div class="cite">Earth Embeddings (book chapter, 2026), Table 8 — AWS S3 Standard, us-west-2 · egress from Corley, 2026.</div>

---
layout: default
---

# Hosting and Format Barriers

- **Hugging Face** enforces storage caps and API rate limits, so TB-scale downloads throttle or fail.
- **Tessera** distributes `.npy` tiles plus a metadata sidecar. NumPy arrays do not support HTTP range requests, so reads download whole tiles that a <span class="hl">COG or Zarr would stream</span>.
- The **AlphaEarth embeddings** were available only through Earth Engine or a requester-pays bucket. **Taylor Geospatial rehosted them in a non-requester-pays bucket on Source Cooperative**, with free egress, HTTP range reads, and CORS for browser streaming.
- Several products are so **sparse in space and time** that no common footprint exists for comparison.

<div class="cite">Corley — The Technical Debt of Earth Embedding Products, cloudnativegeo.org, Feb 2026 · AEF rehost: source.coop, 2026.</div>

---
layout: default
---

# Reproducibility and Licensing

- **Clay, Earth Index, and Copernicus-Embed** release code, weights, and data openly.
- **Tessera** releases code, weights, and embeddings openly, but records <span class="hl">no metadata about which inputs built each tile</span>, so its outputs cannot be audited.
- **Major TOM**'s CC-BY-SA training data makes its embeddings copyleft, deterring commercial use.
- **AlphaEarth and ESDNet** publish CC-BY embeddings but keep code and weights proprietary.
- **No product provides checksums.** Reprocessed archives make the exact inputs unrecoverable.

<div class="cite">Earth Embeddings (book chapter, 2026), Tables 4–6 — license provenance from data to weights to embeddings.</div>

---
layout: default
---

# Foundation Models vs. Embedding Products

<div class="cols2">
<div>

## Foundation models

Distributed as public weights (DOFA, OlmoEarth). Users manage preprocessing and GPU inference themselves. This is flexible but raises a hardware and engineering barrier.

</div>
<div>

## Embedding products

Distributed as pre-computed vector archives (Google Satellite Embedding). The assets are frozen and versioned, so analysis proceeds without the model or its compute.

</div>
</div>

<p style="margin-top:1.2rem;">
A product is pinned to the data snapshot it was computed on, so <span class="hl">results measured on a product do not generalize to the model behind it</span>.
</p>

<div class="cite">Fang, Stewart, Corley, Zhu, Azizpour — Earth Embeddings as Products, IGARSS 2026, §II.</div>

---
layout: default
---

# Paper Metrics vs. Product Metrics

<div style="max-width:46.5rem; font-size:1.12em; line-height:1.6;">

The AlphaEarth and Tessera papers report benchmark numbers from internal pipelines. The same tasks, evaluated on the <span class="hl">released annual embedding products</span>, give different numbers.

- The papers embed **exact input stacks**. The products are **annual composites** over reprocessed archives.
- Product benchmarks should describe the **downloadable data**.

</div>

<div class="cite">Earth Embeddings (book chapter, 2026), §5 · Corley et al., 2026 — EuroSAT-Embed re-evaluation of AlphaEarth, Tessera, OlmoEarth.</div>

---
layout: default
---

# No One Knows the SOTA in GFMs

<div class="cols2" style="grid-template-columns: 1.35fr 1fr; align-items:center;">
<div>

An audit of 152 geospatial foundation model papers found **46 cross-paper disagreements of ≥10 points** for the same model, benchmark, and protocol.

94 of 126 papers use a pretraining configuration that appears in no other paper. **39% release no weights**, so their results cannot be re-run.

We built **torchgeo-bench**, a maintained harness for frozen backbones with shared datasets, consistent probes, and bootstrapped confidence intervals.

</div>
<div class="plot paperpage fig-nooneknows" style="height:19rem;"></div>
</div>

<div class="cite">Corley et al., 2026 — No One Knows the SOTA in GFMs, arXiv:2605.12678 · torchgeo.org/torchgeo-bench.</div>

---
layout: default
---

# Fusing Multiple Products

<div class="cols2" style="grid-template-columns: 1.35fr 1fr; align-items:center;">
<div>

You do not have to pick one product.

Fusing AlphaEarth, Tessera, GeoCLIP, and SatCLIP beats the best single product on <span class="hl">4 of 6 downstream tasks</span>.

Which products complement each other depends on the task and region, so a probe trained on the concatenated embeddings is a cheap first experiment.

</div>
<div class="plot paperpage fig-bettertogether" style="height:19rem;"></div>
</div>

<div class="cite">van der Plas et al., 2026 — Better Together, arXiv:2605.18667.</div>

---
layout: default
---

# Open Research Directions

<div class="cols2" style="grid-template-columns: 1.2fr 1fr; align-items:center;">
<div>

- **Quantization.** Google and Tessera use int8 at no measurable cost. Binary recovers ~65% of float32 nearest neighbors.
- **Disentangled representations.** VAE-style training gives each dimension a separate meaning. Not yet applied to Earth embeddings.
- **Matryoshka learning.** Tessera v2, Clay, and our **MIND location encoder** train nested dimensions, so users truncate to their budget.

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

# Compressed Embeddings in the Browser

<div class="cols2">
<div>

<div style="width:88%; margin:0 auto;"><LoopVideo name="terrabit" /></div>

<p class="democap"><strong>TerraBit</strong> — 50M Clay v1.5 patches binarized to 128 bytes each and streamed from Source Cooperative. Hamming search runs in a Web Worker with no backend.<br><span class="demolink">isaac.earth/terrabit</span></p>

</div>
<div>

<div style="width:88%; margin:0 auto;"><LoopVideo name="deltabit" /></div>

<p class="democap"><strong>DeltaBit</strong> — AlphaEarth pixel differences at 8 bytes per pixel (PCA-8 + int8) as XYZ GeoTIFF tiles. The user labels, trains, and maps change in the browser (Seattle, 2020 → 2024).<br><span class="demolink">calebrob.com/deltabit</span></p>

</div>
</div>

<div class="cite">Corley & Robinson — TerraBit · Robinson & Corley — DeltaBit, geospatialml.com, Apr 2026 · embeddings hosted on source.coop.</div>

---
layout: default
class: bigtable
---

# Recommendations for Producers

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

- Provide a **model card**: sensors, time window, CRS, grid, dtype, license.
- Store metadata **inside the files** rather than in separate docs.
- **int8 by default**; PCA to 64 dims costs <2% accuracy for 64× compression.
- **Runnable benchmarks** instead of leaderboards.

</div>
</div>

<div class="cite">Earth Embeddings (book chapter, 2026), §7 · Corley & Robinson, 2026 — TerraBit compression study.</div>

---
layout: cover
class: cover
---

# Takeaways and Open Problems

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
