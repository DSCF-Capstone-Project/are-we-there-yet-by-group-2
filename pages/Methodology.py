import streamlit as st

from PIL import Image

st.set_page_config(page_title="Methodology")

st.markdown("# Our Methodology")
st.sidebar.header("How was this dashboard done?")
st.sidebar.subheader("From data gathering to building our machine learning model. We'll try to explain how everything was done in the simplest way we can.")

st.markdown("#### Data Collection")
st.markdown("""
    First of all, we determined the routes that we are going to investigate from OpenStreetMap where we scraped data for the road segments of each route. We then fed those nodes to Google Maps API, specifically the Distance Matrix API, to collect data such as distance and duration of travel both during traffic and non-traffic.

    <to be continued>
""")

img = Image.open('./media/general_methodology.png')
st.image(img, caption="Our whole process in a nutshell.")