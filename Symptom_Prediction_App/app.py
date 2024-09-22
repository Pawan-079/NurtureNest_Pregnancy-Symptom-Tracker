from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained model and label encoders
model = pickle.load(open('new_model.pkl', 'rb'))
label_encoders = pickle.load(open('label_encoders.pkl', 'rb'))

app = Flask(__name__)

# Home page with the input form
@app.route('/')
def index():
    return render_template('index.htm')

# Route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input data from form
        trimester = request.form['trimester']
        symptom = request.form['symptom']
        severity = request.form['severity']
        duration = request.form['duration']
        frequency = request.form['frequency']

        # Convert text inputs to encoded numerical values using LabelEncoders
        input_data = np.array([
            label_encoders['Trimester'].transform([trimester])[0],
            label_encoders['Symptom'].transform([symptom])[0],
            label_encoders['Severity'].transform([severity])[0],
            label_encoders['Duration'].transform([duration])[0],
            label_encoders['Frequency'].transform([frequency])[0]
        ]).reshape(1, -1)

        # Make prediction using the model
        prediction = model.predict(input_data)

        # Convert the numerical output back to text
        recommended_action = label_encoders['Recommended Action'].inverse_transform([prediction[0][0]])[0]
        medical_advice = label_encoders['Medical Advice'].inverse_transform([prediction[0][1]])[0]
        follow_up = label_encoders['Follow-Up'].inverse_transform([prediction[0][2]])[0]

        # Return the results
        return render_template('result.htm', 
                               recommended_action=recommended_action, 
                               medical_advice=medical_advice, 
                               follow_up=follow_up)

if __name__ == '__main__':
    app.run(debug=True)
