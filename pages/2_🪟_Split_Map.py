import streamlit as st
import leafmap.foliumap as leafmap

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
import random

m = leafmap.Map(center=[0, 0], zoom=2)

url = "https://huggingface.co/datasets/lauransotomayor/eco_composition/raw/main/mask_fvc_3072.16.shp"


def random_color(feature):
    return {
        "color": "black",
        "fillColor": random.choice(["red", "yellow", "green", "orange"]),
    }


m.add_shp(url, layer_name="class", style_callback=random_color)
m