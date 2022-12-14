import streamlit as st
import pybase64 as base64

st.set_page_config(page_title="Sa'n Ka Punta?")

file_ = open("./media/compressed.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="routes gif">',
    unsafe_allow_html=True,
)