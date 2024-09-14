from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the trained model and encoders
model_filename = 'trained_model.pkl'
try:
    with open(model_filename, 'rb') as file:
        model = pickle.load(file)
    print(f"Model loaded from {model_filename}")
except Exception as e:
    print(f"Error loading the model: {e}")

# Load LabelEncoders
try:
    le_trimester = pickle.load(open('le_trimester.pkl', 'rb'))
    le_symptom = pickle.load(open('le_symptom.pkl', 'rb'))
    le_severity = pickle.load(open('le_severity.pkl', 'rb'))
    le_frequency = pickle.load(open('le_frequency.pkl', 'rb'))
    le_follow_up = pickle.load(open('le_follow_up.pkl', 'rb'))
    print("LabelEncoders loaded successfully.")
except Exception as e:
    print(f"Error loading LabelEncoders: {e}")

# Function to preprocess input data
def preprocess_data(data):
    try:
        data['Trimester'] = le_trimester.transform([data['Trimester']])[0]
        data['Symptom'] = le_symptom.transform([data['Symptom']])[0]
        data['Severity'] = le_severity.transform([data['Severity']])[0]
        data['Frequency'] = le_frequency.transform([data['Frequency']])[0]
        data['Duration'] = convert_duration(data['Duration'])
        
        return pd.DataFrame([data])
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        return pd.DataFrame()

def convert_duration(duration):
    try:
        if 'hour' in duration:
            return float(duration.split()[0])
        elif 'day' in duration:
            return float(duration.split()[0]) * 24  # Assuming a day equals 24 hours
        else:
            return 0
    except Exception as e:
        print(f"Error converting duration: {e}")
        return 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get form data
            data = {
                'Date': request.form['Date'],
                'Trimester': request.form['Trimester'],
                'Symptom': request.form['Symptom'],
                'Severity': request.form['Severity'],
                'Duration': request.form['Duration'],
                'Frequency': request.form['Frequency'],
                'Additional Notes': request.form['Additional Notes'],
                'Recommended Action': request.form['Recommended Action'],
                'Medical Advice': request.form['Medical Advice'],
                'Follow-Up': request.form['Follow-Up']
            }

            # Check Medical Advice and determine health status
            
            if data['Medical Advice'] == 'Yes':
                prediction = 'bad health'
            
            
            else:
                prediction = 'good health'
            
                
            return render_template('result.htm', prediction=prediction)
        except Exception as e:
            print(f"Error in prediction: {e}")
            return render_template('result.htm', prediction="Error in prediction")
    
    return render_template('index.htm')

if __name__ == '__main__':
    app.run(debug=True)
