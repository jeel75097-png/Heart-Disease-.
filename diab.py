import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

diabetes_dataset = pd.read_csv("diabetes.csv")

print("\nFirst 5 Rows:")
print(diabetes_dataset.head())

print("\nDataset Shape:")
print(diabetes_dataset.shape)

print("\nOutcome Count:")
print(diabetes_dataset['Outcome'].value_counts())

X = diabetes_dataset.drop(columns='Outcome')
Y = diabetes_dataset['Outcome']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(
    X_scaled,
    Y,
    test_size=0.2,
    random_state=2,
    stratify=Y
)

classifier = SVC(kernel='linear')
classifier.fit(X_train, Y_train)

train_prediction = classifier.predict(X_train)
train_accuracy = accuracy_score(Y_train, train_prediction)

test_prediction = classifier.predict(X_test)
test_accuracy = accuracy_score(Y_test, test_prediction)

print("\nTraining Accuracy:", train_accuracy)
print("Testing Accuracy:", test_accuracy)

while True:

    print("\n===== Diabetes Prediction =====")

    pregnancies = float(input("Enter Pregnancies: "))
    glucose = float(input("Enter Glucose Level: "))
    bloodpressure = float(input("Enter Blood Pressure: "))
    skinthickness = float(input("Enter Skin Thickness: "))
    insulin = float(input("Enter Insulin Level: "))
    bmi = float(input("Enter BMI: "))
    dpf = float(input("Enter Diabetes Pedigree Function: "))
    age = float(input("Enter Age: "))

    input_data = (
        pregnancies,
        glucose,
        bloodpressure,
        skinthickness,
        insulin,
        bmi,
        dpf,
        age
    )

    input_df = pd.DataFrame([input_data], columns=X.columns)

    input_scaled = scaler.transform(input_df)

    prediction = classifier.predict(input_scaled)

    print("\nPrediction Result:")

    if prediction[0] == 0:
        print("Person is NOT Diabetic")
    else:
        print("Person is Diabetic")

    again = input("\nCheck another person? (yes/no): ")

    if again.lower() != "yes":
        print("Program Ended.")
        break