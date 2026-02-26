# Military-Soldier-Safety-and-Weapon-Detection-using-YOLO-and-Computer-Vision-



YOLOv8-Based Real-Time Military Object Detection

---

## 📌 Project Overview

This project implements a **real-time military threat detection system** using **YOLOv8n object detection model**.

The system detects and classifies:

* 🔫 Weapon
* 🚛 Military Truck
* 🚙 Military Vehicle
* 🎯 Military Artillery

The goal is to enhance **soldier safety and battlefield awareness** using AI-powered computer vision.

---

## 🎯 Problem Statement

In military surveillance scenarios, detecting threats such as weapons and heavy artillery quickly is critical. Manual monitoring is slow and error-prone.

This project provides:

* Automated object detection
* Threat-level classification
* Real-time inference capability
* Streamlit-based user interface

---

## 🧠 Model Used

This project uses:

* YOLOv8
* YOLOv8n (Nano version – lightweight and fast)

Why YOLOv8n?

* Fast inference
* Low computational cost
* Suitable for CPU deployment
* Good balance of speed and accuracy

---

## 🏗 Architecture Overview

The system pipeline:

1. Dataset preprocessing
2. 4-class dataset creation
3. Model training using YOLOv8n
4. Validation & evaluation
5. Streamlit deployment

---

## 📊 Model Performance

Validation Dataset:

* 533 Images
* 930 Object Instances

### 🔹 Overall Metrics

| Metric       | Score |
| ------------ | ----- |
| Precision    | 72.8% |
| Recall       | 68.8% |
| mAP@0.5      | 72.4% |
| mAP@0.5:0.95 | 50.4% |

### 🔹 Class-wise Performance

| Class              | mAP@0.5 |
| ------------------ | ------- |
| Weapon             | 74.7%   |
| Military Vehicle   | 75.1%   |
| Military Artillery | 71.2%   |
| Military Truck     | 68.3%   |

Inference Speed:

* ~53ms per image
* ~18–19 FPS (CPU)

---

## ⚙ Technologies Used

* Python
* OpenCV
* PyTorch
* Ultralytics YOLOv8
* Streamlit
* NumPy
* Matplotlib

---

## 📂 Project Structure

```
Military_Threat_Detection/
│
├── dataset/
│   ├── train/
│   ├── val/
│   ├── test/
│
├── runs/
│   └── detect/
│
├── military_4class.yaml
├── train.py
├── app.py (Streamlit app)
└── README.md
```

---

## 🚀 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/military-threat-detection.git
cd military-threat-detection
```

### 2️⃣ Install Dependencies

```bash
pip install ultralytics
pip install streamlit
pip install opencv-python
pip install numpy
pip install pillow
```

---

## 🏋 Model Training

```bash
yolo detect train \
data=military_4class.yaml \
model=yolov8n.pt \
epochs=40 \
imgsz=640 \
batch=4
```

---

## 📊 Model Validation

```bash
yolo detect val \
model=runs/detect/military_4class_yolo/weights/best.pt \
data=military_4class.yaml
```

---

## 🖥 Run Streamlit App

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 🚨 Threat Classification Logic

The system classifies threats into:

* 🔴 HIGH THREAT → Weapon / Artillery
* 🟠 MEDIUM THREAT → Military Vehicle
* 🟡 LOW THREAT → Military Truck
* ⚠ No Detection

---

## 📈 Future Improvements

* Upgrade to YOLOv8m or YOLOv8l
* Add video detection support
* Apply advanced data augmentation
* Hyperparameter tuning
* Increase dataset size
* Deploy on edge device (Jetson Nano)


