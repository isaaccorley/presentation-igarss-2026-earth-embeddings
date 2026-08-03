"""Looping illustration clips for the Earth Embeddings talk.

White background, palette matched to the book chapter's embedding-types
figure (encoder fills, embedding oranges, land-cover mosaic colors).

Manim keeps frame_width = 14.22 units under custom --resolution; only
frame_height changes (14.22 * H / W). All layouts below assume that.

Render (from repo root):
    manim render --fps 30 --resolution 1920,720  -o loop-pipeline.mp4 clips/clips.py PipelineLoop
    manim render --fps 30 --resolution 1440,1080 -o loop-search.mp4   clips/clips.py SearchLoop
    manim render --fps 30 --resolution 1920,860  -o loop-storage.mp4  clips/clips.py StorageBars
"""

import math

from manim import *

# palette (chapter figure + deck)
BG = "#FFFFFF"
INK = "#24201d"
MUTED = "#7a736c"
ACCENT = "#D8401F"     # TG red
PERI = "#4A6AA8"       # TG periwinkle
ENC_BLUE = "#AEC5E8"
EMB = ["#D95F0E", "#EC8C3C", "#F7B26A", "#FCD39E", "#FEEDCD"]  # embedding oranges
LC = {
    "water": "#84B1D4", "forestA": "#588A4F", "forestB": "#6C9C5C",
    "field": "#C4D182", "fieldB": "#B2C474", "urban": "#C6BCAE", "urbanB": "#B6AEA4",
}
MONO = "Menlo"

MOSAIC_CELLS = [
    ["water", "water", "forestA", "forestB"],
    ["water", "fieldB", "forestB", "forestA"],
    ["field", "fieldB", "field", "forestB"],
    ["fieldB", "urban", "urbanB", "field"],
]


def mosaic(side=1.6, cells=MOSAIC_CELLS):
    """4x4 land-cover chip like the chapter figure's input mosaics."""
    n = len(cells)
    cell = side / n
    g = VGroup()
    for r, row in enumerate(cells):
        for c, name in enumerate(row):
            sq = Square(cell, fill_color=LC[name], fill_opacity=1.0,
                        stroke_color=INK, stroke_opacity=0.18, stroke_width=0.8)
            sq.move_to([(c - (n - 1) / 2) * cell, ((n - 1) / 2 - r) * cell, 0])
            g.add(sq)
    g.add(Square(side, stroke_color=INK, stroke_opacity=0.5,
                 stroke_width=1.4, fill_opacity=0))
    return g


def embvec(order=(1, 3, 0, 4, 2), cell_w=0.42, cell_h=0.42):
    """1D embedding vector, 5 cells of the orange ramp (unordered)."""
    g = VGroup()
    for i, k in enumerate(order):
        r = Rectangle(width=cell_w, height=cell_h, fill_color=EMB[k],
                      fill_opacity=1.0, stroke_color=INK, stroke_opacity=0.4,
                      stroke_width=1.0)
        r.move_to([(i - 2) * cell_w, 0, 0])
        g.add(r)
    return g


def encoder(fill=ENC_BLUE, label="encoder", w=2.0, h=1.6):
    """Trapezoid encoder like the chapter figure."""
    shape = Polygon(
        [-w / 2, -h / 2, 0], [w / 2, -h * 0.33, 0],
        [w / 2, h * 0.33, 0], [-w / 2, h / 2, 0],
        fill_color=fill, fill_opacity=1.0,
        stroke_color=INK, stroke_opacity=0.45, stroke_width=1.6,
    )
    txt = Text(label, font=MONO, font_size=20, color=INK)
    txt.move_to(shape.get_center())
    return VGroup(shape, txt)


def arrow(a, b, **kw):
    return Arrow(a, b, buff=0.12, stroke_width=3.2, color=INK,
                 max_tip_length_to_length_ratio=0.14,
                 max_stroke_width_to_length_ratio=6, **kw).set_opacity(0.65)


