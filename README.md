# 🍷 Wine Clustering Web App using KMeans & PCA

This is a beginner-friendly machine learning project that uses **KMeans clustering** to group wines based on their chemical properties. The project is deployed as an interactive **Streamlit web app** where users can input wine data and get a predicted cluster label.

---

## 🔍 Features

- Predicts which cluster a wine belongs to based on input features
- Built using **Unsupervised Machine Learning (KMeans + PCA)**
- Trained using the Wine dataset (13 numerical features)
- Simple and interactive Streamlit UI

---

## 📁 Project Structure

wine-clustering-app/
├── app.py # Streamlit app
├── scaler.pkl # Trained StandardScaler
├── pca.pkl # Trained PCA model (2D)
├── kmeans.pkl # Trained KMeans model
├── wine-clustering.csv # Dataset used for training
├── requirements.txt # Python dependencies
└── README.md # Project overview

yaml
Copy
Edit

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/wine-clustering-app.git
cd wine-clustering-app
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Streamlit app
bash
Copy
Edit
streamlit run app.py
🧪 Features Used for Clustering
The app uses the following 13 features from the Wine dataset:

Alcohol

Malic acid

Ash

Alcalinity of ash

Magnesium

Total phenols

Flavanoids

Nonflavanoid phenols

Proanthocyanins

Color intensity

Hue

OD280/OD315 of diluted wines

Proline

🧠 ML Workflow Overview
Model was trained using a standard machine learning pipeline:

Data Preprocessing

Handled missing values

Scaled features with StandardScaler

PCA

Reduced dimensions to 2D for clustering & visualization

KMeans Clustering

Optimal clusters determined using Elbow Method

Final model trained and saved with pickle

🌐 Deployment on Streamlit Cloud
Push this project to a GitHub repository

Go to https://streamlit.io/cloud

Click “Deploy an app” and connect your repo

Set the entry point as app.py

📃 Requirements
All dependencies are listed in requirements.txt:

txt
Copy
Edit
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
plotly
Install with:

bash
Copy
Edit
pip install -r requirements.txt
🙋‍♂️ Author
Lapsang Lama
