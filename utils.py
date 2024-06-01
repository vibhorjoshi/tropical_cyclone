import geopandas as gpd
import plotly.express as px

def load_geodata():
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    return world

import plotly.express as px

def plot_wind_speed_map(df):
    print(df.head())  # Debug: Print first few rows of DataFrame
    print(df.columns)  # Debug: Print column names
    
    # Scatter plot
    fig_scatter = px.scatter(
        df,
        x='relative_time',
        y='wind_speed',
        color='ocean',
        hover_name='storm_id',
        title='Wind Speed and Ocean Data Scatter Plot',
        template='plotly'
    )
    
    # Heatmap
    fig_heatmap = px.density_heatmap(
        df,
        x='relative_time',
        y='wind_speed',
        marginal_x='histogram',
        marginal_y='histogram',
       
        title='Wind Speed and Ocean Data Heatmap',
        template='plotly'
    )

    return fig_scatter, fig_heatmap
