# 🩺 Diabetes Prediction Using Machine Learning

This project predicts whether a person is diabetic or not using Machine Learning and the Support Vector Machine (SVM) algorithm.

## 📌 Project Description

The model analyzes patient health parameters and predicts the likelihood of diabetes.

The prediction is based on:

- Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin Level
- BMI
- Diabetes Pedigree Function
- Age

## 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Scikit-Learn

## 🤖 Machine Learning Algorithm

- Support Vector Machine (SVM)
- Linear Kernel

## 📂 Dataset

The project uses the Pima Indians Diabetes Dataset.

Target Variable:

```text
Outcome
```

- 0 = Non-Diabetic
- 1 = Diabetic

## 🚀 Features

- Data preprocessing
- Feature scaling using StandardScaler
- Train-Test Split
- SVM Classification
- Accuracy Evaluation
- Interactive User Input Prediction

## 📁 Project Structure

```text
Diabetes-Prediction/
│
├── diabetes.csv
├── diab.py
├── README.md
└── requirements.txt
```

## 📦 Installation

```bash
pip install numpy pandas scikit-learn
```

## ▶️ Run Project

```bash
python diab.py
```

## 📊 Output

The program:

1. Trains an SVM model
2. Displays training accuracy
3. Displays testing accuracy
4. Takes user input
5. Predicts whether the person is diabetic or not

## Example Output

```text
Prediction Result:
Person is NOT Diabetic
```

or

```text
Prediction Result:
Person is Diabetic
```

## 🔮 Future Improvements

- GUI Interface
- Streamlit Deployment
- Flask API
- Model Saving with Pickle
- Web-based Prediction System

## 👨‍💻 Author

Machine Learning Project for Diabetes Risk Prediction.

## ⭐ Star this Repository

If you found this project useful, please give it a star.
