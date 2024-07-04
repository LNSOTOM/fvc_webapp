import streamlit as st
import leafmap.foliumap as leafmap
import random

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Laura N. Sotomayor
<https://x.com/lauransotomayor>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "assets/sotomayorstudio_flir.jpg"
st.sidebar.image(logo)

st.title("Split-panel Map")

# with st.expander("See source code"):
#     with st.echo():
#         m = leafmap.Map()
#         m.split_map(
#             left_layer="ESA WorldCover 2020 S2 FCC", right_layer="ESA WorldCover 2020"
#         )
#         m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")

# m.to_streamlit(height=700)


m = leafmap.Map(center=[0, 0], zoom=2)

url = "/media/laura/Extreme SSD/code/fvc_webapp/dataset/annotation_geojson/mask_fvc_3072.16.geojson"


style = {
    "stroke": True,
    "color": "#0000ff",
    "weight": 2,
    "opacity": 1,
    "fill": True,
    "fillColor": "#0000ff",
    "fillOpacity": 0.1,
}

hover_style = {"fillOpacity": 0.7}

m.add_geojson(url, layer_name="class", style=style, hover_style=hover_style)
m