"""Переключение языка. Выбранный язык лежит в st.session_state['lang'] ('en' или 'ru')."""
import streamlit as st

from texts import T

LANGS = {"en": "English", "ru": "Русский"}


def lang():
    return st.session_state.get("lang", "en")


def t(key, **kw):
    """Текст по ключу на выбранном языке. Если переданы значения, подставляет их через format."""
    value = T[key][0 if lang() == "en" else 1]
    if kw and isinstance(value, str):
        return value.format(**kw)
    return value
