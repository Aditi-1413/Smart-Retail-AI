import streamlit as st


# ==========================
# HERO SECTION
# ==========================

def hero():

    st.markdown("""

<div class="hero">

<span class="eyebrow">AI Retail Intelligence Suite</span>

<h1>Turn every product, face<br>and review into <em>insight</em>.</h1>

<p>
One platform that classifies products, recognises customers, reads sentiment
and answers questions — in real time, at retail scale.
</p>

<div class="hero-divider"></div>

</div>

""", unsafe_allow_html=True)


# ==========================
# KPI TICKER
# ==========================

def dashboard_cards():

    st.markdown("""

<div class="ticker">

<div class="ticker-item">
<span class="tick-value">10</span>
<span class="tick-label">Product Classes</span>
</div>

<div class="ticker-item">
<span class="tick-value">62</span>
<span class="tick-label">Known Faces</span>
</div>

<div class="ticker-item">
<span class="tick-value">94%</span>
<span class="tick-label">Sentiment Accuracy</span>
</div>

<div class="ticker-item">
<span class="tick-value">24/7</span>
<span class="tick-label">AI Chatbot</span>
</div>

</div>

""", unsafe_allow_html=True)


# ==========================
# FEATURE / CATALOGUE CARDS
# ==========================

def feature_cards():

    left, right = st.columns(2)

    with left:

        st.markdown("""

<div class="card">

<span class="index-num">01 — CLASSIFY</span>

<h3>👕 Product Classification</h3>

<p>

Upload a fashion image and classify it into one of the Fashion-MNIST categories using a CNN model.

</p>

</div>

""", unsafe_allow_html=True)

        st.markdown("""

<div class="card">

<span class="index-num">02 — RECOGNISE</span>

<h3>🙂 Face Recognition</h3>

<p>

Recognize faces from uploaded images using OpenCV's LBPH Face Recognizer trained on the LFW dataset.

</p>

</div>

""", unsafe_allow_html=True)

    with right:

        st.markdown("""

<div class="card">

<span class="index-num">03 — LISTEN</span>

<h3>⭐ Sentiment Analysis</h3>

<p>

Predict customer sentiment from reviews using an LSTM deep learning model.

</p>

</div>

""", unsafe_allow_html=True)

        st.markdown("""

<div class="card">

<span class="index-num">04 — RESPOND</span>

<h3>🤖 AI Chatbot</h3>

<p>

Retail chatbot capable of identifying user intent and responding intelligently.

</p>

</div>

""", unsafe_allow_html=True)


# ==========================
# VALUE PROPS
# ==========================

def value_props():

    st.markdown("""

<div class="value-strip">

<div class="value-item">
<h4>⚡ Real-Time Inference</h4>
<p>Every module returns a prediction in seconds — ready to plug into a live storefront or ops workflow.</p>
</div>

<div class="value-item">
<h4>🎯 Trained at Scale</h4>
<p>125,000+ labelled samples across four datasets ground every model in real retail data.</p>
</div>

<div class="value-item">
<h4>🧩 One Dashboard</h4>
<p>Classification, recognition, sentiment and conversation — unified in a single interface.</p>
</div>

</div>

""", unsafe_allow_html=True)


# ==========================
# PAGE TITLE
# ==========================

def page_title(title, subtitle=""):

    st.markdown(f"""

<div class="hero" style="padding:36px 40px;">

<span class="eyebrow">Module</span>

<h1 style="font-size:32px; margin-bottom:10px;">{title}</h1>

<p>{subtitle}</p>

</div>

""", unsafe_allow_html=True)


# ==========================
# RESULT CARD
# ==========================

def result_card(title, value):

    st.markdown(f"""

<div class="success-box">

<h3>{title}</h3>

<h2>{value}</h2>

</div>

""", unsafe_allow_html=True)


# ==========================
# FOOTER
# ==========================

def footer():

    st.markdown("""

<div class="footer">

<hr>

<h4>🛍️ Smart Retail AI Platform</h4>

<p>

TensorFlow · OpenCV · FastAPI · Streamlit

</p>

<p>

© 2026 Smart Retail AI — Retail Intelligence, Refined.

</p>

</div>

""", unsafe_allow_html=True)