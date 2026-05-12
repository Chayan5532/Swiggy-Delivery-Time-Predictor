import streamlit as st
import pickle
import pandas as pd

# page config
st.set_page_config(page_title="Swiggy ETA Predictor", page_icon="")

# TOP IMAGE
st.image("banner.png",   use_container_width=True)

# load model
model = pickle.load(open("swiggy_model.pkl", "rb"))

# title
st.title("Swiggy Delivery Time Predictor")
st.write("Predict delivery time using key influencing factors")
st.divider()

st.subheader("Enter Order Details")

# ---------------- INPUTS ----------------
col1, col2 = st.columns(2)

# LEFT SIDE → Order + Rider
with col1:
    st.markdown("#### Order & Rider")

    distance = st.number_input("Distance (km)", 0.1, 30.0, 5.0, step=0.1)
    pickup_time = st.number_input("Pickup Time", 5, 30, 15)
    ratings = st.slider("Rider Rating", 1.0, 5.0, 4.2)
    multiple_deliveries = st.selectbox("Multiple Deliveries", [0,1,2,3])


# RIGHT SIDE → External Factors
with col2:
    st.markdown("#### Delivery Conditions")

    traffic = st.selectbox("Traffic", ["low", "medium", "high", "jam"])
    weather = st.selectbox("Weather", ["sunny","cloudy","fog","stormy","sandstorms"])
    festival = st.selectbox("Festival", ["yes","no"])
    vehicle_condition = st.selectbox("Vehicle Condition", [0,1,2])

st.divider()

# ---------------- PREDICT ----------------
if st.button("Predict Delivery Time"):

    input_df = pd.DataFrame([{
        'distance': distance,
        'traffic': traffic,
        'pickup_time_minutes': pickup_time,
        'ratings': ratings,
        'vehicle_condition': vehicle_condition,
        'multiple_deliveries': multiple_deliveries,
        'weather': weather,
        'festival': festival,

        # default values (required by model)
        'age': 30,
        'city_type': 'urban',
        'city_name': 'INDO',
        'order_time_hour': 20,
        'type_of_order': 'meal',
        'type_of_vehicle': 'bike',
        'order_time_of_day': 'evening',
        'order_day_of_week': 'friday',
        'is_weekend': 0
    }])

    prediction = model.predict(input_df)[0]

    st.subheader("Prediction Result")
    st.success(f"Estimated Delivery Time: {prediction:.2f} minutes")