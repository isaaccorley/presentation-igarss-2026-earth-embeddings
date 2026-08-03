# /// script
# requires-python = ">=3.10"
# dependencies = ["pikepdf>=9"]
# ///
"""Embed the loop clips into the exported deck as RichMedia annotations.

Produces a PDF whose clips autoplay in Adobe Acrobat / Acrobat Reader
(native MP4 player, page-open activation). Other viewers (Preview,
browsers) ignore the annotation and show the poster frame already
painted on the page, so the file degrades gracefully.

Rects were measured from the export (735.12 x 414 pt pages) by
outlining the poster divs; re-measure if slide layout changes.

Usage: uv run scripts/embed_videos.py <in.pdf> <out.pdf>
"""

import sys

import pikepdf
from pikepdf import Array, Dictionary, Name, Pdf, String

# (0-based page index, mp4 path, rect in PDF points [x0, y0, x1, y1])
CLIPS = [
    (1, "public/loop-pipeline.mp4", (74.9, 0.7, 659.5, 207.4)),
    (7, "public/loop-storage.mp4", (115.2, 41.0, 619.9, 267.8)),
    (9, "public/loop-search.mp4", (376.6, 10.8, 699.1, 253.4)),
]


def add_clip(pdf: Pdf, page_index: int, mp4_path: str, rect: tuple) -> None:
    name = mp4_path.rsplit("/", 1)[-1]
    with open(mp4_path, "rb") as f:
        data = f.read()

    ef = pdf.make_stream(data)
    ef.Type = Name.EmbeddedFile

    fs = pdf.make_indirect(
        Dictionary(
            Type=Name.Filespec,
            F=String(name),
            UF=String(name),
            EF=Dictionary(F=ef),
        )
    )
    instance = pdf.make_indirect(
        Dictionary(Type=Name.RichMediaInstance, Subtype=Name.Video, Asset=fs)
    )
    cfg = pdf.make_indirect(
        Dictionary(
            Type=Name.RichMediaConfiguration,
            Subtype=Name.Video,
            Instances=Array([instance]),
        )
    )
    content = pdf.make_indirect(
        Dictionary(
            Assets=Dictionary(Names=Array([String(name), fs])),
            Configurations=Array([cfg]),
        )
    )
    settings = Dictionary(
        Activation=Dictionary(
            Condition=Name.PO,
            Configuration=cfg,
            Presentation=Dictionary(Style=Name.Embedded),
        ),
        Deactivation=Dictionary(Condition=Name.PC),
    )
    annot = pdf.make_indirect(
        Dictionary(
            Type=Name.Annot,
            Subtype=Name.RichMedia,
            Rect=Array(rect),
            F=4,
            RichMediaContent=content,
            RichMediaSettings=settings,
        )
    )

    page = pdf.pages[page_index]
    if Name.Annots in page:
        page.Annots.append(annot)
    else:
        page.Annots = pdf.make_indirect(Array([annot]))


def main() -> None:
    src, dst = sys.argv[1], sys.argv[2]
    with Pdf.open(src) as pdf:
        for page_index, mp4_path, rect in CLIPS:
            add_clip(pdf, page_index, mp4_path, rect)
        pdf.save(dst)
    print(f"wrote {dst} with {len(CLIPS)} embedded clips")


if __name__ == "__main__":
    main()
