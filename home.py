import streamlit as st
import visualization, Hypothesis

PAGES = {
    'Data Visualization': visualization,
    'Hyphothesis Testing': Hypothesis
}

selected = st.sidebar.selectbox('SELECT A PAGE', list(PAGES.keys()))
warna = st.sidebar.color_picker("Pilih Warna","#0000FF")
page = PAGES[selected]
page.app()