# MeghaTec-DEEPVISION-Non-Invasive-Heart-Attack-Risk-Prediction-via-Retinal-Image-Analysis
# Overview

DeepVision is a deep learning-based healthcare system that predicts heart attack risk using retinal fundus images.

Traditional cardiac diagnosis methods are often invasive, expensive, and inaccessible, especially in rural areas. This project provides a non-invasive, cost-effective, and automated screening solution using computer vision and deep learning.

 # Problem Statement

Conventional heart disease detection methods such as ECG, angiography, and blood tests:

Require specialized infrastructure
Are expensive and time-consuming
Are not accessible in remote or rural areas

👉 There is a need for a low-cost, non-invasive, and scalable early detection system.

# Proposed Solution

DeepVision leverages the correlation between retinal blood vessels and cardiovascular health.

✔ Input: Retinal Fundus Image
✔ Processing: CLAHE + Deep Learning
✔ Output: Heart Attack Risk Category

The model classifies patients into 5 risk levels:

🟢 No Risk
🟡 Low Risk
🟠 Moderate Risk
🔴 High Risk
⚫ Critical Risk

# Model Architecture
Base Model: EfficientNetB0 (Transfer Learning)
Framework: TensorFlow / Keras
Input Size: 224 × 224
Output: 5-class Softmax

# Key Features:
Fine-tuned EfficientNetB0
Dropout for regularization
Global Average Pooling
1-Step Fine-Tuning Strategy

# System Pipeline
Image Input
Preprocessing
Black border cropping
CLAHE enhancement
Normalization
Data Augmentation
Model Training
Prediction & Visualization

# Dataset
Dataset: APTOS 2019 Blindness Detection (Kaggle)
Type: Retinal Fundus Images
Classes: 5 (0–4 mapped to risk levels)
Split: 80% Training / 20% Validation

# Tech Stack
Category	Tools
Language	Python
Deep Learning	TensorFlow, Keras
Image Processing	OpenCV
Data Handling	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Evaluation	Scikit-learn

📁 # Project Structure
DeepVision/
│
├── DATASET/
│   ├── train_1.csv
│   └── train_images/
│
├── effnet_b0_final.keras
├── new_main.ipynb
├── requirements.txt
└── README.md

3 Preprocessing Steps
Convert BGR → RGB
Remove black borders
Resize to 224×224
Apply CLAHE (Contrast Enhancement)
Normalize pixel values

# Model Performance
Metric	Description
Accuracy	Overall correctness
Precision	Prediction accuracy per class
Recall	Detection ability
F1 Score	Balance of precision & recall

👉# Sample Result:

Accuracy ≈ 64%
Strong performance in low-risk classes

# Inference
The model provides:

Predicted Risk Level
Confidence Score
Probability Distribution Graph
predict_risk("image.png", model)

# Evaluation
Confusion Matrix
Classification Report
Accuracy & Loss Curves

# Applications
 Preventive Healthcare Screening
 Rural & Remote Medical Support
 Telemedicine Platforms
 Clinical Decision Support
 Insurance Risk Assessment

⚠️ # Limitations
Dataset not originally designed for cardiac prediction
Class imbalance (high/critical risk underrepresented)
No explainability (black-box model)
No real-world clinical validation yet

# Future Enhancements
 Grad-CAM visualization (Explainable AI)
 Multimodal learning (add clinical data)
 Mobile App / Web API deployment
 Clinical validation with hospitals
 Federated learning for privacy
 
# References
Poplin et al. (2018) – Google Research
EfficientNet Paper (ICML 2019)
APTOS 2019 Dataset (Kaggle)
Deep Learning – Goodfellow et al.
#Author

Megha R
MCA Student | Aspiring Data Scientist

# Contribution

Feel free to fork, contribute, and improve the project!

# License

This project is for academic and research purposes.
