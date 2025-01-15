# Airlines-Analysis

Overview
This project is designed to predict airline passenger satisfaction using machine learning techniques. The analysis is performed using a Jupyter notebook, and the prediction model is deployed as a web application using Streamlit. The main goal is to provide insights into factors influencing passenger satisfaction and to deploy a model that allows real-time prediction based on user input.

Project Structure
Analysis (Jupyter Notebook)
The Jupyter notebook contains the exploratory data analysis (EDA) and model building process. It includes data cleaning, feature engineering, and a detailed analysis to understand the impact of various factors on passenger satisfaction. Different machine learning models are trained and evaluated to find the best performer.

Prediction Application (app.py)
The Python file app.py uses Streamlit to create an interactive web application where users can input their travel details to predict satisfaction levels. The model used for predictions is loaded from a serialized file (Airlines_model.pkl).

Key Features of the App
Selection options for gender, type of travel, and class.
Sliders to specify age, flight distance, and ratings for various services like wifi, food, and boarding.
Real-time prediction of passenger satisfaction based on the input provided.
How to Run the Application
Clone the repository to your local machine.
Ensure you have Python and Streamlit installed.
Navigate to the directory containing app.py.
Run the command streamlit run app.py in your terminal.
The application will open in your web browser where you can start interacting with it.
