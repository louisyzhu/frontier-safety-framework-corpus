"""Figures 1 and 2 for the silent-revision-rate paper.

Reproduces fig1_srr_by_pair.{pdf,png} and fig2_direction_by_pair.{pdf,png} from the two CSVs.
Every plotted value is read from the CSV; nothing is smoothed, reordered beyond the documented
sort, or retyped.

Usage:  python make_figures.py [fig1_csv] [fig2_csv] [outdir]
"""
import sys
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle

# ---------------------------------------------------------------- style
# Arial first: the pair labels contain U+2192 (RIGHTWARDS ARROW), which the local
# Helvetica lacks. Arial and DejaVu Sans both cover it; all three are sans-serif.
FONTS = ["Arial", "DejaVu Sans", "Helvetica"]
SZ_AXLABEL, SZ_ANNOT, SZ_TICK = 9, 8, 8   # brief section 3


def apply_style():
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": FONTS,
        "mathtext.fontset": "dejavusans",
        "pdf.fonttype": 42, "ps.fonttype": 42,      # embed TrueType, no Type-3
        "svg.fonttype": "none",
        "axes.labelsize": SZ_AXLABEL, "axes.titlesize": SZ_AXLABEL,
        "xtick.labelsize": SZ_TICK, "ytick.labelsize": SZ_TICK,
        "legend.fontsize": SZ_ANNOT, "font.size": SZ_ANNOT,
        "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
        "xtick.direction": "out", "ytick.direction": "out",
        "xtick.major.size": 3, "ytick.major.size": 0,
        "axes.spines.top": False, "axes.spines.right": False,
        "legend.frameon": False, "legend.handletextpad": 0.5,
        "legend.labelspacing": 0.35, "legend.borderpad": 0.0,
        "figure.dpi": 200, "savefig.bbox": None,
    })


# Okabe-Ito, one palette for the four disclosure regimes, identical in both figures.
REGIME_COLOUR = {"redline": "#000000", "itemised": "#0072B2",
                 "narrative": "#E69F00", "none": "#999999"}
REGIME_ORDER = ["redline", "itemised", "narrative", "none"]

# Figure 2: three related blues for the weakening family, one contrasting hue for
# strengthened, neutral grey for added. Relative luminance in comments (greyscale check).
DIRECTION_COLOUR = {
    "weakened":     "#08306B",   # L 43
    "removed":      "#2171B5",   # L 97
    "relocated":    "#9ECAE1",   # L 191
    "strengthened": "#CC79A7",   # L 151
    "added":        "#737373",   # L 115
}
DIRECTION_ORDER = ["weakened", "removed", "relocated", "strengthened", "added"]
GRID_GREY = "#DDDDDD"
TEXT_GREY = "#555555"


# ---------------------------------------------------------------- data
def load(fig1_csv, fig2_csv):
    f1 = pd.read_csv(fig1_csv)
    f2 = pd.read_csv(fig2_csv)
    assert set(f1["pair"]) == set(f2["pair"]), "pair sets differ between the two files"
    # documented sort: regime order, then srr_strict descending; NaN keeps file order
    f1 = f1.reset_index().rename(columns={"index": "file_order"})
    f1["regime_rank"] = f1["regime"].map({r: i for i, r in enumerate(REGIME_ORDER)})
    f1["neg_strict"] = -f1["srr_strict"]
    f1 = f1.sort_values(["regime_rank", "neg_strict", "file_order"],
                        na_position="last", kind="mergesort").reset_index(drop=True)
    f2 = f2.set_index("pair").loc[f1["pair"]].reset_index()
    return f1, f2


def row_positions(regimes):
    """Top-to-bottom row centres in data coordinates, with a half-row gap between regimes."""
    y, pos = 0.0, []
    for i, r in enumerate(regimes):
        if i and r != regimes[i - 1]:
            y += 0.6
        pos.append(y)
        y += 1.0
    return [max(pos) - p for p in pos]          # invert: first row at the top


