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

# Customize page title
st.title("Deriving fractional vegetation cover from uncrewed aerial systems")

st.markdown(
    """
    This multipage app template demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). It is an open-source project and you are very welcome to contribute to the [GitHub repository](https://github.com/opengeos/streamlit-map-template).
    """
)

st.header("Instructions")

markdown = """
1. For the [GitHub repository](https://github.com/opengeos/streamlit-map-template) or [use it as a template](https://github.com/opengeos/streamlit-map-template/generate) for your own project.
2. Customize the sidebar by changing the sidebar text and logo in each Python files.
3. Find your favorite emoji from https://emojipedia.org.
4. Add a new app to the `pages/` directory with an emoji in the file name, e.g., `1_🚀_Chart.py`.

"""

st.markdown(markdown)

st.header("Location of the three study sites at Calperum Station, South Australia")

m = leafmap.Map(center=[-34.167671, 140.751541], zoom=8, minimap_control=True)
# m.add_basemap("OpenTopoMap")
m.add_tile_layer(
    url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    name="Google Satellite",
    attribution="Google",
)
m.to_streamlit(height=500)
