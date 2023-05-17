import imp
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

temple = Image.open("D:\entreprenure project 2023\website\Render_result.png")
icon = Image.open("D:\entreprenure project 2023\website\HistoriArchive_2-removebg-preview.png")
st.set_page_config(page_title="About Us", page_icon= icon, layout="wide")

selected = option_menu(
     menu_title=None,  # required
     options=["HistoriArchive"],  # required
     icons=["box"],  # optional
     menu_icon="cast",  # optional
     default_index=0,  # optional
     orientation="horizontal",
     styles={
         "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "silver", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "purple",
                },
                "nav-link-selected": {"background-color": "purple"},
            },
)

st.markdown("<h1 style=' text-align: center; color: white; font-size: 130px;'>Nara Period: 710-794</h1>", unsafe_allow_html=True)       

st.header("Classic Architecture: Todaiji Temple")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(temple)
    with text_column:
        st.write("[Interactive 3D Model >](https://app.vectary.com/p/5zbTD9EdFZMbULM90PjG4e)")
    