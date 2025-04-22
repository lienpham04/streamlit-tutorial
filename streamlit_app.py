import streamlit as st

st.title('🚗 Multi-Car Detection with YOLO')

# st.write('Hello world!')
st.info('👨🏻‍💻 Welcome to the app')

# expander
with st.expander('Project Introduction'):
    st.write('Say something here!')

# sidebar
with st.sidebar:
    st.header("Settings")
    input_type = st.radio("Select Input Type:", ["Upload Image", "Upload Video", "Live Stream"])
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