class PipelineLoop(Scene):
    """Imagery -> encoder (run once) -> vectors -> reused by many.

    1920x720: visible x in [-7.11, 7.11], y in [-2.67, 2.67].
    """

    def construct(self):
        self.camera.background_color = BG

        stack = VGroup()
        for i in range(3):
            m = mosaic(1.25)
            m.shift(RIGHT * 0.14 * i + UP * 0.14 * i)
            m.set_z_index(3 - i)
            stack.add(m)
        stack.move_to(LEFT * 5.45 + UP * 0.25)
        in_label = Text("petabytes of imagery", font=MONO, font_size=16,
                        color=MUTED).next_to(stack, DOWN, buff=0.35)

        enc = encoder(ENC_BLUE, "encoder", w=2.0, h=1.6)
        enc.move_to(LEFT * 2.9 + UP * 0.25)
        enc_label = Text("run once", font=MONO, font_size=17,
                         color=MUTED).next_to(enc, DOWN, buff=0.35)

        vec = embvec().move_to(RIGHT * 0.35 + UP * 0.25)
        vec_label = Text("compact vectors", font=MONO, font_size=17,
                         color=MUTED).next_to(vec, DOWN, buff=0.42)

        a1 = arrow(stack.get_right(), enc.get_left())
        a2 = arrow(enc.get_right(), vec.get_left())

        uses = ["land cover mapping", "similarity search", "yield / risk models"]
        use_texts = VGroup(*[Text(u, font=MONO, font_size=18, color=INK)
                             for u in uses])
        use_texts.arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        use_texts.move_to(RIGHT * 4.95 + UP * 0.25)
        fan = VGroup(*[arrow(vec.get_right() + RIGHT * 0.05, t.get_left())
                       for t in use_texts])

        self.play(FadeIn(stack, shift=RIGHT * 0.3), FadeIn(in_label), run_time=0.9)
        self.play(FadeIn(enc), FadeIn(enc_label), Create(a1), run_time=0.8)
        self.play(Create(a2), FadeIn(vec, shift=RIGHT * 0.2), FadeIn(vec_label),
                  run_time=0.8)
        self.wait(0.3)

        for f, t in zip(fan, use_texts):
            ghost = vec.copy().scale(0.5)
            self.play(
                Create(f),
                ghost.animate.move_to(t.get_left() + LEFT * 0.7).set_opacity(0.0),
                FadeIn(t, shift=RIGHT * 0.15),
                run_time=0.75,
            )
        self.wait(2.6)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.6)
        self.wait(0.2)


class SearchLoop(Scene):
    """Query chip -> vector -> scan candidate tiles -> best cosine match.

    1440x1080: visible x in [-7.11, 7.11], y in [-5.33, 5.33].
    """

    def construct(self):
        self.camera.background_color = BG

        q_chip = mosaic(1.5).move_to(LEFT * 5.0 + UP * 3.55)
        q_label = Text("query", font=MONO, font_size=18, color=MUTED)
        q_label.next_to(q_chip, DOWN, buff=0.3)
        q_vec = embvec(cell_w=0.38, cell_h=0.38)
        q_vec.move_to(LEFT * 2.0 + UP * 3.55)
        qa = arrow(q_chip.get_right(), q_vec.get_left())

        orders = [
            (0, 2, 4, 1, 3), (3, 1, 0, 2, 4), (2, 4, 3, 0, 1), (4, 0, 1, 3, 2),
            (1, 2, 3, 4, 0), (0, 4, 2, 3, 1), (3, 0, 4, 1, 2), (2, 1, 0, 4, 3),
            (4, 3, 1, 2, 0), (1, 0, 3, 2, 4), (0, 3, 1, 4, 2), (1, 3, 0, 4, 2),
            (2, 0, 4, 3, 1), (4, 1, 2, 0, 3), (3, 4, 0, 2, 1), (0, 1, 3, 2, 4),
            (2, 3, 4, 1, 0), (4, 2, 0, 3, 1), (1, 4, 2, 0, 3), (3, 2, 1, 4, 0),
        ]
        rows, cols = 4, 5
        tiles = VGroup()
        for i in range(rows * cols):
            v = embvec(orders[i], cell_w=0.3, cell_h=0.3)
            box = SurroundingRectangle(v, buff=0.15, corner_radius=0.02,
                                       stroke_color=INK, stroke_opacity=0.22,
                                       stroke_width=1.0)
            tiles.add(VGroup(box, v))
        tiles.arrange_in_grid(rows=rows, cols=cols, buff=(0.55, 0.72))
        tiles.move_to(DOWN * 1.05)
        grid_label = Text("patch embedding product", font=MONO, font_size=18,
                          color=MUTED).next_to(tiles, DOWN, buff=0.5)

        self.play(FadeIn(q_chip), FadeIn(q_label), run_time=0.7)
        self.play(Create(qa), FadeIn(q_vec, shift=RIGHT * 0.15), run_time=0.7)
        self.play(FadeIn(tiles, lag_ratio=0.03), FadeIn(grid_label), run_time=1.0)

        path = [0, 3, 7, 10, 14, 17, 12]
        sims = ["0.31", "0.44", "0.18", "0.52", "0.27", "0.63", "0.97"]
        ring = SurroundingRectangle(tiles[path[0]], buff=0.05, corner_radius=0.03,
                                    stroke_color=PERI, stroke_width=3.4)
        anchor = RIGHT * 6.85 + UP * 3.55
        readout = Text("cos = 0.31", font=MONO, font_size=24, color=PERI)
        readout.move_to(anchor, aligned_edge=RIGHT)
        self.play(Create(ring), FadeIn(readout), run_time=0.5)

        for idx, s in list(zip(path, sims))[1:]:
            new_ring = SurroundingRectangle(tiles[idx], buff=0.05,
                                            corner_radius=0.03,
                                            stroke_color=PERI, stroke_width=3.4)
            new_read = Text(f"cos = {s}", font=MONO, font_size=24, color=PERI)
            new_read.move_to(anchor, aligned_edge=RIGHT)
            self.play(Transform(ring, new_ring),
                      Transform(readout, new_read), run_time=0.42)

        best = tiles[path[-1]]
        final_read = Text("best match · cos = 0.97", font=MONO, font_size=24,
                          color=ACCENT, weight=BOLD)
        final_read.move_to(anchor, aligned_edge=RIGHT)
        self.play(ring.animate.set_stroke(color=ACCENT, width=4.2),
                  Transform(readout, final_read),
                  best.animate.scale(1.15), run_time=0.6)
        self.wait(2.6)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.6)
        self.wait(0.2)


