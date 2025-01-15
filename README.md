# Airlines-Analysis

Airlines Passenger Satisfaction Prediction Application
This Streamlit-based web application predicts airline passenger satisfaction using a trained machine learning model. It allows users to input their travel details, which the application processes using the loaded model to provide real-time satisfaction predictions.

Features
Interactive Input Options: Customize your travel details using select boxes and sliders for gender, type of travel, class, and various service ratings.
Real-time Predictions: Immediately receive a satisfaction prediction upon input submission.
Visualization of Input Data: View your input data as you adjust the controls.
Prerequisites
Tools Required
Python (3.8 or higher recommended)
pip for installing dependencies
Virtual environment tools (venv or conda)
Installation Guide
Step 1: Clone the Repository
bash
Copy code
git clone <repository_url>
cd <repository_name>
Step 2: Create a Virtual Environment
For Unix/MacOS

bash
Copy code
python3 -m venv venv
source venv/bin/activate
For Windows

bash
Copy code
python -m venv venv
venv\Scripts\Activate
Step 3: Install Dependencies
Install all required dependencies listed in requirements.txt.

bash
Copy code
pip install -r requirements.txt
Running the Application
To start the Streamlit application, execute:

bash
Copy code
streamlit run app.py
This will launch the application in your default web browser. If it doesn’t open automatically, navigate to the URL shown in the terminal (usually http://localhost:8501).

Usage Instructions
Input Details: Use the interactive options to fill in your travel details.
Submit for Prediction: Click the 'Predict' button to submit your details and view the prediction.
View Prediction: The satisfaction level ('Satisfied' or 'Not Satisfied') will be displayed based on your input.
Requirements
Python Packages (from requirements.txt):
streamlit
pandas
pickle5
scikit-learn (if the model training process is included in the notebook)
