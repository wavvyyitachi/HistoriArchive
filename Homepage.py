import imp
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

icon = Image.open("D:\entreprenure project 2023\website\HistoriArchive_2-removebg-preview.png")
timeline = Image.open("D:\entreprenure project 2023\website\World time line.png")
st.set_page_config(page_title="HistoriArchive-Home", page_icon= icon, layout="wide")


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


# if selected == "Home":
#     st.title(f"You have selected {selected}")
# if selected == "Projects":
#     st.title(f"You have selected {selected}")
# if selected == "Contact":
#     st.title(f"You have selected {selected}")


with st.container():
    
    st.markdown("<h1 style=' text-align: center; color: white; font-size: 130px;'>HistoriArchive</h1>", unsafe_allow_html=True)       
    st.markdown("<h1 style='text-align: center; color: white; font-size: 35px; font-family: Courier New'>A global platform for all artistic creators and game developers</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white; font-size: 20px; font-family: Courier New'>Inspire, Motivate, and Learn</h1>", unsafe_allow_html=True)


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns([1,2,1])

    with col1:
        st.write(" ")

    with col2:
        st.image(timeline)

    with col3:
        st.write(" ")
