import streamlit as st
import pandas as pd
import geopandas as gpd
from data_loader import load_cyclone_data, process_data
from utils import load_geodata, plot_rainfall_map
from download_dataset import dataset

st.title('Tropical Cyclone Rainfall Visualization')

@st.cache
def load_data():
    df_train, df_test = load_cyclone_data()
    df_train = process_data(df_train)
    df_test = process_data(df_test)
    return df_train, df_test

df_train, df_test = load_data()

st.sidebar.title("Configuration")
selected_data = st.sidebar.selectbox("Select Dataset", ["Train", "Test"])

if selected_data == "Train":
    df = df_train
else:
    df = df_test

geodata = load_geodata()
fig = plot_rainfall_map(df, geodata)
st.plotly_chart(fig)

st.sidebar.markdown("## Data Sample")
st.sidebar.write(df.head())
