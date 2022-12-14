# Import modules
import streamlit as st

from PIL import Image

st.set_page_config(page_title="Top Page")

st.markdown("# Overview")
st.sidebar.header("Are We There Yet?")
st.sidebar.markdown("#### Data driven insights for local government traffic management.")

st.subheader("""We present to you our capstone project where we studied some well-known public transportation routes in Pasig City, Manila using traffic and geospatial data from Google Maps and OpenStreetMap.""")

img = Image.open('./media/pasig_city_road_network.png')
st.image(img, caption="Pasig City, Metro Manila Road Network")

st.markdown("#### Why did we chose this topic? As we all know, *commuting* is one of the negative experiences for the majority of us Filipinos in our daily lives. Due to poor response of our government to our traffic management crisis, Filipinos are suffering evryday and wasting precious time. Also as a nation, we lose about 4.3 billion pesos due to Metro Manila's traffic alone. And it seems like this problem won't go any time soon. So in our own little ways, we want to ease this problem with the help of machine learning.")

st.markdown("#### How? We aim to build a dashboard that shows the projected hour per hour traffic in your area. Our traffic dashboard won't solve our traffic problem overnight but what it can do is help LGU's be better drivers of change. With the help of our dashboard, local governments can make sound decisions with the help of data and ultimately, makes life a bit easier for all of us.")

st.caption("Brought to you by Group 2 | DSCF Cohort 10")

st.caption("Alawi, Chavez, Gilay, Nuqui, Tulda")