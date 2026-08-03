# Earth Embeddings as Products — IGARSS 2026 talk
# bun for JS, manim for the loop clips, pikepdf for the video-embedded PDF.

MANIM ?= manim

.PHONY: dev build export clips posters pdf-animated lint

dev:
	bun run dev

build:
	bun run build

# Static PDF (posters shown where the web build plays loops).
# Lands in public/ so the deployed site serves it ("View as PDF").
export:
	bun run export

# Re-render the three loop clips and refresh public/ + poster frames
clips:
	$(MANIM) render --fps 30 --resolution 1920,720  -o loop-pipeline.mp4 clips/clips.py PipelineLoop
	$(MANIM) render --fps 30 --resolution 1440,1080 -o loop-search.mp4   clips/clips.py SearchLoop
	$(MANIM) render --fps 30 --resolution 1920,860  -o loop-storage.mp4  clips/clips.py StorageBars
	cp -f media/videos/clips/720p30/loop-pipeline.mp4 media/videos/clips/1080p30/loop-search.mp4 media/videos/clips/860p30/loop-storage.mp4 public/
	$(MAKE) posters

posters:
	for c in pipeline search storage; do \
	  ffmpeg -y -sseof -1.0 -i public/loop-$$c.mp4 -update 1 -frames:v 1 assets/posters/poster-$$c.png; \
	done
	cp -f assets/posters/poster-*.png public/

# PDF with playable embedded loops (RichMedia; plays in Adobe Acrobat)
pdf-animated: export
	uv run scripts/embed_videos.py public/earth-embeddings-igarss2026.pdf earth-embeddings-igarss2026-animated.pdf

lint:
	bun run lint
