import streamlit as st
from styles import load_css
from components import hero, dashboard_cards, feature_cards, value_props, footer
from utils import check_server

st.set_page_config(
    page_title="Smart Retail AI",
    page_icon="🛍️",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

st.sidebar.title("🛍 Smart Retail AI")

if check_server():
    st.sidebar.success("🟢 Backend Connected")
else:
    st.sidebar.error("🔴 Backend Offline")

hero()

dashboard_cards()

st.write("")

st.subheader("The Platform")

feature_cards()

st.write("")

st.subheader("Why Teams Choose This Platform")

value_props()

st.info(
"""
👈 Select a module from the sidebar to get started.

**Product Classification** · **Face Recognition** · **Sentiment Analysis** · **AI Chatbot**
"""
)

footer()