import pandas as pd
import streamlit as st

import calc
import charts
from i18n import lang, t

L = lang()
risk, both = calc.load()
p = risk["p"]
N = len(risk)
K = int((risk["level"] == "high").sum())
p_high = K / N

st.title(t("a_title"))
st.write(t("a_conv"))

# 1. описательная статистика
st.header(t("a_h1"))
d = calc.describe(p)
values = [
    f"{d['n']}", f"{d['mean']:.3f}", f"{d['median']:.3f}", f"{d['std']:.3f}",
    f"{d['min']:.3f}", f"{d['q1']:.3f}", f"{d['q3']:.3f}", f"{d['max']:.3f}", f"{d['skew']:.2f}",
]
name_col, value_col = t("a_stat_cols")
stat_table = pd.DataFrame({name_col: t("a_stat_names"), value_col: values}).set_index(name_col)
st.table(stat_table)
st.write(t("a_s1", mean=d["mean"], median=d["median"], std=d["std"]))

counts = calc.hist_counts(p)
st.pyplot(charts.hist_p(p, L))
st.write(t("a_hist", first=counts[0], last=counts[-1], mid=counts[2:7].max()))
st.write(t("a_shapiro", p=calc.pv(calc.shapiro_p(p))))

# 2. подбор распределения
st.header(t("a_h2"))
st.write(t("a_s2"))
st.latex(r"f(x)=\frac{x^{a-1}(1-x)^{b-1}}{B(a,b)},\qquad 0<x<1")
a, b, ks_d, ks_p = calc.beta_fit(p)
st.write(t("a_params", a=a, b=b))
st.pyplot(charts.hist_beta(p, a, b, L))
st.write(t("a_ks", d=ks_d, p=calc.pv(ks_p)))
st.write(t("a_uniform", p=calc.pv(calc.uniform_chi2(p))))

# 3. доли и биномиальная модель
st.header(t("a_h3"))
st.write(t("a_s3", k=K, n=N, ph=p_high))
rows = []
for key, label in zip(["low", "medium", "high"], t("a_cat_names")):
    k = int((risk["level"] == key).sum())
    lo, hi = calc.share_ci(k, N)
    rows.append([label, k, f"{k / N:.3f}", t("a_range", lo=lo, hi=hi)])
cat_table = pd.DataFrame(rows, columns=[t("a_cat_col")] + t("a_cat_cols")).set_index(t("a_cat_col"))
st.table(cat_table)
lo_h, hi_h = calc.share_ci(K, N)
st.write(t("a_wilson", lo=lo_h, hi=hi_h))

st.write(t("a_binom", ph=p_high))
st.latex(r"P(X=k)=\binom{n}{k}\,p^{k}(1-p)^{n-k}")
n_pick = st.slider(t("a_slider_n"), 2, 30, 10)
k_pick = st.slider(t("a_slider_k"), 0, n_pick, min(5, n_pick))
p_binom, p_hyper = calc.high_at_least(k_pick, n_pick, N, K)
sd_binom = (n_pick * p_high * (1 - p_high)) ** 0.5
st.write(t("a_binom_res", k=k_pick, pb=p_binom, pf=p_hyper, mean=n_pick * p_high, sd=sd_binom))
st.pyplot(charts.binom_bars(n_pick, k_pick, p_high, L))
st.caption(t("a_binom_cap"))

# 4. среднее и доверительный интервал
st.header(t("a_h4"))
m, se, lo, hi = calc.mean_ci(p)
st.write(t("a_s4a", m=m, se=se))
st.latex(r"\bar{x}\pm t_{0.975,\,n-1}\,\frac{s}{\sqrt{n}}")
st.write(t("a_s4b", lo=lo, hi=hi))
means = calc.bootstrap_means()
b_lo, b_hi = (float(x) for x in pd.Series(means).quantile([0.025, 0.975]))
st.write(t("a_s4c", n=N, lo=b_lo, hi=b_hi))
st.pyplot(charts.boot_hist(means, b_lo, b_hi, m, L))
st.write(t("a_s4d"))

# 5. условные вероятности
st.header(t("a_h5"))
st.write(t("a_s5"))
st.latex(r"P(G\mid H)=\frac{P(H\mid G)\,P(G)}{P(H)}")
tab = calc.group_table(risk)
top = tab.loc[tab["p_g_given_h"].idxmax()]
p_g = top["n"] / N
st.write(t("a_s5ex", g=top["group"], n=int(top["n"]), N=N, pg=p_g, phg=top["p_h_given_g"],
           ph=p_high, pgh=top["p_g_given_h"]))
st.pyplot(charts.group_bars(tab, p_high, L))
st.caption(t("a_s5cap"))
show = tab.copy()
show.columns = t("a_s5cols")
st.dataframe(show.round(3), hide_index=True)
h_stat, h_p, n_groups = calc.groups_kruskal(risk)
st.write(t("a_kw", g=n_groups, h=h_stat, p=calc.pv(h_p)))

# 6. сколько профессий из 150 автоматизируется
st.header(t("a_h6"))
st.write(t("a_s6a"))
st.latex(r"E[N]=\sum_{i=1}^{150}p_i,\qquad \mathrm{Var}[N]=\sum_{i=1}^{150}p_i(1-p_i)")
e_n, sd_n = calc.count_moments(p)
sim = calc.simulate_count()
s_lo, s_hi = (float(x) for x in pd.Series(sim).quantile([0.025, 0.975]))
st.write(t("a_s6b", e=e_n, sd=sd_n, m=sim.mean(), lo=s_lo, hi=s_hi))
st.pyplot(charts.sim_hist(sim, s_lo, s_hi, L))
st.write(t("a_s6c", e=e_n / N, ph=p_high))

# 7. риск, зарплата и рост
st.header(t("a_h7"))
ls = calc.link_stats(both)
st.write(t("a_s7a", n=ls["n"]))
c1, c2 = st.columns(2)
c1.pyplot(charts.scatter_wage(both, ls["slope"], ls["intercept"], L))
c2.pyplot(charts.scatter_growth(both, ls["gslope"], ls["gintercept"], L))
w, g = ls["wage"], ls["growth"]
corr = pd.DataFrame(
    {
        c: v for c, v in zip(
            t("a_corr_cols"),
            [
                [f"{w['pearson']:.2f}", f"{g['pearson']:.2f}"],
                [calc.pv(w["pearson_p"]), calc.pv(g["pearson_p"])],
                [f"{w['spearman']:.2f}", f"{g['spearman']:.2f}"],
                [calc.pv(w["spearman_p"]), calc.pv(g["spearman_p"])],
            ],
        )
    },
    index=t("a_corr_rows"),
)
st.table(corr)
st.write(t("a_reg", a=calc.money(ls["intercept"], L), b=calc.money(-ls["slope"], L),
           d=calc.money(-ls["slope"] * 0.1, L)))
st.write(t("a_cmp", hi=calc.money(ls["med_high"], L), nh=ls["n_high"], lo=calc.money(ls["med_low"], L),
           nl=ls["n_low"], p=calc.pv(ls["mw_p"])))
st.write(t("a_weight", n=ls["n"], w=ls["weighted_p"], m=ls["mean_p"],
           es=ls["emp_share_high"], ps=ls["prof_share_high"]))
st.write(t("a_bias"))
