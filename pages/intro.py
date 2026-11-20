import streamlit as st

import calc
from i18n import lang, t

risk, both = calc.load()
p = risk["p"]
n_high = int((risk["level"] == "high").sum())

st.title(t("i_title"))
st.caption(t("i_caption"))

st.write(t("i_p1"))
st.write(t("i_p2"))

st.subheader(t("i_q_h"))
st.markdown(t("i_q"))

st.subheader(t("i_read_h"))
st.write(t("i_read"))

c1, c2, c3 = st.columns(3)
c1.metric(t("i_m1"), len(risk))
c2.metric(t("i_m2"), f"{p.mean():.2f}")
c3.metric(t("i_m3"), f"{n_high / len(risk):.0%}")

st.subheader(t("i_look_h"))
names = risk["occupation"].sort_values().tolist()
start = names.index("Accountants and Auditors") if "Accountants and Auditors" in names else 0
name = st.selectbox(t("i_select"), names, index=start)

row = risk[risk["occupation"] == name].iloc[0]
below = (p < row["p"]).mean()
st.write(t("i_look", p=row["p"], group=row["group"], below=below))
extra = both[both["occupation"] == name]
if len(extra):
    e = extra.iloc[0]
    st.write(t("i_look_extra", growth=e["growth"], wage=calc.money(e["wage"], lang())))

with st.expander(t("i_expander")):
    table = risk[["occupation", "group", "p"]].copy()
    table.columns = t("i_cols")
    st.dataframe(table, hide_index=True)

st.caption(t("author"))
