from pickle import load
import streamlit as st

model = load(open("../models/logistic_rg.sav", "rb"))
class_dict = {
    "0": "No sobreviviente",
    "1": "Sobreviviente"
}

st.title("Titanic - Model prediction")

val1 = st.selectbox("Pclass	", [1.0,2.0 ,3.0])
val2 = st.slider("Fare", min_value = 0.0, max_value = 513.0, step = 50.0)
val3 = st.selectbox("Sex", [0.0,1.0])
val4 = st.selectbox("Embarked", [-1.0,0.0,1.0,2.0])
val5 = st.slider("FamMembers", min_value = 0.0, max_value = 10.0, step = 1.0)


if st.button("Predict"):
    prediction = str(model.predict([[val1, val2, val3, val4,val5]])[0])
    pred_class = class_dict[prediction]
    st.write("Prediction:", pred_class)