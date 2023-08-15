import streamlit as st
from predict import show_predict_page
from explore import show_explore_page
from streamlit.web import cli as stcli

page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()