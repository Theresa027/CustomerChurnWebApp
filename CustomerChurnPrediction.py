import pickle
import sklearn
import numpy as np
import streamlit as st
#to display images
from PIL import Image



#loading the saved model
loaded_model = pickle.load(open("Churn_model.sav", 'rb'))


#creating a function for prediction

def Customer_churn(input_data):

    #changing the input_data_to_numpy_array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return "The Customer has Exited"
    else:
        return "The Customer has not Exited"

def main():
    # display image
    img = Image.open("Customer_Churn_Prediction_img.png")
    new_image = img.resize((700, 200))
    st.image(new_image)
    # let's display
    # st.image(img, width=700)

    # giving a title
    st.title('Customer Churn Prediction')

    # getting the input data from the user


    CreditScore = st.number_input('Customer Credit Score')
    Geography = st.number_input('Input Geography as: 1 is France, 2 is Germany, 3 is Spain')
    Gender = st.number_input('Input Gender as : 0 is Male, 1 is Female')
    Age = st.number_input('Age of Customer')
    Tenure = st.number_input('How long has the customer been on board')
    Balance = st.number_input('Customer Account Balance')
    NumOfProducts = st.number_input('How many products does the customer use')
    HasCrCard = st.number_input('Does the customer have credit card? 0 is yes, 1 is no')
    IsActiveMember = st.number_input('Is the customer Active? 0 is yes, 1 is no')
    EstimatedSalary = st.number_input('Customers Estimated salary')
    Complain = st.number_input('Any complain since onboarding? 0 is yes, 1 is no')
    SatisfactionScore = st.number_input('Customer satisfaction score')
    CardType = st.number_input(
        'Input a number as card type based on the following: 0 is Diamond , 1 is Gold, 2 is Silver, 3 is Platinum ')
    PointEarned = st.number_input('How many points Earned?')



    # code for prediction
    ChurnPrediction = ''

    # creating a button for prediction

    if st.button('Churn Test Result'):
        ChurnPrediction = Customer_churn([CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Complain, SatisfactionScore, CardType, PointEarned])


        st.success(ChurnPrediction)


if __name__ == '__main__':
    main()
