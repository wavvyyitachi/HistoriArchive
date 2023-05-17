import imp
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

temple = Image.open("render_result.png")
icon = Image.open("HistoriArchive_2-removebg-preview.png")
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
    image_column, text_column = st.columns((1, 1))
    with image_column:
        st.image(temple, width = 400)
    with text_column:
        st.write("[Interactive 3D Model >](https://app.vectary.com/p/5zbTD9EdFZMbULM90PjG4e)")
    st.write("Tōdai-ji (東大寺, Todaiji temple, 'Eastern Great Temple') is a Buddhist temple complex that was once one of the powerful Seven Great Temples, located in the city of Nara, Japan. Though it was originally founded in the year 738 CE, Tōdai-ji was not opened until the year 752 CE. The temple has undergone several reconstructions since then, with the most significant reconstruction (that of the Great Buddha Hall) taking place in 1709.[1] Its Great Buddha Hall (大仏殿 Daibutsuden) houses the world's largest bronze statue of the Buddha Vairocana, known in Japanese as Daibutsu (大仏). The temple also serves as the Japanese headquarters of the Kegon school of Buddhism. The temple is a listed UNESCO World Heritage Site as one of the 'Historic Monuments of Ancient Nara', together with seven other sites including temples, shrines and places in the city of Nara.")    
