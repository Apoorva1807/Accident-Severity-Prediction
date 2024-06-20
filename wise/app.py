import streamlit as st
import pandas as pd
import joblib
import base64


loaded_model = joblib.load('C:/Users/Apoor/OneDrive/Desktop/wise/trained_model1.pkl')


st.title("Air Crash Severity")
st.header("Enter the following details to predict the severity")


Days_Since_Inspection = st.text_input("Days Since Inspection (1-23): ", 1, 23)
Adverse_Weather_Metric = st.slider("Adverse Weather Metric (0-2.37): ", 0.0, 2.37)
Total_Safety_Complaints = st.text_input("Total Safety Complaints (0-54): ", 0, 54)
Turbulence_In_gforces = st.slider("Turbulence In g-forces (0.13-0.88): ", 0.13, 0.88)
Accident_Type_Code = st.selectbox("Accident Type Code:", [1, 2, 3, 4, 5, 6, 7])
Safety_Score = st.text_input("Safety Score (0-100): ", 0, 100)
Cabin_Temperature = st.slider("Cabin Temperature (74.7-97.5): ", 74.7, 97.5)
Violations = st.selectbox("Number of Violations (0-5): ",[0,1,2,3,4,5])
Max_Elevation = st.slider("Max Elevation (832-64.3k): ", 832.0, 64300.0)
Control_Metric = st.text_input("Control Metric (0-100): ", 0, 100)


if st.button("Prdict Severity"):
    user_input = pd.DataFrame({
        'Days_Since_Inspection': [Days_Since_Inspection],
        'Adverse_Weather_Metric': [Adverse_Weather_Metric],
        'Total_Safety_Complaints': [Total_Safety_Complaints],
        'Turbulence_In_gforces': [Turbulence_In_gforces],
        'Accident_Type_Code': [Accident_Type_Code],
        'Safety_Score': [Safety_Score],
        'Cabin_Temperature': [Cabin_Temperature],
        'Violations': [Violations],
        'Max_Elevation': [Max_Elevation],
        'Control_Metric': [Control_Metric],
    })
    
    
    input_data = user_input.values.reshape(1, -1)
    
    
    predicted_severity = loaded_model.predict(input_data)

    
    severity_mapping = {0: 'Minor Damage', 1: 'Significant Damage', 2: 'Major Damage', 3: 'Highly Significant Damage '}
    predicted_severity = severity_mapping[predicted_severity[0]]

   
    st.write(f"Predicted Severity: {predicted_severity}")


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local('pl.jpg')