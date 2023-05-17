import imp
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

leo = Image.open("Leo.jpg")
josh = Image.open("Josh.png")
chris = Image.open("Chris.jpg")
jinu = Image.open("Jinu.png")
park = Image.open("Park.png")
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

st.markdown("<h1 style=' text-align: center; color: white; font-size: 130px;'>About Us</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white; font-size: 30px; font-family: Courier New'>Dublin High School students who are aspiring to become successful engineers, entrepreneurs, coders, and more. Our team is made up of 4 budding engineers: Leo, Jinu, Chris, and Josh. Our goal is to give more accurate historical information, while preserving culture and spreading cultural diversity at the same time.</h1>", unsafe_allow_html=True)      


st.write("")
st.write("")
st.write("")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(leo)
    with text_column:
        st.subheader("Leo (Yuzhen) Zhu")
        st.write("Project Lead and currently enrolled in AP CSP, over 5 years of experience with 3D modeling and 3 years with programing. Passionate about art and history. Currently a part time concept artist and 3D modeler while persuing the roll of a highschool student at the same time.")
        st.write("[Personal Portfolio >](https://sites.google.com/mydusd.org/yuzhen-portfolio/home)")
        st.write("[Art Portfolio >](https://sites.google.com/view/yuzhen-zhu-portfolio/color)")
        
st.write("")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(jinu)
    with text_column:
        st.subheader("Jinu Park")
        st.write("Currently enrolled in IED, experienced with 3D modeling and an expert at using fusion 360. He holds a strongsuit in mathmetics and calculations, experienced with ultilitizing math and science for creative purposes. Passinoate about history and world culture, a strong write at the same time. ")

st.write("")
        
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(josh, width = 176)
    with text_column:
        st.subheader("Josh Zeng")
        st.write("Currently enrolled in AP CSP and passinoate about programming, great at implementing python algorithims and libraries")

st.write("")
        

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(chris, width = 176)
    with text_column:
        st.subheader("Chris Chung")
        st.write("Currently enrolled in AP CSP and passinoate about programming, passionate about gaming and online application development.")

st.write("")
       