import streamlit as st
from styles import load_css
from components import page_title, footer
from utils import predict_sentiment

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="⭐",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

# ============================================
# SESSION STATE
# ============================================

if "sentiment_history" not in st.session_state:
    st.session_state.sentiment_history = []

# ============================================
# PAGE TITLE
# ============================================

page_title(
    "⭐ Customer Sentiment Analysis",
    "Analyze customer reviews using the trained LSTM model."
)

st.write("")

# ============================================
# REVIEW INPUT
# ============================================

review = st.text_area(
    "Enter Customer Review",
    height=220,
    placeholder="Example:\nThis product is amazing. The quality exceeded my expectations."
)

st.write("")

if st.button("🚀 Analyze Review"):

    if review.strip() == "":

        st.warning("Please enter a review.")

    else:

        with st.spinner("Analyzing sentiment..."):

            result = predict_sentiment(review)

        if "error" in result:

            st.error(result["error"])

        else:

            sentiment = result["sentiment"]
            confidence = float(result["confidence"])

            st.success("Analysis Completed")

            c1, c2 = st.columns([1, 1])

            with c1:

                if sentiment.lower() == "positive":

                    st.success("😊 Positive Review")

                else:

                    st.error("☹️ Negative Review")

                st.metric(
                    "Prediction",
                    sentiment
                )

            with c2:

                st.metric(
                    "Confidence",
                    f"{confidence*100:.2f}%"
                )

                st.progress(confidence)

            st.info(
                f"The review has been classified as **{sentiment}**."
            )

            st.session_state.sentiment_history.append(
                {
                    "Review": review[:50] + "...",
                    "Sentiment": sentiment,
                    "Confidence": f"{confidence*100:.2f}%"
                }
            )

st.write("")

# ============================================
# REVIEW HISTORY
# ============================================

st.subheader("📜 Recent Analyses")

if len(st.session_state.sentiment_history):

    st.dataframe(
        st.session_state.sentiment_history,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No reviews analyzed yet.")

st.write("")

# ============================================
# MODEL INFORMATION
# ============================================

st.subheader("🧠 LSTM Model")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Dataset",
    "IMDB Reviews"
)

c2.metric(
    "Reviews",
    "50,000"
)

c3.metric(
    "Accuracy",
    "85.54%"
)

st.write("")

# ============================================
# DATASET DETAILS
# ============================================

st.subheader("📂 Dataset Information")

left, right = st.columns(2)

with left:

    st.info("""
### IMDB Movie Reviews

✔ 50,000 Reviews

✔ Positive Reviews

✔ Negative Reviews

✔ Binary Classification
""")

with right:

    st.info("""
### Deep Learning Pipeline

✔ Tokenization

✔ Padding

✔ Embedding Layer

✔ LSTM Layer

✔ Dense Output
""")

st.write("")

# ============================================
# SENTIMENT GUIDE
# ============================================

st.subheader("📘 Understanding Results")

st.markdown("""

| Sentiment | Meaning |
|------------|---------|
| 😊 Positive | Customer is satisfied |
| ☹️ Negative | Customer is dissatisfied |

Confidence indicates how certain the model is about its prediction.

""")

st.write("")

footer()