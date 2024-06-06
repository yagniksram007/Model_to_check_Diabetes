import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm

# Load the data from the CSV file into a pandas dataframe
diabetes_data = pd.read_csv('D:/My Files/Engineering/6th Sem/Machine Learning Lab/Dataset/diabetes.csv')

# Separate the features and target
features = diabetes_data.drop(columns='Outcome', axis=1)
target = diabetes_data['Outcome']

# Data Standardization
scaler = StandardScaler()
scaler.fit(features)
standardized_data = scaler.transform(features)

# Preprocess the data
X_train, X_test, Y_train, Y_test = train_test_split(standardized_data, target, test_size=0.2, random_state=42)

# Train the SVM model
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

# Tkinter GUI
def make_prediction():
    try:
        # Gather input data from the user
        input_data = [
            float(entry_pregnancies.get()),
            float(entry_glucose.get()),
            float(entry_blood_pressure.get()),
            float(entry_skin_thickness.get()),
            float(entry_insulin.get()),
            float(entry_bmi.get()),
            float(entry_dpf.get()),
            float(entry_age.get())
        ]

        # Convert input data to a numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # Reshape the array for standardization
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

        # Standardize the input data
        std_data = scaler.transform(input_data_reshaped)

        # Make a prediction using the trained SVM model
        prediction = classifier.predict(std_data)

        # Display the result
        if prediction[0] == 0:
            result = 'The person is not diabetic'
        else:
            result = 'The person is diabetic'
        
        messagebox.showinfo('Prediction Result', result)
    
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numeric values for all fields.")

# Create the main window
root = tk.Tk()
root.title('Diabetes Prediction')

# Create and place the input fields and labels
labels = ['Pregnancies', 'Glucose', 'Blood Pressure', 'Skin Thickness', 'Insulin', 'BMI', 'Diabetes Pedigree Function', 'Age']
entries = []

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

entry_pregnancies, entry_glucose, entry_blood_pressure, entry_skin_thickness, entry_insulin, entry_bmi, entry_dpf, entry_age = entries

# Create and place the Predict button
predict_button = tk.Button(root, text='Predict', command=make_prediction)
predict_button.grid(row=len(labels), column=0, columnspan=2, pady=20)

# Start the Tkinter event loop
root.mainloop()
