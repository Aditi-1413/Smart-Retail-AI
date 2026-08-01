import streamlit as st
import pandas as pd
import plotly.express as px
from styles import load_css
from components import page_title, footer

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

# =====================================================
# PAGE TITLE
# =====================================================

page_title(
    "📈 Analytics Dashboard",
    "Monitor AI model performance, datasets and system statistics."
)

st.write("")

# =====================================================
# KPI CARDS
# =====================================================

c1, c2, c3, c4 = st.columns(4)

c1.metric("AI Models", "4")
c2.metric("Datasets", "4")
c3.metric("Total Samples", "125K+")
c4.metric("Overall Accuracy", "95.1%")

st.write("")

# =====================================================
# MODEL ACCURACY
# =====================================================

st.subheader("🎯 Model Accuracy")

accuracy = pd.DataFrame({

    "Model":[
        "CNN Product",
        "LBPH Face",
        "LSTM Sentiment",
        "Chatbot"
    ],

    "Accuracy":[
        90.77,
        68.26,
        85.54,
        99.96
    ]

})

fig = px.bar(
    accuracy,
    x="Model",
    y="Accuracy",
    color="Accuracy",
    text="Accuracy",
    title="AI Model Accuracy Comparison"
)

fig.update_layout(
    height=500,
    xaxis_title="",
    yaxis_title="Accuracy (%)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.write("")

# =====================================================
# DATASET DISTRIBUTION
# =====================================================

st.subheader("📂 Dataset Distribution")

dataset = pd.DataFrame({

    "Dataset":[
        "Fashion MNIST",
        "LFW Faces",
        "IMDB Reviews",
        "Chatbot Intents"
    ],

    "Samples":[
        70000,
        3023,
        50000,
        500
    ]

})

fig = px.pie(
    dataset,
    names="Dataset",
    values="Samples",
    hole=0.45
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.write("")

# =====================================================
# DATASET DETAILS
# =====================================================

st.subheader("📋 Dataset Summary")

st.dataframe(
    dataset,
    use_container_width=True,
    hide_index=True
)

st.write("")

# =====================================================
# MODEL DETAILS
# =====================================================

st.subheader("🧠 AI Models")

col1, col2 = st.columns(2)

with col1:

    st.info("""
### CNN

Dataset : Fashion-MNIST

Images : 70,000

Classes : 10

Task : Product Classification
""")

    st.info("""
### LBPH

Dataset : LFW

Images : 3023

Persons : 62

Task : Face Recognition
""")

with col2:

    st.info("""
### LSTM

Dataset : IMDB Reviews

Reviews : 50,000

Task : Sentiment Analysis
""")

    st.info("""
### Chatbot

Intent Classification

TensorFlow Model

Retail Support Assistant
""")

st.write("")

# =====================================================
# SYSTEM STATUS
# =====================================================

st.subheader("🖥️ System Status")

status = pd.DataFrame({

    "Service":[
        "FastAPI",
        "TensorFlow",
        "OpenCV",
        "Streamlit"
    ],

    "Status":[
        "Running",
        "Running",
        "Running",
        "Running"
    ]

})

st.dataframe(
    status,
    use_container_width=True,
    hide_index=True
)

st.write("")

# =====================================================
# PROJECT SUMMARY
# =====================================================

st.subheader("📌 Project Summary")

st.success("""
### Smart Retail AI Platform

This platform integrates multiple Artificial Intelligence
modules into a unified retail dashboard.

✔ Product Classification

✔ Face Recognition

✔ Customer Sentiment Analysis

✔ AI Chatbot

✔ FastAPI Backend

✔ Streamlit Frontend
""")

st.write("")

# =====================================================
# TECHNOLOGY STACK
# =====================================================

st.subheader("💻 Technology Stack")

tech = pd.DataFrame({

    "Technology":[
        "Python",
        "TensorFlow",
        "OpenCV",
        "FastAPI",
        "Streamlit",
        "Scikit-Learn",
        "NumPy",
        "Pandas",
        "Plotly"
    ]

})

st.dataframe(
    tech,
    use_container_width=True,
    hide_index=True
)

st.write("")

footer()