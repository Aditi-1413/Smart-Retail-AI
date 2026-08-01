import streamlit as st

st.set_page_config(
    page_title="Smart Retail AI",
    page_icon="🛍️",
    layout="wide"
)

home = st.Page("app_home.py", title="Home", icon="🏠")
dashboard = st.Page("pages/1_Dashboard.py", title="Dashboard", icon="📊")
product = st.Page("pages/2_Product.py", title="Product Classification", icon="👕")
face = st.Page("pages/3_Face.py", title="Face Recognition", icon="🙂")
sentiment = st.Page("pages/4_Sentiment.py", title="Sentiment Analysis", icon="⭐")
chatbot = st.Page("pages/5_Chatbot.py", title="AI Chatbot", icon="🤖")
analytics = st.Page("pages/6_Analytics.py", title="Analytics", icon="📈")

pg = st.navigation([
    home,
    dashboard,
    product,
    face,
    sentiment,
    chatbot,
    analytics,
])

pg.run()