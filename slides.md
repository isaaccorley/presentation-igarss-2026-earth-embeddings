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

# Embedding products move model inference out of the user's workflow

NASA's EOSDIS alone holds <span class="hl">178.7 PB</span> of imagery and grows by 160 TB per day. Foundation models can summarize this archive, but every team re-downloads the same pixels and re-pays the same preprocessing and GPU inference. Embedding products run the model once and ship the vectors as reusable data.

<div style="width:88%; margin:0.7rem auto 0;">
<LoopVideo name="pipeline" />
</div>

<div class="cite">NASA ESDS annual metrics, FY2025 · Bommasani et al., 2021 — foundation model framing.</div>

---
layout: default
---

<span class="kicker">Motivation · practice</span>

# The model is not the map

<div class="cols2" style="margin-top:1rem; align-items:center;">
<div>

<div class="plot fig-ren-post"></div>

<p style="margin-top:1.3rem;">Four planted failure modes, <span class="hl">near-identical scores</span>, four visibly different maps. Ship the predictions and embeddings, not just the checkpoint — nobody knows a model better than the team that trained it.</p>

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

These are distributed as public weights (DOFA, OlmoEarth). Users manage preprocessing and GPU inference themselves. This is flexible but raises a hardware and engineering barrier.

</div>
<div>

## Embedding products (static data)

These are distributed as pre-computed vector archives (Google Satellite Embedding). The assets are frozen and versioned, so analysis proceeds without the model or its compute.

</div>
</div>

<p style="margin-top:1.2rem;">
A product is pinned to the data snapshot it was computed on, so <span class="hl">treating a product as a proxy for its model invites invalid generalization claims</span>.
</p>

<div class="cite">Fang, Stewart, Corley, Zhu, Azizpour — Earth Embeddings as Products, IGARSS 2026, §II.</div>

---
layout: default
---

<span class="kicker">Taxonomy</span>

# Three families: location, patch, and pixel embeddings

<div class="plot fig-types" style="height:19.5rem; margin-top:0.4rem;"></div>

<div class="cite">Stewart, Fang, Corley, Zhu — Earth Embeddings (book chapter, 2026), Fig. 1; figure design adapted from Klemmer et al., 2025 (EarthArXiv).</div>

---
layout: default
---

<span class="kicker">Landscape · 1 of 2</span>

# Patch products summarize km-scale tiles for retrieval

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

# Pixel products store one vector per pixel for each year

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

<span class="kicker">Ecosystem</span>

# Each product ships with its own formats, grids, and hosting

- Products are scattered across **Source Cooperative** (Clay, Earth Index), Hugging Face (Major TOM, Copernicus-Embed), Google Earth Engine (Google, Presto), and private university servers (Tessera).
- Formats range from **GeoParquet** to GeoTIFF with implicit CRS assumptions to raw NumPy arrays with no CRS or bounds ("numbers and a prayer").
- Each product defines its own **tiling grid** (Major TOM grid, MGRS, custom), so cross-product comparison starts with reprojection.
- **One flipped coordinate** in the Google Satellite Embedding rasters required patches to <span class="hl">GDAL, rasterio, and TorchGeo</span> before standard tools could read them.

Every team solves distribution independently. The integration tax is paid once per product, per user.

<div class="cite">Corley — The Technical Debt of Earth Embedding Products, cloudnativegeo.org, Feb 2026.</div>

---
layout: default
clicks: 1
---

<span class="kicker">Ecosystem · cost</span>

# Storage for one continent-year spans five orders of magnitude

<div style="width:63%; margin:0.4rem auto 0;">
<LoopVideo name="storage" />
</div>

Patch products stay in the MB–GB range, while dense 10 m pixel products reach tens of TB. A single full download of Presto's Africa coverage adds ~<span class="hl">$6.9k in egress</span> on top of storage.

<div class="cite">Earth Embeddings (book chapter, 2026), Table 8 — AWS S3 Standard, us-west-2 · egress from Corley, 2026.</div>

---
layout: default
---

<span class="kicker">Ecosystem · access</span>

# Hosting and format choices decide whether a product is usable

- **Hugging Face** enforces repo storage caps and API rate limits, so bulk pulls of TB-scale products throttle or fail.
- **Tessera** ships raw `.npy` tiles with coordinates and metadata in a sidecar file. NumPy supports no HTTP range requests, so reads pull whole tiles that a <span class="hl">COG or Zarr would stream</span> — GeoTIFF re-implemented without its streaming or metadata.
- **Google Satellite Embedding** was reachable only inside Earth Engine until **Taylor Geospatial rehosted it on Source Cooperative**, which adds free egress, an HTTP cross-region proxy, and CORS so browsers can stream it.
- Several products are so **sparse in space and time** that no common footprint exists for comparing them.

<div class="cite">Corley — The Technical Debt of Earth Embedding Products, cloudnativegeo.org, Feb 2026 · Google Satellite Embedding rehost: source.coop, 2026.</div>

---
layout: default
---

<span class="kicker">Ecosystem · reproducibility</span>

# Patch products are reproducible, but pixel models are often proprietary

