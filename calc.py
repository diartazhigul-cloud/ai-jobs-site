"""Все расчёты проекта. Streamlit здесь не используется, чтобы функции можно было запускать и проверять отдельно."""
from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

FILE = Path(__file__).parent / "data" / "AI_labor_market_150_for_THEORY.xlsx"
HIGH, LOW = 0.7, 0.3  # границы категорий, такие же как в файле


def level(p):
    if p > HIGH:
        return "high"
    if p < LOW:
        return "low"
    return "medium"


@lru_cache(maxsize=1)
def load():
    """Читает два листа из xlsx. Названия профессий и групп оставлены как в источнике."""
    risk = pd.read_excel(FILE, sheet_name="Risk_150")
    risk.columns = ["n", "soc", "occupation", "p", "risk", "group", "has_bls"]
    risk["level"] = risk["p"].map(level)

    both = pd.read_excel(FILE, sheet_name="Both_Datasets")
    both.columns = ["occupation", "p", "risk", "growth", "wage", "emp25", "emp35"]
    both["level"] = both["p"].map(level)
    return risk, both


def money(x, lang="en"):
    """83680 -> '83,680' по-английски и '83 680' по-русски (там запятая означала бы десятичную дробь)."""
    s = f"{x:,.0f}"
    return s.replace(",", "\u00a0") if lang == "ru" else s


def pv(x):
    """p-value в читаемом виде."""
    return "< 0.001" if x < 0.001 else f"= {x:.3f}"


# 1. описательная статистика

def describe(p):
    return {
        "n": len(p),
        "mean": p.mean(),
        "median": p.median(),
        "std": p.std(ddof=1),
        "min": p.min(),
        "q1": p.quantile(0.25),
        "q3": p.quantile(0.75),
        "max": p.max(),
        "skew": stats.skew(p),
    }


def shapiro_p(p):
    return stats.shapiro(p).pvalue


def hist_counts(p):
    return np.histogram(p, bins=np.linspace(0, 1, 11))[0]


# 2. подбор распределения

def beta_fit(p):
    a, b, _, _ = stats.beta.fit(p, floc=0, fscale=1)
    ks = stats.kstest(p, "beta", args=(a, b))
    return a, b, ks.statistic, ks.pvalue


def uniform_chi2(p):
    observed = np.histogram(p, bins=5, range=(0, 1))[0]
    return stats.chisquare(observed).pvalue


# 3. доли и биномиальная модель

def share_ci(k, n):
    ci = stats.binomtest(k, n).proportion_ci(confidence_level=0.95, method="wilson")
    return ci.low, ci.high


def high_at_least(k, n, N, K):
    """P(X >= k) для биномиальной и гипергеометрической моделей. N профессий всего, K высокорисковых."""
    binom = stats.binom.sf(k - 1, n, K / N)
    hyper = stats.hypergeom.sf(k - 1, N, K, n)
    return binom, hyper


# 4. среднее и доверительный интервал

def mean_ci(p):
    n = len(p)
    m = p.mean()
    se = p.std(ddof=1) / np.sqrt(n)
    t = stats.t.ppf(0.975, n - 1)
    return m, se, m - t * se, m + t * se


@lru_cache(maxsize=1)
def bootstrap_means(B=10000, seed=42):
    risk, _ = load()
    p = risk["p"].to_numpy()
    rng = np.random.default_rng(seed)
    means = rng.choice(p, size=(B, len(p))).mean(axis=1)
    return means


# 5. условные вероятности

def group_table(risk, min_n=5):
    n_high_total = (risk["level"] == "high").sum()
    g = risk.groupby("group").agg(
        n=("p", "size"),
        n_high=("level", lambda s: (s == "high").sum()),
        mean_p=("p", "mean"),
    )
    g["p_h_given_g"] = g["n_high"] / g["n"]
    g["p_g_given_h"] = g["n_high"] / n_high_total
    g = g[g["n"] >= min_n].sort_values("p_h_given_g", ascending=False)
    return g.reset_index()


def groups_kruskal(risk, min_n=5):
    big = risk.groupby("group").filter(lambda d: len(d) >= min_n)
    samples = [d["p"].to_numpy() for _, d in big.groupby("group")]
    res = stats.kruskal(*samples)
    return res.statistic, res.pvalue, len(samples)


# 6. сколько профессий автоматизируется

def count_moments(p):
    p = np.asarray(p)
    return p.sum(), np.sqrt((p * (1 - p)).sum())


@lru_cache(maxsize=1)
def simulate_count(B=20000, seed=1):
    risk, _ = load()
    p = risk["p"].to_numpy()
    rng = np.random.default_rng(seed)
    return (rng.random((B, len(p))) < p).sum(axis=1)


# 7. риск, зарплата и рост

def link_stats(both):
    out = {"n": len(both)}
    for col in ["wage", "growth"]:
        r = stats.pearsonr(both["p"], both[col])
        s = stats.spearmanr(both["p"], both[col])
        out[col] = {"pearson": r.statistic, "pearson_p": r.pvalue,
                    "spearman": s.statistic, "spearman_p": s.pvalue}
    line = stats.linregress(both["p"], both["wage"])
    out["slope"], out["intercept"] = line.slope, line.intercept
    gline = stats.linregress(both["p"], both["growth"])
    out["gslope"], out["gintercept"] = gline.slope, gline.intercept

    hi = both.loc[both["level"] == "high", "wage"]
    lo = both.loc[both["level"] == "low", "wage"]
    out["n_high"], out["n_low"] = len(hi), len(lo)
    out["med_high"], out["med_low"] = hi.median(), lo.median()
    out["mw_p"] = stats.mannwhitneyu(hi, lo, alternative="two-sided").pvalue

    high = both["level"] == "high"
    out["emp_share_high"] = both.loc[high, "emp25"].sum() / both["emp25"].sum()
    out["prof_share_high"] = high.mean()

    out["mean_p"] = both["p"].mean()
    out["weighted_p"] = (both["p"] * both["emp25"]).sum() / both["emp25"].sum()
    return out
