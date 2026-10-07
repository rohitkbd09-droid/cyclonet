import streamlit as st

def app():
    st.title('🛰️ CycloNet - Cyclone Intensity Estimator')
    
    st.markdown("""
    Welcome to **CycloNet** — a web-based interface for estimating cyclone intensity using infrared satellite images from **INSAT-3D** ☁️.

    📡 **How it works**  
    Upload an **IR satellite image** of a cyclone, and our **Deep Convolutional Neural Network (CNN)** — trained on curated cyclone imagery — will predict the **intensity in knots**.

    🧠 **Why CycloNet?**  
    Traditional systems rely heavily on manual center detection. CycloNet simplifies this by directly analyzing the **full satellite image** using deep learning.

    🔍 **Features:**  
    - Upload satellite images (JPEG/PNG)  
    - Real-time intensity prediction  
    - Clear categorization of cyclone types  
    - Easy-to-use & accurate 🚀

    🗃️ **Dataset:**  
    Curated from raw **INSAT-3D IR** satellite captures via the **MOSDAC** server.

    ⛈️ **Built with:**  
    TensorFlow • Python • Streamlit • Satellite Meteorology expertise
    """)
