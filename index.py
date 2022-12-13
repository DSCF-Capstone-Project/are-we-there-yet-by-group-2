# Import modules
import streamlit as st

# Import other dependencies
from views import Pages


# List of Pages
page_list = [
    "Introduction"
]

# Sidebar with project title
st.sidebar.title(':scroll: Are We There Yet?')
page = st.sidebar.radio('Explore: ', page_list)


# Showing which pages are shown
if page == "Overview":
    Pages.intro()