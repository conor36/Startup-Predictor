import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model_loaded = data["model"]
market_fit = data["market_fit"]
country_fit = data["country_fit"]

def show_predict_page():
    st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style> """, unsafe_allow_html=True)
    
    st.set_page_config(page_title="Startup Predictor")
    
    st.title("Predict if a Startup Will be Succesful ':rocket:')

    st.write("""#### This a project using Random Forest Classifaction model to determine if a startup will be acquired or closed based on the several values below. For a full breakdwon on how this was made, feel free to visit my medium article [here]. The full dataset can be found [here](https://www.kaggle.com/arindam235/startup-investments-crunchbase).""")

    st.write("""#### By [Conor Reilly](http://www.conorreilly.com)""")

    st.write("""### Fill out the info below to complete prediction""")

    markets = ('E-Commerce', 'HealthandWellness', 'Education', 'CuratedWeb',
       'Software', 'Biotechnology', 'Mobile', 'Advertising', 'Games',
       'Finance', 'SocialMedia', 'EnterpriseSoftware', 'CleanTechnology',
       'Hardware+Software', 'HealthCare')

    countries = ('USA', 'Other', 'GBR', 'CAN', 'FRA', 'CHN', 'IND', 'DEU', 'ISR', 'ESP')

    market = st.selectbox("Company Market", markets)

    country = st.selectbox("Country of origin", countries)

    funding = st.slider("Funding in total (USD)", 0, 20000000, 100000, step=100000)

    founded_year = st.slider("Year company was founded", 1995, 2013, 1995, step=1)

    ok = st.button("Predict Startup Future")
    if ok:
        X = np.array([[market, funding, country, founded_year]])
        X[:, 0] = market_fit.transform(X[:,0])
        X[:, 2] = country_fit.transform(X[:,2])
        X = X.astype(float) 

        status = model_loaded.predict(X)
        st.subheader(f"The status for this company is predicted to be {status}")

    
