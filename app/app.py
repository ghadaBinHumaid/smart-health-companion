import streamlit as st
from utils.ui_helpers import set_bg

st.set_page_config(
    page_title="Smart Health Companion",
    page_icon="💊",
    layout="centered"
)

set_bg()

st.title("💊 Smart Health Companion")

st.markdown("""
Your AI assistant for health insights and symptom analysis.
""")
st.markdown("""
Welcome! Please choose an option below:
""")

col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/page_01.py", label="🩺 Remedy Recommendations", icon="💡")
with col2:
    st.page_link("pages/page_02.py", label="🧠 Diagnosis Assistant", icon="🧬")

st.markdown("""
---
**Disclaimer:** This is **not** medical advice.
Always consult a qualified healthcare professional, especially for severe, persistent, or worsening symptoms.
""")
