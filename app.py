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
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Hepatitis B Detector App </h2>
    </div>
    """

if __name__ == '__main__':
	main()