# ---------------------------------------------------------------- figure 1
def figure1(f1, outdir):
    ypos = row_positions(list(f1["regime"]))
    fig = plt.figure(figsize=(5.5, 3.15))
    ax = fig.add_axes([0.255, 0.115, 0.415, 0.845])

    ax.axvline(0.5, color=GRID_GREY, lw=0.6, zorder=0)

    drawn = []          # (kind, value) pairs, for the verification note
    for y, r in zip(ypos, f1.itertuples()):
        colour = REGIME_COLOUR[r.regime]
        if np.isnan(r.srr_strict):
            ax.text(0.02, y, f"no revision account (n = {r.n_ncl:.0f})",
                    va="center", ha="left", fontsize=SZ_ANNOT, color=TEXT_GREY)
            drawn.append(("ncl_text", float(r.n_ncl)))
            continue
        lo, hi = min(r.srr_lenient, r.srr_strict), max(r.srr_lenient, r.srr_strict)
        ax.plot([lo, hi], [y, y], color=colour, lw=1.2, solid_capstyle="round", zorder=2)
        ax.plot([r.srr_lenient], [y], marker="o", ms=4.6, mfc="white",
                mec=colour, mew=1.1, zorder=3, ls="none")
        ax.plot([r.srr_strict], [y], marker="o", ms=4.6, color=colour, zorder=3, ls="none")
        # value labels: two decimals (one decimal collapses distinct pairs, see notes)
        ax.text(r.srr_lenient - 0.022, y, f"{r.srr_lenient:.2f}", va="center", ha="right",
                fontsize=SZ_ANNOT, color="black")
        ax.text(r.srr_strict + 0.022, y, f"{r.srr_strict:.2f}", va="center", ha="left",
                fontsize=SZ_ANNOT, color="black")
        drawn += [("srr_lenient", r.srr_lenient), ("srr_strict", r.srr_strict)]

    # right-margin count columns
    tr = ax.get_yaxis_transform()
    ytop = max(ypos) + 0.95
    ax.text(1.11, ytop, "n", transform=tr, ha="right", va="center",
            fontsize=SZ_ANNOT, color=TEXT_GREY)
    ax.text(1.20, ytop, "ANN / ANN-P / SIL", transform=tr, ha="left", va="center",
            fontsize=SZ_ANNOT, color=TEXT_GREY)
    for y, r in zip(ypos, f1.itertuples()):
        if np.isnan(r.srr_strict):
            # No account: n_material_with_account and the ANN/ANN-P/SIL counts are 0 by
            # construction (a different n from the n_ncl already printed in the row), so an
            # en dash marks the columns as not applicable rather than as a zero rate.
            n_txt, split_txt = "\u2013", "\u2013 / \u2013 / \u2013"
        else:
            n_txt = f"{r.n_material_with_account:.0f}"
            split_txt = f"{r.n_ann:.0f} / {r.n_annp:.0f} / {r.n_sil:.0f}"
        ax.text(1.11, y, n_txt, transform=tr, ha="right", va="center",
                fontsize=SZ_ANNOT, color="black")
        ax.text(1.20, y, split_txt, transform=tr, ha="left", va="center",
                fontsize=SZ_ANNOT, color="black")
        drawn += [("n_material_with_account", float(r.n_material_with_account)),
                  ("n_ann", float(r.n_ann)), ("n_annp", float(r.n_annp)),
                  ("n_sil", float(r.n_sil))]

    ax.set_xlim(0, 1)
    ax.set_ylim(-0.75, ytop + 0.55)
    ax.set_yticks(ypos)
    ax.set_yticklabels(f1["pair"], fontsize=SZ_TICK)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xlabel("Silent revision rate", fontsize=SZ_AXLABEL)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0, pad=2)

    handles = [Line2D([], [], color=REGIME_COLOUR[r], lw=1.2, marker="o", ms=4.6,
                      label=r) for r in ["itemised", "narrative", "none"]]
    handles += [Line2D([], [], color="black", ls="none", marker="o", ms=4.6, mfc="white",
                       mec="black", mew=1.1, label="lenient"),
                Line2D([], [], color="black", ls="none", marker="o", ms=4.6, label="strict")]
    ax.legend(handles=handles, loc="lower right", bbox_to_anchor=(1.0, -0.02),
              ncol=1, fontsize=SZ_ANNOT, handlelength=1.4)

    fig.savefig(f"{outdir}/fig1_srr_by_pair.pdf")
    fig.savefig(f"{outdir}/fig1_srr_by_pair.png", dpi=200)
    return fig, ypos, drawn


