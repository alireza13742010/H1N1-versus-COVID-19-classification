import streamlit as st
import pandas as pd 
import os 
import numpy as np 
from sklearn.preprocessing import LabelEncoder
from Processing_COVID19_H1N1 import Preprocesing
import pickle
import plotly.express as px
import streamlit.components.v1 as components
import base64

import streamlit as st
import base64


Global_path = os.path.abspath(os.getcwd())
# Load background image
background_image_path = f"{Global_path}/background.jpeg"
with open(background_image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

# Define the HTML template with inline CSS for background and button
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asset Development </title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-image: url(data:image/jpg;base64,{encoded_image});
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            height: 100vh;
            width: 100vw;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .container {{
            width: 60%;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
        }}
        .container h1 {{
            font-size: 24px;
            margin-bottom: 20px;
        }}
    </style>
</head>
</html>
"""

components.html(html_template, height=600)






Global_path = os.path.abspath(os.getcwd())



Fatigue = st.multiselect( "Do you feel fraustrations in moving your muscle?",
    ["Yes", "No", "fatigue(Moderate)", "fatigue(Severe)"])

Gastrointestinal = st.multiselect( "Do you have gastrointestinal problem?",
    ["Yes", "No"])   
    
fever = st.multiselect( "Do you have fever?",
    ["Yes","fever(Moderate)", "No"])         

drycough = st.multiselect( "Do you have dry cough?",
    ["Yes", "No", "cough(Mild)"])

Sore_throat = st.multiselect( "Do you have sorethroat?",
    ["Yes", "No"])    

Running_Nose = st.multiselect( "Do you have running nose?",
    ["Yes", "No", "running nose(Mild)"])     

Hyper_Tension = st.multiselect( "Do you have Hyper tension?",
    ["Yes", "No"])  

Headache = st.multiselect( "Do you have headache?",
    ["Yes", "No", "headache(Mild)", "headache(Severe)"])   

Breathing_Problem = st.multiselect( "Do you have breathing problem?",
    ["Yes", "No"])

Asthma =  st.multiselect( "Do you have asthma?",
    ["Yes", "No"])

Chronic_Lung_Disease =  st.multiselect( "Do you have chronic lung disease?",
    ["Yes", "No"])

Heart_Disease =  st.multiselect( "Do you have heart disease?",
    ["Yes", "No"])

Diabetes =  st.multiselect( "Do you have Diabetes?",
    ["Yes", "No"])    

Abroad_travel =  st.multiselect( "Have you get out of the country recently?",
    ["Yes", "No"])

Contact_with_COVID_Patient =  st.multiselect( "Have you been in contact with COVID-19 patients?",
    ["Yes", "No"])  

Attended_Large_Gathering =  st.multiselect( "Have you attened in any social event with population more than 50 people?",
    ["Yes", "No"]) 


Visited_Public_Exposed_Places =  st.multiselect( "Have you gone to proven exposed places to COVID-19?",
    ["Yes", "No"])   

Family_working_in_Public_Exposed_Places =  st.multiselect( "Dose your family member works in public place exposed to COVID-19 virus?",
    ["Yes", "No"])                              
if Breathing_Problem and fever and drycough and Family_working_in_Public_Exposed_Places and Visited_Public_Exposed_Places:
    data = {'Breathing Problem':Breathing_Problem, 'Fever':fever, 'Dry Cough':drycough,
            'Sore throat':Sore_throat, 'Running Nose':Running_Nose, 'Asthma':Asthma,
            'Chronic Lung Disease':Chronic_Lung_Disease, 'Headache':Headache,
            'Heart Disease':Heart_Disease, 'Diabetes': Diabetes, 'Hyper Tension':Hyper_Tension , 'Fatigue ': Fatigue,
           'Gastrointestinal ' :Gastrointestinal , 'Abroad travel': Abroad_travel, 'Contact with COVID Patient' : Contact_with_COVID_Patient,
           'Attended Large Gathering': Attended_Large_Gathering, 'Visited Public Exposed Places':Visited_Public_Exposed_Places,
           'Family working in Public Exposed Places':Family_working_in_Public_Exposed_Places}
    df = pd.DataFrame(data)
    
    df2 = Preprocesing(df)
    var_mod = ['Asthma', 'Chronic Lung Disease',
           'Heart Disease', 'Diabetes',
           'Abroad travel', 'Contact with COVID Patient',
           'Attended Large Gathering', 'Visited Public Exposed Places',
           'Family working in Public Exposed Places']
    le = LabelEncoder()
    for i in var_mod:
        df2[i] = le.fit_transform(df2[i])
    df2 = df2.astype('int64')
    
    
    label = {0 : 'You havent disgnosed with COVID-19 or H1N1',
             1 : 'You might be infected with H1N1',
             2 : 'You might be infected with COVID-19'}
    
    model_path = "ASK FOR MODEL PATH UISNG https://www.linkedin.com/in/alireza-tavakolian-6a23161b4?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B%2BY5JyNFPQnCEMC%2B7ZQJI0Q%3D%3D"
    with open(f'{Global_path}/{model_path}', 'rb') as f:
        model = pickle.load(f)
        out = model.predict(df2)
        probobality =model.predict_proba(df2)
        result = label[int(out)]
    #st.write("***P shape***:  ", probobality.shape)
    #st.write("***P type***:  ", type(probobality))  
    st.write("***This is your test result***:  ", result)  
    st.write("***The level of mode confidency***:  ", probobality)  
    probobality_df = pd.DataFrame({"classes": ["Nor COVID-19 no H1N1", "H1N1", "COVID-19"], 
                               "Probobality" : [probobality[0][0],probobality[0][1],probobality[0][2]]})
    st.write("***The level of mode confidency***:  ", probobality_df)  
    fig=px.pie(probobality_df, values='Probobality', names='classes',title='The confidency level for each prediction')
    st.plotly_chart(fig)  

    