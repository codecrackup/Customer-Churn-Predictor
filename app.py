import streamlit as st
import pandas as pd
import joblib



pipe= joblib.load('model_pipeline.pkl')

st.title("Telco Customer Churn Predictor")
st.write("")


st.markdown("#### Customer Information:")


# Customer Info Block
col1,col2= st.columns([1,1])

with col1:
    gender= st.selectbox('Gender', ['Male','Female'], placeholder='Select Gender', index=None)

    senior_citizen= st.selectbox('Senior Citizen:', ['Yes', 'No'], placeholder='Select an option', index=None)
    if senior_citizen=='Yes':
        senior_citizen= 1
    else: senior_citizen=0

    partner= st.selectbox('Have a Partner?', ['Yes', 'No'], placeholder='Select an option', index=None)

with col2:
    dependents= st.selectbox('Dependents:', ['Yes', 'No'], placeholder='Select an option', index=None)

    tenure= st.number_input('Tenure:', max_value=72, min_value=0, value=None, placeholder='Enter the value')

st.write("")
st.markdown("#### Services:")

# Services block
col1,col2= st.columns([1,1])

with col1:
    internet_service= st.selectbox('Internet Service:', ['DSL', 'Fiber optic','No'], placeholder='Select an option', index=None)
    
    phone_service= st.selectbox('Phone Service:', ['Yes', 'No'], placeholder='Select an option', index=None)
    
    online_security= st.selectbox('Online Security:', ['Yes', 'No'], placeholder='Select an option', index=None)


with col2:
    device_protection= st.selectbox('Device Protection:', ['Yes', 'No'], placeholder='Select an option', index=None)
    
    streaming_tv= st.selectbox('Streaming TV:', ['Yes', 'No'], placeholder='Select an option', index=None)

    streaming_movies= st.selectbox('Streaming Movies:', ['Yes', 'No'], placeholder='Select an option', index=None)

st.write("")
st.markdown("#### Payment Details:")

# Payment block
col1,col2= st.columns([1,1])

with col1:
    contract= st.selectbox('Contract:', ['Month-to-month', 'Two year', 'One year'], placeholder='Select an option', index=None)

with col2:
    paymentmethod= st.selectbox('Payment Method:', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], placeholder='Select an option', index=None)



input_data = pd.DataFrame({
    "gender": [gender],
    "SeniorCitizen": [senior_citizen],
    "Partner": [partner],
    "Dependents": [dependents],
    "tenure": [tenure],
    "phone_service": [phone_service],
    "internet_service": [internet_service],
    "online_security": [online_security],
    "device_protection": [device_protection],
    "streaming_tv": [streaming_tv],
    "streaming_movies": [streaming_movies],
    "contract": [contract],
    "paymentmethod": [paymentmethod],


    
})


st.write("")
col1, col2, col3= st.columns([1,2,1])

with col2:
    predict=st.button("Predict", use_container_width=True)

if predict:
    if input_data.isnull().any().any():
        st.error("Please fill all required fields..")

    else:
        pred= pipe.predict(input_data.values)
        pred_prob= pipe.predict_proba(input_data.values) *100
        churn_probabilty= pred_prob[0][1]


        if pred == 1:
            st.error("Customer is likely to churn...")

        else: st.success('Customer is not likely to churn...')

        st.metric('Probability to Churn:', f'{churn_probabilty:.1f}%')







