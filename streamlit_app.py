import streamlit as st

st.title('🚗 Multi-Car Detection with YOLO')

# st.write('Hello world!')
st.info('👨🏻‍💻 Welcome to the app')

# expander
with st.expander('Project Introduction'):
    st.write('Say something here!')
    st.write('Say more')

# sidebar
with st.sidebar:
    st.header("Settings")
    input_type = st.radio("Select Input Type:", ["Upload Image", "Upload Video", "Live Stream (optional)"])
    confidence = st.slider("Detection Confidence Threshold", 0.1, 1.0, 0.5)

