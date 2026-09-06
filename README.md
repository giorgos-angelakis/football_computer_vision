# ⚽ AI-Powered Football Analytics System

<img width="1294" height="654" alt="Capture" src="https://github.com/user-attachments/assets/4a25314d-9738-4036-bf1a-a0e548af21b5" />

An advanced, end-to-end computer vision pipeline designed to automatically extract actionable sports analytics from raw match footage. This system detects, tracks, and analyzes player movements, calculates real-world speeds, and segments teams using state-of-the-art deep learning and classical computer vision techniques.

## 📌 Project Overview
In modern sports analytics, extracting physical metrics from standard broadcast video requires overcoming significant technical hurdles like dynamic camera panning, occlusion, and perspective distortion. This project solves these challenges by combining a custom-trained **YOLOv8** object detector with **Optical Flow** and **Perspective Transformation**, creating a highly accurate tracking system that measures distance in real-world meters rather than raw pixels.

This repository serves as a showcase of production-ready machine learning engineering, highlighting skills in model fine-tuning, unsupervised learning, and complex data pipelines.

## 🚀 Key Features

* **Custom Object Detection:** Fine-tuned YOLOv8 architecture on a custom dataset to detect players, referees, and the football with high precision, improving upon baseline pre-trained models.
* **Robust Multi-Object Tracking:** Persistent tracking of entities across frames, maintaining unique IDs despite occlusions and overlapping bounding boxes.
* **Algorithmic Team Segmentation:** Utilized Unsupervised Machine Learning (**K-Means Clustering**) to segment player bounding boxes, extract dominant t-shirt colors, and automatically assign players to their respective teams without manual labeling.
* **Camera Motion Compensation:** Implemented **Optical Flow** to calculate and negate camera panning and zooming, ensuring player movement data is strictly isolated from camera movement.
* **Spatial Depth & Real-World Physics:** Applied OpenCV **Perspective Transformation** to map 2D pixel coordinates to a 3D real-world plane, allowing the system to calculate precise physical metrics like total distance covered and current running speed in km/h.

## 🧠 System Architecture
```mermaid
graph TD
    A[Broadcast Video] --> B[Fine-tuned YOLOv8 Object Detection]
    A --> C[Optical Flow Analysis Camera Displacement]
    B --> D["Persistent Tracker (ByteTrack / DeepSORT)"]
    D --> E["K-Means Clustering (Team Kit Segmenter)"]
    E --> F["Perspective Homography Matrix Transformation (H)"]
    C --> F
    F --> G["Kinematic Metrics Engine (Speed km/h, Distance m)"]

1. **Detection & Tracking:** Frames are passed through the fine-tuned YOLOv8 model. Detections are handed off to a tracker to maintain state across the video timeline.
2. **Feature Extraction:** Bounding box crops are analyzed. Backgrounds are masked out, and the remaining pixel data is clustered via K-Means to identify team colors.
3. **Kinematic Calculations:** 
   - *Optical flow* tracks static background features to measure camera shift.
   - *Perspective mapping* transforms the adjusted pixel coordinates into a top-down, real-world metric space.
4. **Data Overlay:** Speeds, distances, and team affiliations are rendered back onto the original video frames in real-time.

## 🛠️ Tech Stack
* **Deep Learning:** PyTorch, Ultralytics (YOLOv8)
* **Computer Vision:** OpenCV, Scikit-Learn (K-Means)
* **Data Processing:** NumPy, Pandas
* **Environment:** Python 3.x

## 📈 Results & Visuals
**Team Segmentation**
Unsupervised clustering accurately grouping players by their extracted dominant colors.
**Real-time Kinematics**
The final output showcasing tracking persistence and real-time physical metric overlays.



https://github.com/user-attachments/assets/50d17399-72ea-45c5-8e01-200c66d57377

