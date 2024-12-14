# Employee Churn Prediction

This project predicts whether an employee will stay or leave the company using a neural network-based machine learning model. The model is trained on employee-related data and optimized through hyperparameter tuning and feature selection for high accuracy.

## Features
- **Prediction**: Uses a trained neural network to predict if an employee is likely to leave or stay at the company.
- **Input Form**: Collects employee details such as satisfaction level, last evaluation score, average monthly hours, etc.
- **Result Display**: Shows the prediction result along with model performance metrics (accuracy, iterations, and error).

## Machine Learning Model
- **Neural Network**: The prediction model is a **Multilayer Perceptron (MLP)**, a type of neural network well-suited for classification tasks. It consists of:
  - **Input Layer**: Takes features such as satisfaction level, last evaluation, and other employee data.
  - **Hidden Layers**: Processes the input features to learn complex patterns.
  - **Output Layer**: Outputs the prediction, indicating whether the employee is likely to stay or leave.


- **Hyperparameter Tuning**: The MLP model was optimized using hyperparameter tuning techniques. Parameters like the number of hidden layers, learning rate, and activation functions were adjusted to achieve the best results.

## How It Works
1. The user fills in employee details through the web form.
2. The Flask backend processes the inputs and scales the continuous features using a pre-trained scaler.
3. The optimized MLP model evaluates the inputs and predicts whether the employee is likely to stay or leave.
4. The prediction result, along with accuracy, error, and iterations, is displayed on the web interface.

## Files Included
- **`app.py`**: Backend Flask application to handle predictions and serve the web application.
- **`index.html`**: Frontend HTML file for the user interface.
- **`employeechurn.ipynb`**: Jupyter Notebook for data preprocessing, feature selection, model training, and hyperparameter tuning.
- **`HR_comma_sep.csv`**: Dataset used for training and testing the model.

## Dataset and Features
The dataset contains the following features:
- **Satisfaction Level**: Employee satisfaction level (0–1).
- **Last Evaluation**: Last performance evaluation score (0–1).
- **Average Monthly Hours**: Average number of hours worked per month.
- **Number of Projects**: Number of projects assigned to the employee.
- **Time Spent**: Number of years spent at the company.
- **Work Accident**: Whether the employee had a work accident (0 or 1).
- **Promotion in Last 5 Years**: Whether the employee got a promotion in the last 5 years (0 or 1).
- **Department**: Employee’s department (e.g., IT, HR, Marketing).
- **Salary**: Salary level (1 = Low, 2 = Medium, 3 = High).

## Model Performance
- **Accuracy**: Achieved high accuracy after hyperparameter tuning.
- **Iterations**: The number of iterations required to converge to the optimal solution.
- **Error**: The lowest error observed during model training.

## Working Application
  ![image](https://github.com/user-attachments/assets/e7de35a3-71f6-4460-ae6d-35c2968a38dd)


## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)

## Acknowledgements
- The dataset used in this project is publicly available and suitable for churn prediction studies.
- Special thanks to open-source contributors for tools and libraries used in this project.
