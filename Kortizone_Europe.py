import streamlit as st
import pandas as pd
import numpy as np
import joblib

        

def Le3ba():
    st.markdown("<p style='text-align: center; font-weight: bold;font-size: 40px;font-family: 'Calibri', Arial, sans-serif;'>ابدأ لعب    </p>", unsafe_allow_html=True)
    st.title(' ')
    st.markdown("<div style='display: flex; justify-content: center</div>", unsafe_allow_html=True)
    st.image('Website 2_page-0001.jpg')
    df=pd.read_excel('KortiEuro Database Final.xlsx',sheet_name='Sheet2')
    st.markdown("<p style='text-align: center; font-weight: bold;font-size: 25px;'>دخل رقم الكارت</p>", unsafe_allow_html=True)
    input_value = st.text_input(' ', value='0', key='Card')
    if input_value != '':
        try:
            x = int(input_value)
        except ValueError:
            st.error("دخلت رقم غلط ")
            x = 0
    else:
        x = 0

    if x == 0:
        st.write('   ')
    elif x not in df['Card'].unique():
        st.error("دخلت رقم غلط ")
        
    elif x in range(21,40) or x in range(93,123) or x in range(133,143):
        index=df[(df['Card']==x)].index[0]
        egaba=str(df[(df['Card']==x)].loc[index,'Answer'])
        egabalist=egaba.split('\n')
        formatted_text = ""
        for line in egabalist:
            formatted_text += f"<div style='text-align: right;font-size:20px;'>{line}</div>"            
        st.markdown(formatted_text, unsafe_allow_html=True)
        
        
        
    else:
        st.markdown("<p style='text-align: center; font-weight: bold;font-size: 25px;'>دخل رقم السؤال</p>", unsafe_allow_html=True)
        input_value1 = st.text_input(' ', value='0', key='Question')
        if input_value1 != '':
            try:
                y = int(input_value1)
            except ValueError:
                st.error("دخلت رقم غلط ")
                y = 0
        else:
            y = 0

        if y == 0:
            st.write('  ')
        elif y==' ':
            st.write('   ')

        elif y not in df[df['Card']==x]['Question'].unique():
            st.error("دخلت رقم غلط ")
        else:
            index=df[(df['Question']==y) & (df['Card']==x)].index[0]
            egaba=str(df[(df['Question']==y) & (df['Card']==x)].loc[index,'Answer'])
            egabalist=egaba.split('\n')
            formatted_text = ""
            for line in egabalist:
                formatted_text += f"<div style='text-align: right;font-size:20px;'>{line}</div>"            
            st.markdown(formatted_text, unsafe_allow_html=True)

            
def tare2et_el_le3b():
    
    st.markdown("<p style='text-align: center; font-weight: bold;font-size: 40px;font-family: 'Calibri', Arial, sans-serif;'>طريقة اللعب</p>", unsafe_allow_html=True)
    st.title(' ')
    st.image('How to Play (Website)_page-0001.jpg')

    


st.markdown("<p style='text-align: right; font-weight: bold;font-size: 25px;'>  اختار الصفحة</p>", unsafe_allow_html=True)    
selected_page = st.selectbox(" ", ['الرئيسية','طريقة اللعب','الاجابات'])

if selected_page=='الرئيسية':
    
    st.markdown("<div style='display: flex; justify-content: center</div>", unsafe_allow_html=True)
    st.image('bd34b9f1-e4cb-4d46-b228-ca698e87d057.jpg')
    
    
elif selected_page=='طريقة اللعب':
    tare2et_el_le3b()
    
elif selected_page=='الاجابات':
    Le3ba()
