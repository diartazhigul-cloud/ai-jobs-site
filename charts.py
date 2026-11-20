"""Графики. Один цвет и его светлый оттенок, без лишнего оформления."""
import matplotlib as mpl
import numpy as np
from matplotlib.figure import Figure
from matplotlib.ticker import FuncFormatter
from scipy import stats

INK = "#2f4a6b"
LIGHT = "#b7c3d4"
GRID = "#dcd8cd"
BG = "#fbfaf7"
TEXT = "#222222"

mpl.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "figure.facecolor": BG,
    "axes.facecolor": BG,
    "axes.edgecolor": "#888888",
    "axes.labelcolor": TEXT,
    "text.color": TEXT,
    "xtick.color": TEXT,
    "ytick.color": TEXT,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.color": GRID,
    "grid.linewidth": 0.6,
    "axes.axisbelow": True,
    "figure.dpi": 130,
})

BINS = np.linspace(0, 1, 11)

# подписи на графиках, по языкам
L = {
    "en": {
        "prob": "Probability of automation", "count": "Number of occupations", "data": "data",
        "density": "Density", "x_binom": "Number of high-risk occupations X",
        "x_boot": "Mean of a bootstrap sample", "y_boot": "Number of samples",
        "x_group": "Share of high-risk occupations in the group", "whole": "whole sample {v:.2f}",
        "x_sim": "Number of automated occupations out of 150", "y_sim": "Number of runs",
        "wage": "Median wage, USD", "growth": "Employment growth 2025-2035, %",
    },
    "ru": {
        "prob": "Вероятность автоматизации", "count": "Число профессий", "data": "данные",
        "density": "Плотность", "x_binom": "Число высокорисковых профессий X",
        "x_boot": "Среднее по бутстреп-выборке", "y_boot": "Число выборок",
        "x_group": "Доля высокорисковых профессий в группе", "whole": "по всей выборке {v:.2f}",
        "x_sim": "Число автоматизируемых профессий из 150", "y_sim": "Число прогонов",
        "wage": "Медианная зарплата, USD", "growth": "Рост занятости 2025-2035, %",
    },
}


def _new(w=7, h=3.3):
    # Figure напрямую, не через pyplot: так фигуры не копятся в памяти при каждом обновлении страницы
    fig = Figure(figsize=(w, h), layout="constrained")
    return fig, fig.subplots()


def hist_p(p, lang="en"):
    t = L[lang]
    fig, ax = _new()
    _, _, bars = ax.hist(p, bins=BINS, color=INK, edgecolor=BG)
    ax.bar_label(bars, fontsize=8)
    ax.set_xticks(BINS)
    ax.set_xlabel(t["prob"])
    ax.set_ylabel(t["count"])
    ax.grid(axis="x", visible=False)
    return fig


def hist_beta(p, a, b, lang="en"):
    t = L[lang]
    fig, ax = _new()
    ax.hist(p, bins=BINS, density=True, color=LIGHT, edgecolor=BG, label=t["data"])
    x = np.linspace(0.01, 0.99, 400)
    ax.plot(x, stats.beta.pdf(x, a, b), color=INK, lw=2, label=f"Beta({a:.2f}; {b:.2f})")
    ax.set_ylim(0, 3.6)
    ax.set_xticks(BINS)
    ax.set_xlabel(t["prob"])
    ax.set_ylabel(t["density"])
    ax.grid(axis="x", visible=False)
    ax.legend(frameon=False, loc="upper center")
    return fig


def binom_bars(n, k, prob, lang="en"):
    t = L[lang]
    fig, ax = _new(7, 2.8)
    x = np.arange(n + 1)
    colors = [INK if v >= k else LIGHT for v in x]
    ax.bar(x, stats.binom.pmf(x, n, prob), color=colors)
    ax.set_xlabel(t["x_binom"])
    ax.set_ylabel("P(X = x)")
    ax.grid(axis="x", visible=False)
    if n <= 15:
        ax.set_xticks(x)
    return fig


def boot_hist(means, lo, hi, m, lang="en"):
    t = L[lang]
    fig, ax = _new(7, 2.8)
    ax.hist(means, bins=40, color=LIGHT, edgecolor=BG)
    ax.axvline(m, color=INK, lw=1.5)
    ax.axvline(lo, color=INK, lw=1.2, ls="--")
    ax.axvline(hi, color=INK, lw=1.2, ls="--")
    ax.set_xlabel(t["x_boot"])
    ax.set_ylabel(t["y_boot"])
    ax.grid(axis="x", visible=False)
    return fig


def group_bars(tab, overall, lang="en"):
    t = L[lang]
    fig, ax = _new(7, 4.8)
    rows = tab.iloc[::-1]
    ax.barh(rows["group"], rows["p_h_given_g"], color=INK)
    ax.axvline(overall, color=TEXT, lw=1, ls="--")
    ax.text(overall + 0.01, 0.2, t["whole"].format(v=overall), fontsize=8, va="bottom")
    ax.set_xlim(0, 1)
    ax.set_xlabel(t["x_group"])
    ax.tick_params(axis="y", labelsize=8.5)
    ax.grid(axis="y", visible=False)
    return fig


def sim_hist(sim, lo, hi, lang="en"):
    t = L[lang]
    fig, ax = _new(7, 2.9)
    counts = np.bincount(sim)
    x = np.arange(len(counts))
    keep = counts > 0
    ax.bar(x[keep], counts[keep], color=LIGHT, width=1.0)
    ax.axvline(lo, color=INK, lw=1.2, ls="--")
    ax.axvline(hi, color=INK, lw=1.2, ls="--")
    ax.set_xlim(x[keep].min() - 1, x[keep].max() + 1)
    ax.set_xlabel(t["x_sim"])
    ax.set_ylabel(t["y_sim"])
    ax.grid(axis="x", visible=False)
    return fig


def _thousands(v, _):
    return f"{v / 1000:.0f}k"


def scatter_wage(both, slope, intercept, lang="en"):
    t = L[lang]
    fig, ax = _new(3.6, 3.3)
    ax.scatter(both["p"], both["wage"], color=INK, s=22, alpha=0.8)
    xs = np.array([0, 1])
    ax.plot(xs, intercept + slope * xs, color=TEXT, lw=1)
    ax.yaxis.set_major_formatter(FuncFormatter(_thousands))
    ax.set_xlabel(t["prob"])
    ax.set_ylabel(t["wage"])
    return fig


def scatter_growth(both, slope, intercept, lang="en"):
    t = L[lang]
    fig, ax = _new(3.6, 3.3)
    ax.scatter(both["p"], both["growth"], color=INK, s=22, alpha=0.8)
    xs = np.array([0, 1])
    ax.plot(xs, intercept + slope * xs, color=TEXT, lw=1)
    ax.set_xlabel(t["prob"])
    ax.set_ylabel(t["growth"])
    return fig
