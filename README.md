# DEEPVISION-Non-Invasive-Heart-Attack-Risk-Prediction-via-Retinal-Image-Analysis

# Overview
DeepVision is a deep learning-based healthcare system that predicts heart attack risk using retinal fundus images.
<br>
Traditional cardiac diagnosis methods are often invasive, expensive, and inaccessible, especially in rural areas. This project provides a non-invasive, cost-effective, and automated screening solution using computer vision and deep learning.

 # Problem Statement
Conventional heart disease detection methods such as ECG, angiography, and blood tests:
<br>
Require specialized infrastructure<br>
Are expensive and time-consuming<br>
Are not accessible in remote or rural areas<br>

👉 There is a need for a low-cost, non-invasive, and scalable early detection system.

# Proposed Solution
DeepVision leverages the correlation between retinal blood vessels and cardiovascular health.
<br>
✔ Input: Retinal Fundus Image<br>
✔ Processing: CLAHE + Deep Learning<br>
✔ Output: Heart Attack Risk Category<br>

The model classifies patients into 5 risk levels:
<br>
🟢 No <br>
🟡 Low Risk<br>
🟠 Moderate Risk<br>
🔴 High Risk<br>
⚫ Critical Risk

# Model Architecture
Base Model: EfficientNetB0 (Transfer Learning)<br>
Framework: TensorFlow / Keras<br>
Input Size: 224 × 224<br>
Output: 5-class Softmax

# Key Features:
Fine-tuned EfficientNetB0<br>
Dropout for regularization<br>
Global Average Pooling<br>
1-Step Fine-Tuning Strategy<br>

# System Pipeline
Image Input<br>
Preprocessing<br>
Black border cropping<br>
CLAHE enhancement<br>
Normalization<br>
Data Augmentation<br>
Model Training<br>
Prediction & Visualization

# Dataset
Dataset: APTOS 2019 Blindness Detection (Kaggle)<br>
Type: Retinal Fundus Images<br>
Classes: 5 (0–4 mapped to risk levels)<br>
Split: 80% Training / 20% Validation

# Tech Stack
Category	Tools<br>
Language	Python<br>
Deep Learning	TensorFlow, Keras<br>
Image Processing	OpenCV<br>
Data Handling	Pandas, NumPy<br>
Visualization	Matplotlib, Seaborn<br>
Evaluation	Scikit-learn

📁 # Project Structure
DeepVision/<br>
│<br>
├── DATASET/<br>
│   ├── train_1.csv<br>
│   └── train_images/<br>
│
├── effnet_b0_final.keras<br>
├── new_main.ipynb<br>
├── requirements.txt<br>
└── README.md<br>

# Preprocessing Steps
Convert BGR → RGB<br>
Remove black borders<br>
Resize to 224×224<br>
Apply CLAHE (Contrast Enhancement)<br>
Normalize pixel values

# Model Performance
Metric	Description<br>
Accuracy	Overall correctness<br>
Precision	Prediction accuracy per class<br>
Recall	Detection ability<br>
F1 Score	Balance of precision & recall

👉# Sample Result:

Accuracy ≈ 64%<br>
Strong performance in low-risk classes

# Inference
The model provides:<br>

Predicted Risk Level<br>
Confidence Score<br>
Probability Distribution Graph<br>
predict_risk("image.png", model)

# Evaluation
Confusion Matrix<br>
Classification Report<br>
Accuracy & Loss Curves<br>

# Applications
 Preventive Healthcare Screening<br>
 Rural & Remote Medical Support<br>
 Telemedicine Platforms<br>
 Clinical Decision Support<br>
 Insurance Risk Assessment

⚠️ # Limitations
Dataset not originally designed for cardiac prediction<br>
Class imbalance (high/critical risk underrepresented)<br>
No explainability (black-box model)<br>
No real-world clinical validation yet

# Future Enhancements
 Grad-CAM visualization (Explainable AI<br>
 Multimodal learning (add clinical data)<br>
 Mobile App / Web API deployment<br>
 Clinical validation with hospitals<br>
 Federated learning for privacy
 
# References
Poplin et al. (2018) – Google Research<br>
EfficientNet Paper (ICML 2019)<br>
APTOS 2019 Dataset (Kaggle)<br>
Deep Learning – Goodfellow et al.<br>

# Author
Megha R

Contribution<br>
Feel free to fork, contribute, and improve the project!

# License

This project is for academic and research purposes.
