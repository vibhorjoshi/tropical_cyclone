import geopandas as gpd
import plotly.express as px

def load_geodata():
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    return world

def plot_rainfall_map(df, geodata):
    fig = px.choropleth_mapbox(
        df,
        geojson=geodata.__geo_interface__,
        locations='iso_a3',
        color='rainfall',
        hover_name='name',
        color_continuous_scale='Viridis',
        mapbox_style='carto-positron',
        zoom=1,
        center={"lat": 0, "lon": 0},
        opacity=0.5
    )
    return fig


