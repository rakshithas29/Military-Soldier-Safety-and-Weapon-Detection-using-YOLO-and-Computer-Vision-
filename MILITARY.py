import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
import os
st.set_page_config(page_title="Military Threat Detection", layout="wide")
st.title("🪖 Military Soldier Safety & Threat Detection System")


MODEL_PATH = r"C:\Users\Rakshitha\runs\detect\military_4class_yolo6\weights\best.pt"

if not os.path.exists(MODEL_PATH):
    st.error("❌ Model not found. Check path.")
    st.stop()

model = YOLO(MODEL_PATH)


class_names = {
    0: "weapon",
    1: "military_truck",
    2: "military_vehicle",
    3: "military_artillery"
}


st.sidebar.header("⚙ Settings")
confidence = st.sidebar.slider("Confidence Threshold", 0.1, 1.0, 0.3)
input_type = st.sidebar.radio("Select Input Type", ["Image"])

def classify_threat(detected_classes):

    if len(detected_classes) == 0:
        return "⚠ No Objects Detected"

    if "weapon" in detected_classes:
        return "🔴 HIGH THREAT - Weapon Detected"

    if "military_artillery" in detected_classes:
        return "🔴 HIGH THREAT - Artillery Detected"

    if "military_vehicle" in detected_classes:
        return "🟠 MEDIUM THREAT - Military Vehicle"

    if "military_truck" in detected_classes:
        return "🟡 LOW THREAT - Logistics Vehicle"

    return "✅ NO THREAT"



if input_type == "Image":

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    if uploaded_file:

        image = Image.open(uploaded_file)
        image_np = np.array(image)

        results = model.predict(image_np, conf=confidence)

        detected_classes = []
        total_detections = 0

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                detected_classes.append(class_names[cls_id])
                total_detections += 1

        annotated_image = results[0].plot()

        col1, col2 = st.columns(2)

        with col1:
            st.image(image_np, caption="Original Image", use_column_width=True)

        with col2:
            st.image(annotated_image, caption="Detected Output", use_column_width=True)

        
        st.markdown("### 📊 Detection Summary")
        st.write("Total Objects Detected:", total_detections)
        st.write("Detected Classes:", detected_classes)

        threat_status = classify_threat(detected_classes)

        st.markdown("## 🚨 Threat Assessment")
        st.subheader(threat_status)

        
        result_pil = Image.fromarray(annotated_image)
        result_pil.save("result.jpg")

        with open("result.jpg", "rb") as f:
            st.download_button(
                label="Download Result Image",
                data=f,
                file_name="detection_result.jpg"
            )

st.markdown("---")
st.success("System Ready for Deployment 🚀")