class StorageBars(Scene):
    """Log-scale storage for one year of Africa coverage, patch vs pixel.

    1920x860: visible x in [-7.11, 7.11], y in [-3.19, 3.19].
    """

    DATA = [
        # name, GB, label, cost, is_pixel
        ("Copernicus-Embed", 0.1475, "147.5 MB", "$0.04/yr", False),
        ("Clay v1.5 Sentinel-2", 18.8, "18.8 GB", "$4.83/yr", False),
        ("Clay v1.5 NAIP", 1_900, "1.9 TB", "$488/yr", False),
        ("Google Satellite Embedding", 19_200, "19.2 TB", "$4,935/yr", True),
        ("Tessera", 38_400, "38.4 TB", "$9,871/yr", True),
        ("Presto", 76_800, "76.8 TB", "$19,497/yr", True),
    ]

    def construct(self):
        self.camera.background_color = BG

        x0, x1 = -2.5, 2.6          # bar start / max end (scene units)
        lo, hi = -1.2, 5.0          # log10 GB range
        y_top, dy = 2.25, 0.92
        val_x = 2.85                # fixed left edge of the value column

        def bar_len(gb):
            return (math.log10(gb) - lo) / (hi - lo) * (x1 - x0)

        grid = VGroup()
        for gb, lab in [(1, "1 GB"), (1_000, "1 TB")]:
            x = x0 + bar_len(gb)
            grid.add(DashedLine([x, y_top + 0.5, 0], [x, y_top - 5 * dy - 0.4, 0],
                                stroke_color=INK, stroke_opacity=0.15,
                                stroke_width=1.2, dash_length=0.08))
            grid.add(Text(lab, font=MONO, font_size=14, color=MUTED)
                     .move_to([x, y_top + 0.72, 0]))
        scale_note = Text("log scale · 1 year of Africa", font=MONO,
                          font_size=14, color=MUTED)
        scale_note.move_to([x1 + 1.9, y_top + 0.72, 0])
        self.play(FadeIn(grid), FadeIn(scale_note), run_time=0.6)

        for i, (name, gb, size_lab, cost, is_pixel) in enumerate(self.DATA):
            y = y_top - i * dy
            color = EMB[1] if is_pixel else ENC_BLUE
            name_t = Text(name, font=MONO, font_size=17, color=INK)
            name_t.move_to([x0 - 0.3, y, 0], aligned_edge=RIGHT)
            L = bar_len(gb)
            bar = Rectangle(width=L, height=0.4, fill_color=color,
                            fill_opacity=1.0, stroke_color=INK,
                            stroke_opacity=0.35, stroke_width=1.0)
            bar.move_to([x0, y, 0], aligned_edge=LEFT)
            val = Text(f"{size_lab}  ·  {cost}", font=MONO, font_size=15,
                       color=MUTED)
            val.move_to([val_x, y, 0], aligned_edge=LEFT)
            self.play(FadeIn(name_t, run_time=0.25),
                      GrowFromEdge(bar, LEFT, run_time=0.55),
                      FadeIn(val, run_time=0.3))

        legend = VGroup(
            Square(0.26, fill_color=ENC_BLUE, fill_opacity=1, stroke_color=INK,
                   stroke_opacity=0.35, stroke_width=1),
            Text("patch", font=MONO, font_size=16, color=INK),
            Square(0.26, fill_color=EMB[1], fill_opacity=1, stroke_color=INK,
                   stroke_opacity=0.35, stroke_width=1),
            Text("pixel", font=MONO, font_size=16, color=INK),
        ).arrange(RIGHT, buff=0.25)
        legend.move_to([-5.6, y_top + 0.72, 0])
        self.play(FadeIn(legend), run_time=0.4)
        self.wait(3.0)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.6)
        self.wait(0.2)
