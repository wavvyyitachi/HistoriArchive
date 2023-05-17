import imp
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

icon = Image.open("HistoriArchive_2-removebg-preview.png")
timeline = Image.open("Japan_timeline.png")
st.set_page_config(page_title="Japan", page_icon= icon, layout="wide")

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

st.markdown("<h1 style=' text-align: center; font-size: 130px;'>Japan</h1>", unsafe_allow_html=True)      

st.image(timeline)
