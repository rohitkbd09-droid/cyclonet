import streamlit as st
from multiapp import MultiApp
from apps import home, cyclone_app, dataset

app = MultiApp()

st.set_page_config(page_title="CycloNet - Cyclone Intensity Predictor", layout="wide")

# Custom Background
st.markdown("""
<style>
    .stApp {
        background-image: url("https://cdn.pixabay.com/photo/2020/05/17/17/15/tornado-5182693_1280.jpg");
        background-attachment: fixed;
        background-size: cover;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("##  CycloNet")
st.markdown("""
Welcome to CycloNet - a Deep Learning Powered Cyclone Intensity Estimation Tool developed by [Srinivas Ramavath &&  Mahesh Uppari](https://github.com/srinivasramavath).
""", unsafe_allow_html=True)

app.add_app("🏠 Home", home.app)
app.add_app("📊 Dataset", dataset.app)
app.add_app("🌀 Cyclone Intensity Estimator", cyclone_app.app)

app.run()
