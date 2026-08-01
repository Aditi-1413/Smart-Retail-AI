import streamlit as st
from styles import load_css
from components import page_title, footer
from utils import predict_product

st.set_page_config(
    page_title="Product Classification",
    page_icon="👕",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

# ==========================
# SESSION STATE
# ==========================

if "product_history" not in st.session_state:
    st.session_state.product_history = []

# ==========================
# PAGE TITLE
# ==========================

page_title(
    "👕 Product Classification",
    "Upload a clothing image and let the AI classify the product."
)

st.write("")

# ==========================
# MAIN LAYOUT
# ==========================

left, right = st.columns([1, 1])

with left:

    st.subheader("📤 Upload Product Image")

    uploaded = st.file_uploader(
        "Choose an image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded:

        st.image(
            uploaded,
            caption="Uploaded Image",
            use_container_width=True
        )

with right:

    st.subheader("🤖 Prediction")

    if uploaded:

        if st.button("🚀 Predict Product"):

            with st.spinner("Analyzing image..."):

                result = predict_product(uploaded)

            if "error" in result:

                st.error(result["error"])

            else:

                product = result["product"]
                confidence = float(result["confidence"])

                st.success("Prediction Completed")

                st.markdown("## 👕 " + product)

                st.metric(
                    "Confidence",
                    f"{confidence*100:.2f}%"
                )

                st.progress(confidence)

                st.info(
                    f"The uploaded product is classified as **{product}**."
                )

                st.session_state.product_history.append(
                    {
                        "Product": product,
                        "Confidence": f"{confidence*100:.2f}%"
                    }
                )

    else:

        st.info("Upload an image to begin.")

st.write("")

# ==========================
# PRODUCT DETAILS
# ==========================

st.subheader("📋 Product Information")

product_info = {
    "T-shirt": "Casual upper-body garment.",
    "Trouser": "Full-length lower-body clothing.",
    "Pullover": "Warm knitted sweater.",
    "Dress": "One-piece garment.",
    "Coat": "Outerwear for cold weather.",
    "Sandal": "Open footwear.",
    "Shirt": "Collared upper garment.",
    "Sneaker": "Casual sports shoe.",
    "Bag": "Fashion accessory.",
    "Ankle Boot": "Boot covering the ankle."
}

if uploaded and "result" in locals():

    st.markdown(
        f"""
### {product}

{product_info.get(product,'No description available.')}

"""
    )

else:

    st.write("Prediction details will appear here.")

st.write("")

# ==========================
# PREDICTION HISTORY
# ==========================

st.subheader("📜 Recent Predictions")

if len(st.session_state.product_history):

    st.dataframe(
        st.session_state.product_history,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No predictions yet.")

st.write("")

# ==========================
# MODEL INFORMATION
# ==========================

st.subheader("🧠 CNN Model")

c1, c2, c3 = st.columns(3)

c1.metric("Dataset", "Fashion-MNIST")

c2.metric("Classes", "10")

c3.metric("Accuracy", "90.77%")

st.write("")

footer()