import streamlit as st
import face_recognition
from PIL import Image
import numpy as np

st.title("Face Recognition App")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    image_np = np.array(image)
    face_locations = face_recognition.face_locations(image_np)
    
    st.write(f"Total faces found: {len(face_locations)}")
