import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
import os
from tensorflow.keras.utils import get_custom_objects, custom_object_scope
from tensorflow.keras.layers import Lambda

# Define the custom function used in Lambda layer
def custom_function(x):
    return x  # Placeholder: your actual transformation logic goes here

# Register the custom function
get_custom_objects().update({'custom_function': custom_function})

# Define the model loading function with custom scope for Lambda layer
def load_model_with_custom_objects(model_path):
    with custom_object_scope({'TFOpLambda': Lambda, 'custom_function': custom_function}):
        return tf.keras.models.load_model(model_path)
# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__),r"..\new_model3.keras")
loaded_model = load_model_with_custom_objects(MODEL_PATH)

def app():
    def predict_intensity(model, image_tensor):
        prediction = model.predict(image_tensor)
        return prediction[0][0]*1.85  # Assuming regression

    def classify_cyclone(intensity_knots):
        if intensity_knots < 17:
            return "Low Pressure", 5
        elif 17 <= intensity_knots < 27:
            return "Depression", 20
        elif 27 <= intensity_knots < 33:
            return "Deep Depression", 40
        elif 33 <= intensity_knots < 47:
            return "Cyclonic Storm", 70
        elif 47 <= intensity_knots < 63:
            return "Severe Cyclonic Storm", 85
        else:
            return "Super Cyclone", 95

    st.markdown("## 🌩️ Cyclone Intensity Estimation", unsafe_allow_html=True)
    st.markdown("🖼️ **Sample Image**")
    st.image("30.jpg", caption="🌀 Sample Cyclone Image")

    uploaded_file = st.file_uploader("📤 Upload a cyclone image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="✅ Uploaded Image")

        # Preprocess
        img_array = np.array(image)
        img_resized = tf.image.resize(img_array, (256, 256))
        img_tensor = tf.expand_dims(img_resized, 0) / 255.0

        if st.button("⚡ 🎯 Predict Intensity"):
            intensity = predict_intensity(loaded_model, img_tensor)
            disturbance_type, cyclone_chance = classify_cyclone(intensity)

            st.success(f"☁️ **Predicted Intensity**: 📈 **{intensity:.2f} KNOTS**")
            st.info(f"📊 **Category**: `{disturbance_type}`")
            st.warning(f"🎯 **Estimated Chance of Cyclone**: **{cyclone_chance}%**")

            if cyclone_chance >= 85:
                st.error("🚨 Severe Cyclonic Activity Detected!")
            elif cyclone_chance >= 70:
                st.warning("⚠️ Moderate Cyclonic Storm Detected.")
            elif cyclone_chance >= 40:
                st.info("🔍 Possibility of a depression.")
            else:
                st.success("✅ Low chance of cyclone.")
