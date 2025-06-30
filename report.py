import streamlit as st
import requests
import pandas as pd
from redcap import Project


st.title("Hello Streamlit-er 👋")
st.markdown(
    """ 
    This is a playground for you to try Streamlit and have fun. 

    **There's :rainbow[so much] you can build!**
    
    We prepared a few examples for you to get started. Just 
    click on the buttons above and discover what you can do 
    with Streamlit. 
    """
)

if st.button("Send balloons!"):
    st.balloons()

api_url = 'https://leopard-redcap.lcsb.uni.lu/redcap/api/'
api_key = st.secrets["rcapikey"]
project = Project(api_url, api_key)
data = project.export_records(format_type='df')
st.write(f"Data shape: {data.shape}")
st.histgram(data['sex_at_birth'], bins=2, title='Sex at Birth Distribution')