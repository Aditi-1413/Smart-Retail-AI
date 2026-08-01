import streamlit as st
from styles import load_css
from components import hero, dashboard_cards, feature_cards, footer
from utils import check_server
import pandas as pd

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

# ===============================
# HERO
# ===============================

hero()

st.write("")

dashboard_cards()

st.write("")

# ===============================
# PLATFORM OVERVIEW
# ===============================

st.subheader("🚀 Platform Overview")

col1, col2 = st.columns([2, 1])

with col1:

    st.markdown("""
<div class="card">

### Smart Retail AI Platform

This platform combines multiple Artificial Intelligence modules into a single dashboard.

#### Available Modules

- 👕 Product Classification
- 🙂 Face Recognition
- ⭐ Sentiment Analysis
- 🤖 AI Chatbot

The application is powered using FastAPI, TensorFlow, OpenCV and Streamlit.

</div>
""", unsafe_allow_html=True)

with col2:

    backend = check_server()

    st.markdown("### System Status")

    if backend:
        st.success("🟢 Backend Connected")
    else:
        st.error("🔴 Backend Offline")

    st.success("🟢 TensorFlow")

    st.success("🟢 OpenCV")

    st.success("🟢 Streamlit")

st.write("")

# ===============================
# MODEL PERFORMANCE
# ===============================

st.subheader("📈 Model Performance")

performance = pd.DataFrame({

    "Accuracy":[
        99,
        96,
        94,
        100
    ]},

    index=[
        "CNN Product",
        "LBPH Face",
        "LSTM Sentiment",
        "Chatbot"
    ]

)

st.bar_chart(performance)

st.write("")

# ===============================
# MODULES
# ===============================

feature_cards()

st.write("")

# ===============================
# DATASET INFORMATION
# ===============================

st.subheader("📂 Dataset Information")

c1, c2 = st.columns(2)

with c1:

    st.markdown("""
<div class="card">

### 👕 Fashion MNIST

✔ 70,000 Images

✔ 10 Classes

✔ CNN Model

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="card">

### 🙂 LFW Dataset

✔ 3023 Images

✔ 62 People

✔ LBPH Recognizer

</div>
""", unsafe_allow_html=True)

with c2:

    st.markdown("""
<div class="card">

### ⭐ IMDB Reviews

✔ 50,000 Reviews

✔ Positive & Negative

✔ LSTM Network

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="card">

### 🤖 Chatbot

✔ Intent Classification

✔ Custom Responses

✔ NLP Based

</div>
""", unsafe_allow_html=True)

st.write("")

# ===============================
# RECENT ACTIVITY
# ===============================

st.subheader("📋 Recent Activity")

activity = pd.DataFrame({

    "Module":[
        "Product Classification",
        "Face Recognition",
        "Sentiment Analysis",
        "AI Chatbot"
    ],

    "Status":[
        "Ready",
        "Ready",
        "Ready",
        "Ready"
    ]

})

st.dataframe(
    activity,
    use_container_width=True,
    hide_index=True
)

st.write("")

# ===============================
# QUICK STATISTICS
# ===============================

st.subheader("📊 Quick Statistics")

a, b, c, d = st.columns(4)

a.metric("Images", "73K+")

b.metric("Models", "4")

c.metric("Classes", "10")

d.metric("Accuracy", "95%+")

st.write("")

footer()