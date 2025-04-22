import streamlit as st

st.title('🚗 Multi-Car Detection with YOLO')

# st.write('Hello world!')
st.info('👨🏻‍💻 Welcome to the app')

# sidebar
with st.sidebar:
    st.header("Settings")
    input_type = st.radio("Select Input Type:", ["Upload Image", "Upload Video", "Live Stream (optional)"])
    confidence = st.slider("Detection Confidence Threshold", 0.1, 1.0, 0.5)

