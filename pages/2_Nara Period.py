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

st.markdown("<h1 style=' text-align: center; font-size: 130px;'>Nara Period: 710-794</h1>", unsafe_allow_html=True)       

st.header("Classic Architecture: Todaiji Temple")

with st.container():
    image_column, text_column = st.columns((1, 1))
    with image_column:
        st.image(temple, width = 400)
    with text_column:
        st.write("[Interactive 3D Model >](https://app.vectary.com/p/5zbTD9EdFZMbULM90PjG4e)")
    st.write("Tōdai-ji (東大寺, Todaiji temple, 'Eastern Great Temple') is a Buddhist temple complex that was once one of the powerful Seven Great Temples, located in the city of Nara, Japan. Though it was originally founded in the year 738 CE, Tōdai-ji was not opened until the year 752 CE. The temple has undergone several reconstructions since then, with the most significant reconstruction (that of the Great Buddha Hall) taking place in 1709.[1] Its Great Buddha Hall (大仏殿 Daibutsuden) houses the world's largest bronze statue of the Buddha Vairocana, known in Japanese as Daibutsu (大仏). The temple also serves as the Japanese headquarters of the Kegon school of Buddhism. The temple is a listed UNESCO World Heritage Site as one of the 'Historic Monuments of Ancient Nara', together with seven other sites including temples, shrines and places in the city of Nara.")    
    st.write("")
    st.write("In 743, Emperor Shōmu issued a law stating that the people should become directly involved with the establishment of new Buddhist temples throughout Japan. The Emperor believed that such piety would inspire Buddha to protect his country from further disaster. Gyōki, with his pupils, traveled the provinces asking for donations. According to records kept by Tōdai-ji, more than 2,600,000 people in total helped construct the Great Buddha and its Hall; contributing rice, wood, metal, cloth, or labor; with 350,000 working directly on the statue's construction. The 16 m (52 ft) high statue was built through eight castings over three years, the head and neck being cast together as a separate element. The making of the statue was started first in Shigaraki. After enduring multiple fires and earthquakes, the construction was eventually resumed in Nara in 745, and the Buddha was finally completed in 751. A year later, in 752, the eye-opening ceremony was held with an attendance of 10,000 monks and 4,000 dancers to celebrate the completion of the Buddha. The Indian priest Bodhisena performed the eye-opening for Emperor Shōmu. The project cost Japan greatly, as the statue used much of Japan's bronze and relied entirely on imported gold. 48 lacquered cinnabar pillars, 1.5 m in diameter and 30 m long, support the blue tiled roof of the Daibutsu-den.")