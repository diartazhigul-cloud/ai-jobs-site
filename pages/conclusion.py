import streamlit as st

import calc
from i18n import t

risk, both = calc.load()
p = risk["p"]
N = len(risk)
K = int((risk["level"] == "high").sum())

m, se, lo, hi = calc.mean_ci(p)
a, b, ks_d, ks_p = calc.beta_fit(p)
e_n, sd_n = calc.count_moments(p)
tab = calc.group_table(risk)
ls = calc.link_stats(both)

st.title(t("c_title"))

st.subheader(t("c_h1"))
st.write(t("c1", m=m, lo=lo, hi=hi, k=K, n=N, share=K / N))
st.write(t("c2", a=a, b=b, p=calc.pv(ks_p)))
best = tab.iloc[0]
zero = "; ".join(tab.loc[tab["p_h_given_g"] == 0, "group"])
st.write(t("c3", g=best["group"], share=best["p_h_given_g"], zero=zero))
st.write(t("c4", e=e_n, n=N, sd=sd_n))
st.write(t("c5", n=ls["n"], rw=ls["wage"]["pearson"], rg=ls["growth"]["pearson"]))

st.subheader(t("c_h2"))
st.markdown(t("c_lim"))

st.subheader(t("c_h3"))
st.markdown(t("c_src"))
st.caption(t("author"))
