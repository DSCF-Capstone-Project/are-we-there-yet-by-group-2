# Import modules
import streamlit as st

from PIL import Image

st.set_page_config(page_title="Top Page")

st.markdown("# Overview")
st.sidebar.header("Are We There Yet?")
st.sidebar.markdown("#### Data driven insights for local government traffic management.")

st.subheader("""We present to you our dashboard (beta) where we studied some well-known public transportation routes in Pasig City, Manila.""")

img = Image.open('./media/pasig_city_road_network.png')
st.image(img, caption="Pasig City, Metro Manila Road Network")

st.subheader("""Why is there a need to this? Commuting is the second most negative daily life experience for the majority of us Filipinos...""")

