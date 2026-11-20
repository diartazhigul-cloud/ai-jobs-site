import streamlit as st

from i18n import LANGS, t

st.set_page_config(page_title="Automation and jobs", layout="centered")

# переключатель языка живёт в боковом меню, выбор хранится в st.session_state["lang"]
st.sidebar.radio("Language / Язык", list(LANGS), format_func=LANGS.get, key="lang", horizontal=True)

pages = [
    st.Page("pages/intro.py", title=t("nav_intro"), default=True),
    st.Page("pages/analysis.py", title=t("nav_main")),
    st.Page("pages/conclusion.py", title=t("nav_concl")),
]
st.navigation(pages).run()
