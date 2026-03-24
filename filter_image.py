# pip install streamlit
# python -m streamlit run filename.py

import streamlit as st
from PIL import Image, ImageFilter

# 🎨 Page config (NEW)
st.set_page_config(
    page_title="Image Filter App",
    page_icon="🎨",
    layout="wide"
)

# 🎯 Title + subtitle
st.title("🎨 Image Filter Studio")
st.markdown("Transform your images with stylish filters ✨")

# 📂 File uploader (centered feel using columns)
col1, col2, col3 = st.columns([1,2,1])
with col2:
    file = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png"]
    )

if file is not None:
    img = Image.open(file)

    # 🎛️ Sidebar controls (NEW UI upgrade)
    st.sidebar.header("⚙️ Controls")

    option = st.sidebar.selectbox(
        "Choose a filter",
        ["Original", "Grayscale", "Blur", "Contour", "Edge Enhance", "Sharpen"]
    )

    blur_strength = st.sidebar.slider("Blur Intensity", 1, 10, 2)

    # 🧠 Apply filters
    filtered_img = img.copy()

    if option == "Grayscale":
        filtered_img = img.convert("L")

    elif option == "Blur":
        for _ in range(blur_strength):  # stronger blur loop
            filtered_img = filtered_img.filter(ImageFilter.BLUR)

    elif option == "Contour":
        filtered_img = img.filter(ImageFilter.CONTOUR)

    elif option == "Edge Enhance":
        filtered_img = img.filter(ImageFilter.EDGE_ENHANCE)

    elif option == "Sharpen":
        filtered_img = img.filter(ImageFilter.SHARPEN)

    # 🖼️ Show images side by side
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📷 Original")
        st.image(img, use_container_width=True)

    with col2:
        st.subheader(f"✨ {option}")
        st.image(filtered_img, use_container_width=True)

    # 💾 Download button (NEW)
    st.download_button(
        label="⬇️ Download Filtered Image",
        data=filtered_img.tobytes(),
        file_name="filtered_image.png",
        mime="image/png"
    )

else:
    st.info("👆 Upload an image to get started")