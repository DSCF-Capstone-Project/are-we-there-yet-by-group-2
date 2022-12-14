import streamlit as st

from PIL import Image

st.set_page_config(page_title="Methodology")

st.markdown("# Our Methodology")
st.sidebar.header("How was this dashboard done?")
st.sidebar.markdown("##### From data gathering to building our machine learning model, we'll try to explain how everything was done in the simplest way we can.")

st.markdown("#### Data Collection")
st.markdown("""
    First of all, we determined the routes that we are going to investigate from OpenStreetMap where we scraped data for the road segments of each route, namely, *Pasig Palengke to LRT Santolan* (route 0), *Pasig City Hall to Kenneth* (route 1), and *Pasig City Hall to Ligaya* (route 2). We then fed the nodes obtained to Google Maps API, specifically the Distance Matrix API, to collect data such as distance in meters and duration of travel, both during traffic and non-traffic.
""")

img = Image.open('./media/general_methodology.png')
st.image(img, caption="Our whole process in a nutshell.")

st.markdown("""
    After a laborious data gathering, we now have a raw dataset to work with. We further cleaned our data and did some featuring engineering techniques like scaling to deal with our outliers.

    We chose K-Means and Bisecting K-Means as our models where both generated the same clusters using the same data, they only differ in the order which the nodes are clustered.
    """)

img2 = Image.open('./media/cluster_results.png')
st.image(img2, caption="Clustered data results. Notice how there are no segments from Route 1 which falls under Cluster A.")