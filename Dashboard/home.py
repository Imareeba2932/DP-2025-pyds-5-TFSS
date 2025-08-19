#pip install streamlit 
#to run the server - streamlit run filename.py
#alternative option to run the server - python -m streamlit run filename.py
import streamlit as st

st.markdown('<h1 style="color:yellow; border: 2px solid white; text-align:center">' \
'Welcome to Titanic Dashboard</h1>',unsafe_allow_html=True)

st.image('assets\OIP.jpg')