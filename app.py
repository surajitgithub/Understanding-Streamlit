import streamlit as st
import pickle
import matplotlib.pyplot as plt
 
with open('finalized_model_surajit.pickle','rb') as temp:
    model = pickle.load(temp)

st.title('BP Monitoring Application')
pulse_rate = st.number_input('Person Pulse Rate: ')
predict  = model.predict([[pulse_rate]])

button = st.button('Prediction',key=1)

if button==True:
    st.write(predict)