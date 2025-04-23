import streamlit as st
import os
from PIL import Image
from serving_pipeline.utils import get_image_array, get_boxes_for_image, draw_boxes_on_image

st.title('🚗 Multi-label Object Detection with YOLOoooo')

# st.write('Hello world!')
st.info('👨🏻‍💻 Welcome to the app')

# expander
with st.expander('Project Introduction'):
    st.write('Say something here!')

# sidebar
with st.sidebar:
    st.header("Settings")
    input_type = st.radio("Select Input Type:", ["Upload Image", "Upload Video"])
    confidence = st.slider("Detection Confidence Threshold", 0.1, 1.0, 0.5)

# input
if input_type == "Upload Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
elif input_type == "Upload Video":
    uploaded_file = st.file_uploader("Upload a video", type=["mp4", "mov"])

# output
if uploaded_file:
    image = load_image(uploaded_file)
    results = model(image)
    st.image(results.render()[0], caption="Detection Result", use_column_width=True)

st.set_page_config(page_title="Multi-label Object Detection", layout="centered")
st.title("🧠 Visualize Labels from CSV")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image_np = get_image_array(uploaded_file)
    st.image(image_np, caption="Uploaded Image", use_column_width=True)

    if st.button("Draw Bounding Boxes"):
        image_id = os.path.splitext(uploaded_file.name)[0]
        h, w = image_np.shape[:2]
        boxes = get_boxes_for_image(image_id, w, h)
        image_with_boxes = draw_boxes_on_image(image_np.copy(), boxes)
        st.image(image_with_boxes, caption="Labeled Bounding Boxes", use_column_width=True)

