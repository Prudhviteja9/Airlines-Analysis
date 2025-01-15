import streamlit as st
import pandas as pd
import pickle

# Load the model
@st.cache
def load_model():
    with open('Airlines_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

# User inputs for prediction
def user_input_features():
    gender_option = st.selectbox('Gender', options=['Male', 'Female'])
    gender = 0 if gender_option == 'Male' else 1
    type_of_travel_option = st.selectbox('Type of Travel', options=['Personal Travel', 'Business Travel'])
    type_of_travel = 0 if type_of_travel_option == 'Personal Travel' else 1
    class_option = st.selectbox('Class', options=['Eco', 'Eco Plus', 'Business'])
    class_encoded = {'Eco': 0, 'Eco Plus': 1, 'Business': 2}[class_option]
    flight_distance = st.number_input('Flight Distance', min_value=0, max_value=10000, value=500)
    age = st.slider('Age', 18, 100, 30)
    inflight_wifi_service = st.slider('Inflight wifi service', 0, 5, 3)
    departure_arrival_time_convenient = st.slider('Departure/Arrival time convenient', 0, 5, 3)
    ease_of_online_booking = st.slider('Ease of Online booking', 0, 5, 3)
    gate_location = st.slider('Gate location', 0, 5, 3)
    food_and_drink = st.slider('Food and drink', 0, 5, 3)
    online_boarding = st.slider('Online boarding', 0, 5, 3)
    seat_comfort = st.slider('Seat comfort', 0, 5, 3)
    inflight_entertainment = st.slider('Inflight entertainment', 0, 5, 3)
    on_board_service = st.slider('On-board service', 0, 5, 3)
    leg_room_service = st.slider('Leg room service', 0, 5, 3)
    baggage_handling = st.slider('Baggage handling', 0, 5, 3)
    checkin_service = st.slider('Checkin service', 0, 5, 3)
    inflight_service = st.slider('Inflight service', 0, 5, 3)
    cleanliness = st.slider('Cleanliness', 0, 5, 3)
    departure_delay = st.number_input('Departure Delay in Minutes', min_value=0, max_value=1200, value=0)
    arrival_delay = st.number_input('Arrival Delay in Minutes', min_value=0, max_value=1200, value=0)

    data = {
        'Gender': gender,
        'Age': age,
        'Type of Travel': type_of_travel,
        'Class': class_encoded,
        'Flight Distance': flight_distance,
        'Inflight wifi service': inflight_wifi_service,
        'Departure/Arrival time convenient': departure_arrival_time_convenient,
        'Ease of Online booking': ease_of_online_booking,
        'Gate location': gate_location,
        'Food and drink': food_and_drink,
        'Online boarding': online_boarding,
        'Seat comfort': seat_comfort,
        'Inflight entertainment': inflight_entertainment,
        'On-board service': on_board_service,
        'Leg room service': leg_room_service,
        'Baggage handling': baggage_handling,
        'Checkin service': checkin_service,
        'Inflight service': inflight_service,
        'Cleanliness': cleanliness,
        'Departure Delay in Minutes': departure_delay,
        'Arrival Delay in Minutes': arrival_delay
    }

    features = pd.DataFrame(data, index=[0])
    return features


st.write("# Airline Passenger Satisfaction Prediction")

# User inputs
input_df = user_input_features()

# Predict button
if st.button('Predict'):
    prediction = model.predict(input_df)
    st.write('Satisfaction Prediction:', 'Satisfied' if prediction[0] == 1 else 'Not Satisfied')

