from pickle import load
import streamlit as st

model = load(open("/workspaces/ML-web-app-using-Streamlit/models/random_forest_classifier_default_42.sav", "rb"))

class_dict={
    "0": "Negative in diabetes",
    "1": "Positive in diabetes",
    }

st.title("Predicting Diabetes")

val1 = st.slider("Pregnancies", min_value = 0.0, max_value = 54.0, step = 0.1)
val2 = st.slider("Glucose", min_value = 0.0, max_value = 554.0, step = 0.1)
val3 = st.slider("BloodPressure", min_value = 0.0, max_value = 200.0, step = 0.1)
val4 = st.slider("SkinThickness", min_value = 0.0, max_value = 94.0, step = 0.1)
val5 = st.slider("Insulin", min_value = 0.0, max_value = 904.0, step = 0.1)
val6 = st.slider("BMI", min_value = 0.0, max_value = 294.0, step = 0.1)
val7 = st.slider("DiabetesPedigreeFunction", min_value = 0.0, max_value = 94.0, step = 0.1)


if st.button("Predict"):
    prediction = str(model.predict([[val1, val2, val3, val4, val5, val6, val7]])[0])
    pred_class = class_dict[prediction]
    st.write("Prediction:", pred_class)    