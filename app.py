# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 10:36:43 2022

@author: Student
""" 
import pickle   
import streamlit as st 
from streamlit_option_menu import option_menu 


autism_model = pickle.load(open('C:/Users/MICRO/Desktop/AutismApp/saved_model/autism_model.sav','rb')) 

with st.sidebar:
    
    selected = option_menu('HOME',
                           ['AUTISM PREDICTOR','ABOUT AUTISM','ABOUT US'],
                           icons = ['activity','person-hearts','person-lines-fill'],
                           default_index = 0) 
    
    
if (selected == 'AUTISM PREDICTOR'):
    
    st.title('AUTISM PREDICTION USING MACHINE LEARNING')
    
    
    A1_Score = st.text_input('Whether the child look at you when you call his/her name?(Yes-1/No-0)')
    A2_Score = st.text_input('How easy it is for you to get eye contact with the child?(Yes-1/No-0)')
    A3_Score = st.text_input('Does your child point to indicate that he/she wants something?(Yes-1/No-0)')
    A4_Score = st.text_input('Does your child point to share interest with you?(Yes-1/No-0)')
    A5_Score = st.text_input('Does your child pretend?(Yes-1/No-0)')
    A6_Score = st.text_input('Does your child follow when you are looking?(Yes-1/No-0)')
    A7_Score = st.text_input('If you or someone else in the family is visibly upset,does your child show signs of warning to comfort them?(Yes-1/No-0)')
    A8_Score = st.text_input('Does your child talk back when you talk?(Yes-1/No-0)')
    A9_Score = st.text_input('Does your child use simple gestures?(Yes-1/No-0)')
    A10_Score = st.text_input('Does your child stare at nothing with no apparent purpose?(Yes-1/No-0)')
    age = st.text_input('Age')
    jundice=st.text_input('Whether the child was born with jaundice?(Yes-1/No-0)')
    
    
    autism_diagnosis = ''
    
    if st.button('GET RESULT'):
        autism_prediction = autism_model.predict([[A1_Score,A2_Score,A3_Score,A4_Score,A5_Score,A6_Score,A7_Score,A8_Score,A9_Score,A10_Score,age,jundice]])
        
        if (autism_prediction[0] == 1):
            autism_diagnosis = 'The Person has the risk of Autism'
        else:
            autism_diagnosis = 'The Person does not have Autism Disease'
            
    st.success(autism_diagnosis)        
if (selected == 'ABOUT AUTISM'):
    st.title('AUTISM')
    st.text('Autism spectrum disorder (ASD) is a developmental disability caused by') 
    st.text('differences in the brain. Social, communicative, and behavioral difficulties')
    st.text('are part of ASD. These issues might range from minor to severe, or even ') 
    st.text('somewhere in between. Receiving an early diagnosis allows for a quicker')
    st.text('start to therapy because a diagnosis is dependent on the level of support')
    st.text('required. Aspergers syndrome, Rett syndrome, childhood disintegrative disorder,')
    st.text('Kanners syndrome, and pervasive developmental disorder-not otherwise specified')
    st.text('are the five main kinds of autism.')
    st.title('SYMPTOMS OF AUTISM') 
    st.text('The symptoms of ASD varies according to its types, some of the common symptoms')
    st.text('are as follows:')
    st.text('          • Moving between activities can be difficult')
    st.text('          • Issues with executive functioning')
    st.text('          • Lack of emotion, expression in their voice, flat monotonous speech, or changing their pitch to match their surroundings')
    st.text('          • Interaction challenges with classmates in school or at home')
    st.text('          • Loss of coordination and regular movement')
    st.text('          • Communication and speech difficulties')
    st.text('          • Breathing issues occasionally')
    st.text('          • Challenges in connection and communication')
    st.text('          • An obsession with manipulating items and uncontrolled speaking')    
if (selected == 'ABOUT US'):
    st.title('ABOUT US')
    st.text('This app is designed to predict whether a person has the disease of Autism or not.')
    st.text('It works by the principle of applying machine learning techniques. When the user')
    st.text('gives the inputs regarding the person, it gets tested by the machine learning model.')
    st.text('The proposed model is based on the Support Vector Machine.The input data gets tested')
    st.text(' and predicts the result.')
if (selected == 'CONTACT'):
    st.title('FURTHER CONTACT DETAILS')
    st.text('For further details contact us at www.xyz.gmail.com')