import streamlit as st
from styles import load_css
from components import page_title, footer
from utils import chatbot

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

# ===================================
# SESSION STATE
# ===================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ===================================
# PAGE TITLE
# ===================================

page_title(
    "🤖 Smart Retail AI Assistant",
    "Ask questions about products, customer support, returns, offers and shopping."
)

st.write("")

# ===================================
# QUICK QUESTIONS
# ===================================

st.subheader("💡 Suggested Questions")

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("🛍️ Product Information"):
        st.session_state.prompt = "Tell me about your products."

with c2:
    if st.button("🚚 Delivery"):
        st.session_state.prompt = "How long does delivery take?"

with c3:
    if st.button("💳 Payment Methods"):
        st.session_state.prompt = "What payment methods are available?"

st.write("---")

# ===================================
# CHAT HISTORY
# ===================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ===================================
# USER INPUT
# ===================================

default_prompt = st.session_state.get("prompt", "")

prompt = st.chat_input(
    "Ask your question..."
)

if default_prompt and not prompt:
    prompt = default_prompt
    st.session_state.prompt = ""

# ===================================
# CHAT PROCESSING
# ===================================

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Retail AI is thinking..."):

            result = chatbot(prompt)

            if "error" in result:

                st.error(result["error"])

            else:

                reply = result["response"]

                st.markdown(reply)

                st.progress(result["confidence"])

                st.caption(
                    f"""
Intent : **{result['intent']}**

Confidence : **{result['confidence']*100:.2f}%**
"""
                )

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":reply
        }
    )

# ===================================
# SIDEBAR
# ===================================

st.sidebar.subheader("⚙ Chat Settings")

if st.sidebar.button("🗑 Clear Conversation"):

    st.session_state.messages = []

    st.rerun()

st.sidebar.markdown("---")

st.sidebar.info(
"""
### AI Assistant

✔ Intent Classification

✔ NLP Processing

✔ Deep Learning Chatbot

✔ Instant Response
"""
)

# ===================================
# CHATBOT FEATURES
# ===================================

st.write("")

st.subheader("🚀 Features")

c1, c2 = st.columns(2)

with c1:

    st.success("""
✔ Greeting Detection

✔ Product Queries

✔ Store Information

✔ Customer Support
""")

with c2:

    st.success("""
✔ Intent Classification

✔ Natural Language Processing

✔ Instant AI Response

✔ Confidence Score
""")

st.write("")

# ===================================
# MODEL INFORMATION
# ===================================

st.subheader("🧠 Chatbot Model")

m1, m2, m3 = st.columns(3)

m1.metric(
    "Intents",
    "8"
)

m2.metric(
    "Accuracy",
    "99%"
)

m3.metric(
    "Framework",
    "TensorFlow"
)

st.write("")

footer()