import streamlit as st
from streamlit_folium import folium_static
import folium
from folium.features import DivIcon
import pandas as pd

from Translator import Translator

st.sidebar.title("Translator")
text = st.sidebar.text_input("Enter text to translate:")
n_country = st.sidebar.slider("Number of countries to show:", 1, 30, 5)

if text:
    translations = Translator().translate(text, n_country)
    df = pd.DataFrame(translations)
    st.write(df)

    m = folium.Map()

    for translation in translations:
        text = f"Country: {translation['country']}<br/>{translation['lang_name']}: {translation['translation']}"
        folium.Marker(location=[translation['latitude'], translation['longitude']],
            icon=DivIcon(
                icon_size=(150,36),
                icon_anchor=(7,20),
                html=f'<div style="font-size: 12pt; color:black">{translation["translation"]}</div>',
            ), popup=text, tooltip=text).add_to(m)

    folium_static(m)
