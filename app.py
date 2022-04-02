# Import Dependencies
import streamlit as st 
import pickle

# Create a title
st.title("Car Selling Prediction Analysis")

# Load the model
filename = "random_forest_regression_model.pkl"
model = pickle.load(open(filename, 'rb'))


# Create a Year Option
st.header("Choose the Year")
Year = st.selectbox(" ",["1990","2011","2012","2013","2018","2017","2015","2016"])
Year = int(Year)
Year = 2021-Year

# Create a Present_Price Option
st.header("What is the Showroom Price?(In MYR)")
Present_Price = st.selectbox(" " , ["5", "10" , "6"])
Present_Price = int(Present_Price)

# Create a Kms Driven Option
st.header("How Many Kilometers Drived?")
Kms_Driven = st.selectbox(" " , ["24000" ,"2400","57000","60000","15001","22517","12900","53000"])
Kms_Driven = int(Kms_Driven)

# Create a Owner Option
st.header("How much owners previously had the car(0 or 1 or 3) ?")
Owner = st.selectbox(" " , ["3" , "1"])

# Create a Fuel Type Option
st.header("What Is the Fuel type?")
Fuel_Type_Petrol = st.selectbox(" " , ["Petrol" , "Diesel" , "CNG"])

if Fuel_Type_Petrol == "Petrol":
    Fuel_Type_Petrol = 1
    Fuel_Type_Diesel = 0

elif Fuel_Type_Petrol == "Diesel":
    Fuel_Type_Petrol = 0
    Fuel_Type_Diesel = 1

else:
    Fuel_Type_Petrol = 0
    Fuel_Type_Diesel = 0

# Create a Seller Type Option
st.header("Are you A Dealer or Individual?")
Seller_Type_Individual = st.selectbox(" ", ["Dealer" , "Individual"])

if Seller_Type_Individual == "Individual":
    Seller_Type_Individual = 1

else:
    Seller_Type_Individual = 0

# Create a Transmission Type Option
st.header("Transmission type?")
Transmission_Mannual = st.selectbox(" ", ["Manual" , "Automatic"])

if Transmission_Mannual == "Manual":
    Transmission_Mannual = 1

else:
    Transmission_Mannual = 0

# Create a Predict_model() function to predict the car selling price
def Predict_model():
    prediction = model.predict([[Present_Price,Kms_Driven,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
    output=round(prediction[0],2)
    if output<0:
        st.warning("Sorry you can not Sell this car")
    else:
        st.success("You can Sell this car at {} Lakh".format(output))

if st.button("Predict"):
    Predict_model()
