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

st.markdown("#### Why did we chose this topic? As we all know, *commuting* is one of the negative experiences for the majority of us Filipinos in our daily lives. Due to poor response of our government to our traffic management crisis, Filipinos are suffering everyday and wasting precious time. Also as a nation, we lose about 4.3 billion pesos due to Metro Manila's traffic alone. And it seems like this problem won't go any time soon. So in our own little ways, we want to ease this problem with the help of machine learning.")

st.markdown(""" #### In a 2014 report by JICA (Japanese International Cooperation Agency), the Philippines endured P2.4 billion (P0.876 trillion in a year) daily losses due to traffic in Metro Manila. It was projected to get worse in 2017 that would deal P3.5 billion (P1.278 trillion in a year) daily losses due to the same reason. If compared, 2013 to 2014 Philippines’ gross domestic product grew by 6.35% (P0.841 trillion), and from 2016 to 2017 a growth by 6.39% (P1.113 trillion). Despite the economic growth, estimated losses due to traffic still outweighs the income growth for those said years.
""")

st.markdown("#### Our goal is to help LGU’s by building a dashboard that shows the projected hour per hour traffic in every street in your area. Our traffic dashboard won't solve our traffic problem overnight but what it can do is help LGU's be better drivers of change. With the help of our dashboard, local governments can make sound decisions with the help of data and ultimately, makes life a bit easier for all of us.")

st.caption("Brought to you by Group 2 | DSCF Cohort 10")

st.caption("Alawi, Chavez, Gilay, Nuqui, Tulda")