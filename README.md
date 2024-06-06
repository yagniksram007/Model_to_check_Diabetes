For the input:
input_data = (5,166,72,19,175,25.8,0.587,51)

Explanation:

1. Data Loading and Preprocessing:
=> The diabetes data is loaded and standardized using StandardScaler.
=> The data is split into training and testing sets.

2. Model Training:
The SVM model is trained using the training set.

3. Tkinter GUI Setup:
=> A main window is created with Tkinter.
=> Labels and entry fields are set up for user input (one for each feature).
=> A "Predict" button is added that triggers the make_prediction function.
=> Prediction Function (make_prediction):

The function retrieves input from the user, converts it to the appropriate format, and standardizes it.
It then uses the trained SVM model to predict whether the person is diabetic or not.
The result is displayed using a message box.

Output:
![Screenshot (520)](https://github.com/yagniksram007/Model_to_check_Diabetes/assets/112811032/1df4bf74-0976-48b3-9d67-f9d30eebc6af)
