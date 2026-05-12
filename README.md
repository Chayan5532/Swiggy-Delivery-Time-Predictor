# 🛵 Swiggy Delivery Time Prediction

A Machine Learning project to predict food delivery time using real-world Swiggy data. Built using Python, Scikit-learn, and XGBoost with a complete preprocessing pipeline.

---

## 📌 Project Overview

Predicting accurate delivery time is critical for platforms like Swiggy. This project uses historical delivery data to build a regression model that estimates delivery time in minutes based on factors like distance, traffic, weather, and rider ratings.

---

## 📊 Dataset

| Property | Details |
|---|---|
| **Rows** | 45,502 |
| **Columns** | 26 |
| **Target Variable** | `time_taken` (minutes) |
| **Source** | Swiggy Demographic Dataset |

### Key Features Used
- `distance` — delivery distance in km
- `traffic` — traffic level (low / medium / high / jam)
- `weather` — weather conditions (sunny, cloudy, stormy, etc.)
- `ratings` — rider rating
- `pickup_time_minutes` — time taken to pick up order
- `multiple_deliveries` — number of simultaneous deliveries
- `festival` — whether it's a festival day
- `city_type` — urban / semi-urban / metropolitan

---

## 🔧 Tech Stack

- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost
- **Tools:** Jupyter Notebook, Pickle

---

## 🏗️ Project Structure

```
Swiggy-Delivery-Time-Prediction/
│
├── swiggy_demographic.csv        # Dataset
├── Swiggy Delivery Time Prediction.ipynb  # Main notebook
├── Swiggy_PPT_final.pptx            
├── README.md                     # Project documentation
```

---

## ⚙️ ML Pipeline

### Step 1 — Data Preprocessing
- Dropped irrelevant columns: `rider_id`, `order_date`, `lat/long` coordinates
- Handled missing values using `SimpleImputer`

### Step 2 — Feature Engineering
- Extracted `order_day`, `order_month`, `order_day_of_week`, `is_weekend` from date
- Extracted `order_time_hour`, `order_time_of_day` from time
- Calculated `distance` from latitude/longitude coordinates

### Step 3 — Feature Encoding
- **Nominal columns** → One-Hot Encoding (weather, city_type, city_name, etc.)
- **Ordinal columns** → Ordinal Encoding (traffic: low → medium → high → jam)
- **Numerical columns** → StandardScaler + PowerTransformer

### Step 4 — Model Training
Trained and compared 5 models:

| Model | R2 Score | MAE |
|---|---|---|
| Linear Regression | 0.576 | 4.91 |
| Decision Tree | 0.642 | 4.27 |
| SVR | 0.713 | 3.99 |
| Random Forest | 0.809 | 3.25 |
| **XGBoost** ✅ | **0.815** | **3.23** |

### Step 5 — Hyperparameter Tuning
Used `RandomizedSearchCV` with 20 iterations and 5-fold cross validation.

**Best Parameters found:**
```python
n_estimators    = 300
learning_rate   = 0.05
max_depth       = 6
subsample       = 0.8
colsample_bytree = 0.8
```

---

## 📈 Final Model Results

| Metric | Value |
|---|---|
| **R2 Score (Test)** | 0.821 |
| **MAE** | 3.17 minutes |
| **Model Confidence** | 88.01% |
| **Train R2** | 0.873 |
| **Cross-Val R2 (avg)** | 0.810 |

### Prediction Example
```
Input:
  Distance       = 5 km
  Traffic        = High
  Pickup Time    = 15 min
  Rating         = 4.2
  Weather        = Sunny
  Festival       = No

Output:
  Estimated Delivery Time: 31.99 minutes
  Expected Range: 28.82 to 35.16 minutes
```

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/aadeshyogi12/Swiggy-Delivery-Time-Predictor.git

# 2. Install dependencies
pip install -r requirements.txt

# 3. Open the notebook
jupyter notebook Swiggy Delivery Time Prediction.ipynb
```

---

## 📦 Requirements

```
streamlit==1.45.1
scikit-learn==1.8.0
pandas==2.2.3
numpy==2.4.0
xgboost==3.2.0
```

---

## 🔍 Key Findings

- **Distance** and **traffic** are the most influential factors in delivery time
- **XGBoost** outperformed all other models due to its gradient boosting capability
- **RandomizedSearchCV** improved R2 from 0.814 to 0.821
- Train-Test gap of only 5% confirms no serious overfitting

---

## 🔮 Future Improvements

- Try LightGBM and CatBoost for potentially better performance
- Add more domain features like road type and restaurant prep time
- Increase hyperparameter tuning iterations for better optimization
- Retrain model periodically with new data to handle changing delivery patterns

---

## 👨‍💻 Author

**Yogi Aadesh**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/aadeshyogi/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/aadeshyogi12)
