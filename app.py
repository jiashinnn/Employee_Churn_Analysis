from flask import Flask, render_template, request
import numpy as np
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')  
X_test = joblib.load('X_test.pkl')
y_test = joblib.load('y_test.pkl')

# Target encoding for department names
department_encoding = {
    "IT": 1,
    "RandD": 2,
    "Accounting": 3,
    "HR": 4,
    "Management": 5,
    "Marketing": 6,
    "Product Management": 7,
    "Sales": 8,
    "Support": 9,
    "Technical": 10
}

# Define the home route
@app.route('/')
def home():
    return render_template('index.html', form_data=None, prediction=None)

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if 'reset' in request.form:  # Check if the reset button was clicked
        return render_template('index.html', form_data=None, prediction=None)

    # Retrieve form inputs
    staf_name = request.form['staf_name']
    satisfaction_level = float(request.form['satisfaction_level'])
    last_evaluation = float(request.form['last_evaluation'])
    number_project = int(request.form['number_project'])
    average_monthly_hours = int(request.form['average_monthly_hours'])
    time_spent = int(request.form['time_spent'])
    work_accident = int(request.form['work_accident'])
    promotion_last_5years = int(request.form['promotion_last_5years'])
    department = request.form['department']
    salary = int(request.form['salary'])

    # Transform department to numeric using target encoding
    department_numeric = department_encoding.get(department, 0)

    # Prepare input data for scaling
    continuous_data = np.array([
        satisfaction_level, last_evaluation, average_monthly_hours
    ]).reshape(1, -1)

    # Scale continuous data using the loaded scaler
    scaled_continuous_data = scaler.transform(continuous_data)

    # Combine scaled continuous data with other features
    data = np.hstack((
        scaled_continuous_data,
        np.array([number_project, time_spent, work_accident, promotion_last_5years, department_numeric, salary]).reshape(1, -1)
    ))

    # Make prediction
    prediction = model.predict(data)[0]
    result = (
        f"Sorry, {staf_name} tends to leave the company."
        if prediction == 1
        else f"Good news! Most likely {staf_name} will stay."
    )

    # Get model details (accuracy, iterations, loss)
    accuracy = round(model.score(X_test, y_test) * 100, 3)
    lowest_error = round(model.best_loss_, 3)
    iterations = model.n_iter_

    # Render result to the HTML
    return render_template(
        'index.html',
        prediction=result,
        accuracy=accuracy,
        iterations=iterations,
        lowest_error=lowest_error,
        form_data={
            'staf_name': staf_name,
            'satisfaction_level': satisfaction_level,
            'last_evaluation': last_evaluation,
            'number_project': number_project,
            'average_monthly_hours': average_monthly_hours,
            'time_spent': time_spent,
            'work_accident': work_accident,
            'promotion_last_5years': promotion_last_5years,
            'department': department,
            'salary': salary
        }
    )


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
