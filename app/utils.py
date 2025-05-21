import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    """Load and return cleaned solar irradiance data for all countries."""
    benin = pd.read_csv('data/benin_clean.csv')
    sierra_leone = pd.read_csv('data/sierraleone_clean.csv')
    togo = pd.read_csv('data/togo_clean.csv')

    benin['Country'] = 'Benin'
    sierra_leone['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'

    return pd.concat([benin, sierra_leone, togo], ignore_index=True)