- **Clay, Earth Index, and Copernicus-Embed** release the full pipeline (code, weights, data, embeddings) under permissive licenses.
- **Major TOM**'s CC-BY-SA pretraining data makes every derived embedding copyleft, which deters commercial users.
- **AlphaEarth Foundations and ESDNet** keep code and weights proprietary. The embeddings are CC-BY, but no one outside can regenerate or audit them.
- **No product ships checksummed data.** Upstream archives keep reprocessing imagery, so the exact training and inference inputs are already unrecoverable.

<div class="cite">Earth Embeddings (book chapter, 2026), Tables 4–6 — license provenance from data to weights to embeddings.</div>

---
layout: default
clicks: 1
---

<span class="kicker">Standardized access</span>

# TorchGeo treats embeddings as first-class geospatial datasets

<div class="cols2">
<div>

- TorchGeo has loaders for **every known embedding product**, plus the generating models and weights. **Presto and Tessera** were added upstream for this work.
- Reprojection, rasterization, spatiotemporal intersection, and sampling are built in.
- These workflows used to require **four or more repositories** and custom loaders. With TorchGeo each is about 20 lines of code.

</div>
<div style="margin-top:1.2rem;">
<LoopVideo name="search" />
</div>
</div>

<div class="cite">Stewart et al., 2025 — TorchGeo, ACM TSAS · Fang et al., IGARSS 2026, §IV.</div>

---
layout: default
class: codesm
---

<span class="kicker">Case studies</span>

# Search and land cover mapping in TorchGeo

<div class="cols2">
<div>

**Search and retrieval**: query by example

```python
# torchgeo.datasets / torchgeo.models
earthindex = EarthIndexEmbeddings('data/ei')
s2 = Sentinel2('data/s2')
image = s2[xmin:xmax, ymin:ymax]['image'] / 10_000

model = vit_small_patch14_dinov2(
    ViTSmall14_DINOv2_Weights.SENTINEL2_ALL_SOFTCON)
embed = model(image)

cos = CosineSimilarity(dim=0)
for sample in iter(earthindex):
    sim = cos(embed, sample['embedding'])
    ...  # keep the argmax, plot the match
```

</div>
<div>

**Land cover mapping**: crop types across Europe

```python
# torchgeo.datasets / torchgeo.samplers
tessera = TesseraEmbeddings('data/tessera')
eurocrops = EuroCrops('data/ec', download=True)
dataset = tessera & eurocrops  # intersection

train_roi = box(-10, 35, 10, 60)  # West EU
test_roi  = box( 10, 35, 30, 60)  # East EU
train_ds, test_ds = roi_split(
    dataset, [train_roi, test_roi])

# random patches -> fit a k-NN / linear probe
# gridded patches -> stitch a map of Europe
```

</div>
</div>

<div class="cite">Earth Embeddings (book chapter, 2026), §4 Listings 1–2 — abridged; geographic train/test splits are built in.</div>

---
layout: default
class: roomy left-table
---

<span class="kicker">Does it work?</span>

# Embeddings improve mapping tasks but degrade under spatial transfer

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

<span class="kicker">Guidance</span>

# Ship cloud-native formats, in-file metadata, and int8 vectors

<div class="cols2">
<div>

| Embedding type | Format |
|----------------|:-------|
| Location / implicit | ONNX or PyTorch |
| Patch / region | GeoParquet |
| Pixel, snapshot | GeoTIFF or GeoZarr |
| Pixel, time series | GeoZarr |

Ship a model card with sensors, temporal window, CRS and grid, dtype, quantization transform, and license. Store the metadata in the files, not the docs.

</div>
<div>

- **int8 quantization** has negligible accuracy cost. Google and Tessera already ship int8.
- **PCA to 64 dimensions with int8** gives 64× compression with <2% accuracy loss.
- **Binary quantization** adds another 32× and still recovers ~65% of float32 nearest neighbors, which is enough for candidate retrieval.
- Ship a **runnable benchmark**, not a private leaderboard.

</div>
</div>

<div class="cite">Earth Embeddings (book chapter, 2026), §7 · Corley & Robinson, 2026 — TerraBit compression study.</div>

---
layout: cover
class: cover
---

<span class="kicker">Takeaways</span>

# Embeddings are usable today; standards are the remaining work

<div style="font-size:0.95rem; line-height:1.75; margin-top:0.6rem; max-width:44rem;">
Pick the family by task: implicit for location context, patch for retrieval, pixel for dense mapping. Validate under geographic splits against simple baselines. Open problems are ocean and atmosphere coverage, uncertainty layers, and shared benchmarks (identical models differ by more than ten points across papers).
</div>

<div class="rule"></div>

<div style="font-family:'JetBrains Mono'; font-size:0.82rem; line-height:2.0;">
Chapter &nbsp;<span style="color:var(--accent2)">arxiv.org/abs/2608.03410</span><br>
Survey &nbsp;&nbsp;<span style="color:var(--accent2)">github.com/hfangcat/Awesome-Geospatial-Embeddings</span><br>
Code &nbsp;&nbsp;&nbsp;&nbsp;<span style="color:var(--accent2)">github.com/torchgeo/torchgeo</span><br>
Contact &nbsp;<span style="color:var(--accent2)">isaac.corley@taylorgeospatial.org</span>
</div>
