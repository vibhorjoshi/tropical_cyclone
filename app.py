import streamlit as st
import pandas as pd
from data_loader import process_data,load_cyclone_data
from utils import load_geodata, plot_wind_speed_map
import plotly.express as px
from download_dataset import load_cyclone_data
@st.cache_data
def load_and_process_data():
    df = pd.read_csv('tropical_cyclone_data.csv')
    # Split the dataframe into train and test sets based on a specific criterion
    # Here, we assume the split is based on some column values or a predefined split
    # Replace this with actual logic for your dataset
    df_train = df[df['split'] == 'train']
    df_test = df[df['split'] == 'test']
    return df_train, df_test
    
# """Load cyclone data from a CSV file."""


def plot_wind_speed_over_time(df):
    fig = px.line(df, x='relative_time', y='wind_speed', title='Wind Speed Over Time')
    return fig

def plot_wind_speed_scatter(df):
    fig = px.scatter(df, x='relative_time', y='wind_speed', color='storm_id', title='Wind Speed Scatter Plot')
    return fig

def main():
    st.title("Tropical Cyclone Data Analysis")

    # Load and process the data
    df_train, df_test = load_and_process_data()

    # Plot wind speed over time
    st.header("Wind Speed Over Time")
    fig_time = plot_wind_speed_over_time(df_train)
    st.plotly_chart(fig_time)

    # Plot wind speed scatter plot
    st.header("Wind Speed Scatter Plot")
    fig_scatter = plot_wind_speed_scatter(df_train)
    st.plotly_chart(fig_scatter)

    # Load geospatial data
    world = load_geodata()

    # Plot wind speed map
    fig_scatter, fig_heatmap = plot_wind_speed_map(df_train)

    st.subheader("Scatter Plot")
    st.plotly_chart(fig_scatter)

    st.subheader("Heatmap")
    st.plotly_chart(fig_heatmap)

    # Display the world map
    st.header("World Map")
    fig_world_map = px.choropleth_mapbox(
        world,
        geojson=world.geometry,
        locations=world.index,
        mapbox_style="carto-positron",
        color="pop_est",
        title="World Map",
        center={"lat": 0, "lon": 0},
        zoom=1
    )
    st.plotly_chart(fig_world_map)

if __name__ == "__main__":
    main()



   
