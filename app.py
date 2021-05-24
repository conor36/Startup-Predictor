import streamlit as st
from predict import show_predict_page
from explore import show_explore_page

st.set_page_config(page_title="Startup Predictor", page_icon=":rocket:")
page = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()



