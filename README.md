# 🌱 Farmland Suitability Prediction  

This project predicts **agricultural land suitability** using **Machine Learning**. The model takes into account three key environmental factors:  

- 🌧️ **Average Rainfall (mm/month)**  
- 🌡️ **Average Temperature (°C)**  
- 🌱 **Soil Fertility Index**  

It classifies land as either:  
- **1 → Suitable** ✅  
- **0 → Not Suitable** ❌  

The project also includes a **Streamlit chatbot UI** that allows users (farmers, agronomists, or researchers) to interact with the model in a simple, conversational way.  

---

## 📊 Dataset & Preprocessing  

- A **synthetic dataset** was generated to simulate realistic environmental ranges.  
- Labels were assigned using agronomic rules (rainfall, temperature, fertility thresholds).  
- To handle class imbalance, **SMOTE (Synthetic Minority Oversampling Technique)** was applied.  

**Class Balance Before SMOTE:**  
0 → 391
1 → 109

**Class Balance After SMOTE:**  
0 → 391
1 → 391


---

## 🤖 Model Training  

- Algorithm: **Random Forest Classifier**  
- Libraries: `scikit-learn`, `imbalanced-learn`  
- Evaluation Metrics: Precision, Recall, F1-score  

**Performance Results:**  
- Accuracy: ~80%  
- Balanced precision & recall across both classes  

---

## 💻 Streamlit Chatbot UI  

I built a **Streamlit app** that allows users to:  
1. Input rainfall, temperature, and fertility index values.  
2. Receive a prediction on land suitability.  
3. Interact with the model in a chatbot-like interface.  

![Chatbot UI](./screenshots/Screenshot%202025-10-04%20200758.png)
![Chatbot UI](./screenshots/Screenshot%202025-10-04%20200858.png)
![Chatbot UI](./screenshots/Screenshot%202025-10-04%20200925.png)

---

## 🚀 Deployment  

- The app is deployed on **Streamlit Cloud** for easy access.  
- Code and resources are version-controlled via **GitHub**.  

👉 [https://hackstuff.streamlit.app/]  
👉 [https://github.com/Lukembogo-dot/Hackstuff_Project.git]  

---

## 🛠️ Tech Stack  

- **Python** (NumPy, Pandas, scikit-learn, imbalanced-learn)  
- **Streamlit** (for UI)  
- **Joblib** (for model persistence)  
- **GitHub + Streamlit Cloud** (for deployment)  

---

## 🌍 Impact  

This project highlights how **AI can contribute to sustainable agriculture and food security** by helping farmers make informed decisions about land use.  

---

## 📌 How to Run Locally  

1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/Hackstuff_Project.git
   cd Hackstuff_Project

2. Install dependencies
  ```bash
    pip install -r requirements.txt
```
3. Run the Streamlit app
  ```bash
streamlit run app.py
```
