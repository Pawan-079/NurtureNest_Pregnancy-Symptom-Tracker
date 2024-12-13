# NurtureNest_Pregnancy-Symptom-Tracker
Empathetic Pregnancy Symptom Tracker

# Pregnancy Symptom Tracker

## Overview
The **Pregnancy Symptom Tracker** is an intuitive and user-friendly application designed to help expecting individuals track and monitor their symptoms throughout pregnancy. This tool is powered by machine learning, offering personalized insights and predictions based on recorded data. It enables better understanding of symptoms, their patterns, and significant changes, facilitating effective communication with healthcare providers.

## Key Features
- **Daily Symptom Logging**: Users can log various pregnancy symptoms daily.
- **Machine Learning Predictions**: Provides insights and predictions on potential health trends based on logged data.
- **Progress Overview**: Visual representation of symptom trends over time.
- **Customizable Symptom List**: Add or remove symptoms to personalize tracking.
- **Reminders and Alerts**: Set reminders to record daily symptoms and receive alerts for significant changes.
- **Data Export**: Export data for personal use or to share with healthcare providers.

## Technologies Used
- **Machine Learning**: Model trained using Python and integrated via Flask to provide predictions.
- **Backend**: Flask for server-side operations and RESTful API integration.
- **Database**: MongoDB for secure and scalable data storage.
- **Frontend**: React.js for the interactive user interface.
- **Authentication**: JSON Web Tokens (JWT) for secure user login.
- **Styling**: CSS and Material-UI for an attractive and responsive design.

## Installation and Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/pregnancy-symptom-tracker.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd pregnancy-symptom-tracker
   ```
3. **Install dependencies**:
   - **Backend** (Flask):
     ```bash
     cd server  # Navigate to the backend directory
     pip install -r requirements.txt
     ```
   - **Frontend** (React):
     ```bash
     cd ../client  # Navigate to the frontend directory
     npm install
     ```
4. **Create a `.env` file** in the `server` directory with the following variables:
   ```env
   MONGO_URI=your-mongodb-connection-string
   JWT_SECRET=your-secret-key
   ```
5. **Start the application**:
   ```bash
   # Start the backend
   cd server
   flask run

   # Start the frontend
   cd ../client
   npm start
   ```
6. **Access the application** at `http://localhost:3000` (frontend).

## Usage Guide
1. **Sign Up / Log In**: Create an account or log in to start tracking.
2. **Log Symptoms**: Navigate to the symptom logging page and record your daily symptoms.
3. **View Predictions**: Access the machine learning predictions for personalized insights.
4. **View Progress**: Access the dashboard to see charts and trends of your recorded data.
5. **Export Data**: Use the export feature to download your data as a CSV file.

## Contributing
We welcome contributions to improve the Pregnancy Symptom Tracker. If you’d like to contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Create a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For questions or support, please reach out to [your email or contact details].


