import streamlit as st
from styles import load_css
from components import page_title, footer
from utils import recognize_face

st.set_page_config(
    page_title="Face Recognition",
    page_icon="🙂",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

# ==========================
# SESSION STATE
# ==========================

if "face_history" not in st.session_state:
    st.session_state.face_history = []

# ==========================
# PAGE TITLE
# ==========================

page_title(
    "🙂 Face Recognition",
    "Upload a face image to identify the person using the trained LBPH model."
)

st.write("")

# ==========================
# MAIN LAYOUT
# ==========================

left, right = st.columns([1, 1])

with left:

    st.subheader("📤 Upload Face Image")

    uploaded = st.file_uploader(
        "Choose an image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded:

        st.image(
            uploaded,
            caption="Uploaded Face",
            use_container_width=True
        )

with right:

    st.subheader("🤖 Recognition Result")

    if uploaded:

        if st.button("🔍 Recognize Face"):

            with st.spinner("Recognizing Face..."):

                result = recognize_face(uploaded)

            if "error" in result:

                st.error(result["error"])

            else:

                person = result["person"]

                distance = result.get(
                    "distance",
                    result.get("confidence", 0)
                )

                st.success("Face Recognition Completed")

                st.markdown(f"## 👤 {person}")

                try:

                    confidence = max(0, 100 - float(distance))

                    st.metric(
                        "Recognition Score",
                        f"{confidence:.2f}%"
                    )

                    st.progress(confidence / 100)

                except:

                    st.metric(
                        "Distance",
                        distance
                    )

                st.info(
                    f"The uploaded face has been identified as **{person}**."
                )

                st.session_state.face_history.append(
                    {
                        "Person": person,
                        "Distance": distance
                    }
                )

    else:

        st.info("Upload a face image to begin.")

st.write("")

# ==========================
# PERSON DETAILS
# ==========================

st.subheader("👤 Person Details")

if uploaded and "result" in locals():

    st.markdown(f"""
### {person}

The uploaded image has been matched with the trained LFW face dataset.

Recognition was performed using the **Local Binary Pattern Histogram (LBPH)** algorithm.

""")

else:

    st.write("Recognition details will appear here.")

st.write("")

# ==========================
# RECOGNITION HISTORY
# ==========================

st.subheader("📜 Recognition History")

if len(st.session_state.face_history):

    st.dataframe(
        st.session_state.face_history,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No faces recognized yet.")

st.write("")

# ==========================
# MODEL INFORMATION
# ==========================

st.subheader("🧠 Face Recognition Model")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Algorithm",
    "LBPH"
)

c2.metric(
    "Dataset",
    "LFW"
)

c3.metric(
    "Known Persons",
    "62"
)

st.write("")

# ==========================
# DATASET DETAILS
# ==========================

st.subheader("📂 Dataset Statistics")

col1, col2 = st.columns(2)

with col1:

    st.info("""
**Dataset Name**

Labeled Faces in the Wild (LFW)

- Images : 3023
- Persons : 62
- Grayscale Images
""")

with col2:

    st.info("""
**Recognition Pipeline**

✔ Image Upload

✔ Face Detection

✔ LBPH Feature Extraction

✔ Person Prediction
""")

st.write("")

footer()