# 🌧️ Rainfall Prediction System using Machine Learning

An end-to-end **Machine Learning project** that predicts whether rainfall will occur based on meteorological parameters using a **Random Forest Classifier**.  
The project includes data preprocessing, exploratory data analysis (EDA), model training with hyperparameter tuning, evaluation, and deployment using **Streamlit**.

🔗 **Live Demo :**  
 https://rainfall-prediction-webapp.streamlit.app/

---

## Problem Statement
Accurate rainfall prediction is crucial for agriculture, water resource management, and disaster preparedness.  
This project aims to predict **next-day rainfall (Yes/No)** using historical weather data and machine learning techniques.

---

## Solution Overview
- Built a **binary classification model** to predict rainfall
- Performed **data cleaning, feature selection, and class balancing**
- Compared models and optimized **Random Forest using GridSearchCV**
- Deployed the trained model as an **interactive Streamlit web application**

---

##  Dataset Description
The dataset contains historical weather observations with the following features:

- Pressure  
- Dew Point  
- Humidity  
- Cloud Cover  
- Sunshine  
- Wind Direction  
- Wind Speed  
- Target Variable: `rainfall` (Yes / No)

---

##  Tech Stack
- **Programming Language:** Python  
- **Libraries:**  
  - NumPy, Pandas  
  - Matplotlib, Seaborn  
  - Scikit-learn  
- **Model:** Random Forest Classifier  
- **Deployment:** Streamlit  
- **Model Serialization:** Pickle  

---

## 1. Exploratory Data Analysis (EDA)
- Distribution analysis using histograms
- Outlier detection using boxplots
- Correlation analysis using heatmaps
- Class distribution visualization

### EDA helped identify:
- Highly correlated temperature features
- Class imbalance in rainfall data

---

## 2. Data Preprocessing
- Removed unnecessary and highly correlated features
- Handled missing values using:
  - Mode (categorical)
  - Median (numerical)
- Encoded target variable (`yes → 1`, `no → 0`)
- Addressed class imbalance using **downsampling**
- Shuffled and split data into train and test sets

---

## 3. Model Training
- Algorithm: **Random Forest Classifier**
- Hyperparameter tuning using **GridSearchCV**
- 5-fold Cross Validation for robust performance

**Hyperparameters Tuned:**
- Number of trees (`n_estimators`)
- Tree depth (`max_depth`)
- Feature selection strategy (`max_features`)
- Minimum samples for splits and leaves

---

## 4.Model Evaluation
- Cross-validation score
- Accuracy
- Confusion Matrix
- Precision, Recall, F1-score

The model demonstrates strong generalization on unseen data.

---

## Deployment 
The trained model is deployed using **Streamlit**, allowing users to:
- Input real-time weather parameters
- Get rainfall predictions instantly
- View results in an interactive UI

---

##  Model Persistence
- The trained model and feature names are saved using **Pickle**
- Enables easy reuse for deployment and future predictions

---

## Future Enhancements
- Apply **SMOTE** for advanced class balancing  
- Use **PCA** for dimensionality reduction  
- Compare with simpler models like **Logistic Regression** (with scaling)  
- Implement **model selection pipeline**
- Add **SHAP explainability**
- Dockerize the application for production readiness  

---

##  How to Run Locally
```bash
git clone https://github.com/your-username/rainfall-prediction-ml.git
cd rainfall-prediction-ml
pip install -r requirements.txt
streamlit run app.py
