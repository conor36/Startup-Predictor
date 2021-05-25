import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


@st.cache

def load_data():
    df = pd.read_csv("investmentVC.csv") 
    df = df[[" market ", " funding_total_usd ", "country_code", "founded_year", "status"]]
    df = df.rename({" market ": "market", " funding_total_usd ": "funding"}, axis=1)
    df['funding'] = df['funding'].str.replace(',', '').str.replace(' -   ', '').str.replace(' ', '').str.replace('  ', '').str.replace('   ', '').str.replace('  ', '').str.replace('    ', '')
    df.replace('', np.nan, inplace = True)
    df = df.dropna()
    df['funding'] = df['funding'].astype(float)
    df['market'] = df['market'].str.replace(' ', '')
    df = df.loc[df['market'].isin(['Software',
 'Biotechnology',
 'Mobile',
 'E-Commerce',
 'CuratedWeb',
 'EnterpriseSoftware',
 'HealthCare',
 'Hardware+Software',
 'Advertising',
 'Games',
 'CleanTechnology',
 'HealthandWellness',
 'SocialMedia',
 'Education',
 'Finance'])]
    
    df.drop(index=df[df['status'] == 'operating'].index, inplace=True)
    country_map = shorten_categories(df.country_code.value_counts(), 17)
    df['country_code'] = df['country_code'].map(country_map)
    print(df)
    return df


df = load_data()

def show_explore_page():

    st.title("Explore Startup Data")

    st.write("""## This page is a little exploration of the dataset provided by Crunchbase for startups around the world up until 2013""")

    st.write("""### The full dataset can be found [here](https://www.kaggle.com/arindam235/startup-investments-crunchbase)""")

    data = df["status"].value_counts()

    fig1, ax1 = plt.subplots()
    colors = ['#66b3ff','#ff9999']
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", colors= colors, shadow=False)
    ax1.axis("equal")
    
    
    st.write("""
    ### Number of Data from different countries
    """)

    st.pyplot(fig1)
    
    st.write(
    
    """
    
    ### Mean Funding Based On Country

    """
    )

    data = df.groupby(["country_code"])["funding"].mean().sort_values(ascending=True)
    st.bar_chart(data)
    
    st.write(
    """
    
    ### Mean Funding Based On Market

    """
    )
    data2 = df.groupby(["market"])["funding"].mean().sort_values()
    st.bar_chart(data2)




  