# ---------------------------------------------------------------- figure 2
def figure2(f2, outdir):
    ypos = row_positions(list(f2["regime"]))
    fig = plt.figure(figsize=(5.5, 3.15))
    ax = fig.add_axes([0.255, 0.115, 0.475, 0.845])

    totals = f2[DIRECTION_ORDER].sum(axis=1)
    xmax = 95
    drawn = []
    inside, outside = [], []                      # label placement bookkeeping
    for y, r in zip(ypos, f2.itertuples()):
        left = 0.0
        for cat in DIRECTION_ORDER:
            v = float(getattr(r, cat))
            drawn.append((cat, v))
            if v == 0:
                continue
            ax.barh(y, v, left=left, height=0.58, color=DIRECTION_COLOUR[cat],
                    edgecolor="white", lw=0.5, zorder=2)
            # label inside when the segment is wide enough for the text at 8 pt
            text_w = len(f"{v:.0f}") * 0.62 * SZ_ANNOT / 72          # inches
            seg_w = v / xmax * (0.475 * 5.5)                          # inches
            if seg_w >= text_w + 0.05:
                lum = {"weakened": 43, "removed": 97, "relocated": 191,
                       "strengthened": 151, "added": 115}[cat]
                ax.text(left + v / 2, y, f"{v:.0f}", va="center", ha="center",
                        fontsize=SZ_ANNOT, color="white" if lum < 130 else "black", zorder=3)
                inside.append((r.pair, cat))
            else:
                outside.append((r.pair, cat))
            left += v
        # regime tag
        ax.add_patch(Rectangle((-4.6, y - 0.16), 2.6, 0.32, clip_on=False,
                               facecolor=REGIME_COLOUR[r.regime], edgecolor="none", zorder=4))

    # Right margin: one fixed, right-aligned column per direction (so narrow segments whose
    # count does not fit inside the bar are still readable), then mix. Numbers carry their
    # segment colour and the column order is the legend order, so no per-column header is needed.
    tr = ax.get_yaxis_transform()
    ytop = max(ypos) + 0.95
    colx = [1.045 + 0.058 * i for i in range(len(DIRECTION_ORDER))]
    mixx = colx[-1] + 0.085
    ax.text(colx[0] - 0.030, ytop, "counts", transform=tr, ha="left", va="center",
            fontsize=SZ_ANNOT, color=TEXT_GREY)
    ax.text(mixx, ytop, "mix", transform=tr, ha="right", va="center",
            fontsize=SZ_ANNOT, color=TEXT_GREY)
    for y, r in zip(ypos, f2.itertuples()):
        for x, cat in zip(colx, DIRECTION_ORDER):
            ax.text(x, y, f"{int(getattr(r, cat))}", transform=tr, ha="right", va="center",
                    fontsize=SZ_ANNOT, color=DIRECTION_COLOUR[cat])
        ax.text(mixx, y, f"{int(r.mix)}", transform=tr, ha="right", va="center",
                fontsize=SZ_ANNOT, color="black")
        drawn.append(("mix", float(r.mix)))

    ax.set_xlim(0, xmax)
    ax.set_ylim(-0.75, ytop + 0.55)
    ax.set_yticks(ypos)
    ax.set_yticklabels(f2["pair"], fontsize=SZ_TICK)
    ax.set_xticks([0, 20, 40, 60, 80])
    ax.set_xlabel("Material changes (count)", fontsize=SZ_AXLABEL)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0, pad=10)

    handles = [Rectangle((0, 0), 1, 1, facecolor=DIRECTION_COLOUR[c], edgecolor="white",
                         lw=0.5, label=c) for c in DIRECTION_ORDER]
    ax.legend(handles=handles, loc="lower right", bbox_to_anchor=(1.005, -0.02),
              ncol=1, fontsize=SZ_ANNOT, handlelength=1.1, handleheight=0.9)

    fig.savefig(f"{outdir}/fig2_direction_by_pair.pdf")
    fig.savefig(f"{outdir}/fig2_direction_by_pair.png", dpi=200)
    return fig, totals, drawn, inside, outside


def main(fig1_csv="fig1_srr_by_pair.csv", fig2_csv="fig2_direction_by_pair.csv", outdir="."):
    apply_style()
    f1, f2 = load(fig1_csv, fig2_csv)
    fig1, ypos1, drawn1 = figure1(f1, outdir)
    fig2_, totals, drawn2, inside, outside = figure2(f2, outdir)
    return dict(f1=f1, f2=f2, fig1=fig1, fig2=fig2_, drawn1=drawn1, drawn2=drawn2,
                totals=totals, inside=inside, outside=outside)


if __name__ == "__main__":
    main(*sys.argv[1:])
