import streamlit as st 
import numpy as np
import pandas as pd
from PIL import Image
import pickle

# import the machine learning algorithm
pickle_in = open("hepatitis_random_forest.pkl", "rb")
classifier = pickle.load(pickle_in)

def predict_hepatitis(age, sex, malaise, anorexia, liver_big, liver_firm, ascites, histology):
    prediction = classifier.predict([[age, sex, malaise, anorexia, liver_big, liver_firm, ascites, histology]])
    print(prediction)
    return prediction 

def main():
    """ Hepatitis B Detector App """

    html_temp = """
    <div style="background-color:tomato;padding:10px;margin-bottom:30px;">
    <h2 style="color:white;text-align:center;">Hepatitis B Detector App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("Age (Age in years)")
    sex = st.text_input("Sex (Male or Female)")
    malaise = st.text_input("Malaise (Discomfort  Yes or No)")
    anorexia = st.text_input("Anorexis (Vomiting Yes or No)")
    liver_big = st.text_input("Enlarged Liver due to Liver diseases(Yes or No)")
    liver_firm = st.text_input("Firm Liver due to liver diseases(Yes or No)")
    ascites = st.text_input("Excess Abdominal fluid > 25ml of fluid in the peritoneal(Yes or No)")
    histology = st.text_input("History with the disease(Yes or No)")
    
        
    if sex.lower() == "male":
        sex = 1
    elif sex.lower() == "female":
        sex = 2
        
    if malaise.lower() == "yes":
        malaise = 1
    elif malaise.lower() == "no":
        malaise = 2
        
    if anorexia.lower() == "yes":
        anorexia = 1
    elif anorexia.lower() == "no":
        anorexia = 2
        
    if liver_big.lower() == "yes":
        liver_big = 1
    elif liver_big.lower() == "no":
        liver_big = 2
        
    if liver_firm.lower() == "yes":
        liver_firm = 1
    elif liver_firm.lower() == "no":
        liver_firm = 2
        
    if ascites.lower() == "yes":
        ascites = 1
    elif ascites.lower() == "no":
        ascites = 2
        
    if histology.lower() == "yes":
        histology = 1
    elif histology.lower() == "no":
        histology = 2    
    
    result  = ""
    
    if st.button("Predict"):
        result=predict_hepatitis(age, sex, malaise, anorexia, liver_big, liver_firm, ascites, histology)
    if result == 1:
        st.success('Hello there, You have Hepatitis B')
    elif result == 2:
        st.success("Hello there, You do not have Hepatitis B")
    if st.button("About"):
        st.text("Learn more about Hepatitis B")
        st.text("Built with Streamlit By Chioma")
     
       
if __name__ == '__main__':
	main()
