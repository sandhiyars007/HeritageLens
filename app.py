import streamlit as st
from PIL import Image
from ocr import extract_text

st.set_page_config(
    page_title="HeritageLens",
    page_icon="🏛️",
    layout="centered"
)

st.title("🏛️ HeritageLens")
st.subheader("AI-Based Tamil Historical Inscription Recognition System")

st.write(
    "Upload an image of a Tamil historical inscription "
    "to extract its text using OCR."
)

uploaded_file = st.file_uploader(
    "📸 Upload Inscription Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Inscription",
        use_container_width=True
    )

    if st.button("🔍 Extract Text"):

        with st.spinner("Processing image..."):
            text = extract_text(image)

        st.subheader("📝 Extracted Text")

        if text:
            st.text_area(
                "OCR Result",
                text,
                height=250
            )
        else:
            st.warning("No text could be detected.")
