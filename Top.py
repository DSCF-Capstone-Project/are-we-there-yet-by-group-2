# Import modules
import streamlit as st
import pybase64 as base64

st.set_page_config(page_title="Top Page")

# List of Pages
# page_list = [
#     "Introduction"
# ]

# Sidebar with project title
# st.sidebar.title(':scroll: Are We There Yet?')
# page = st.sidebar.radio('Explore: ', page_list)


# Showing which pages are shown
# if page == "Overview":
#     Pages.intro()

st.markdown("# Overview")
st.sidebar.header("Are We There Yet?")
st.sidebar.markdown("#### Data driven insights for local government traffic management.")

st.subheader("""We present to you our dashboard (beta) where we studied some well-known public transportation routes in Pasig City, Manila.""")

# file_ = open("../media/animation.gif", "rb")
# contents = file_.read()
# data_url = base64.b64encode(contents).decode("utf-8")
# file_.close()


st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="routes gif">',
    unsafe_allow_html=True,
)

st.subheader("""Why is there a need to this? Commuting is the second most negative daily life experience for the majority of us Filipinos...""")

