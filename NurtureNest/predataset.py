import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker for generating synthetic data
fake = Faker()

# Generate synthetic data
def generate_data(num_records):
    data = {
        "Date": [fake.date_between(start_date='-9mo', end_date='today') for _ in range(num_records)],
        "Trimester": [np.random.choice(['First', 'Second', 'Third']) for _ in range(num_records)],
        "Symptom": [np.random.choice(['Nausea', 'Fatigue', 'Swelling', 'Headache', 'Dizziness', 'Shortness of Breath', 'Abdominal Pain', 'Mood Swings', 'Breast Tenderness']) for _ in range(num_records)],
        "Severity": [np.random.choice(['Mild', 'Moderate', 'Severe']) for _ in range(num_records)],
        "Duration": [np.random.choice(['1 hour', '2 hours', '3 hours', 'Half day', 'Full day', 'Multiple days']) for _ in range(num_records)],
        "Frequency": [np.random.choice(['Occasional', 'Daily', 'Weekly']) for _ in range(num_records)],
        "Additional Notes": [fake.sentence(nb_words=6) for _ in range(num_records)],
        "Recommended Action": [np.random.choice(['Rest and hydrate', 'Seek medical advice', 'Elevate legs', 'Reduce salt intake', 'Take prescribed medication', 'Practice relaxation techniques']) for _ in range(num_records)],
        "Medical Advice": [np.random.choice(['Yes', 'No']) for _ in range(num_records)],
        "Follow-Up": [np.random.choice(['Schedule an appointment', 'Monitor symptoms', 'No follow-up needed']) for _ in range(num_records)]
    }
    
    return pd.DataFrame(data)

# Number of records
num_records = 100000  # Adjust as needed

# Generate the dataset
df = generate_data(num_records)

# Save to CSV
df.to_csv('pregnancy_symptoms_dataset.csv', index=False)

print("Dataset created and saved as 'pregnancy_symptoms_dataset.csv'")