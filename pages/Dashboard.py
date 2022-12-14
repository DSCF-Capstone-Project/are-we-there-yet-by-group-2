import streamlit as st

st.set_page_config(page_title="Traffic Dashboard")

st.markdown("# Dashboard")
st.sidebar.header("Traffic Dashboard (Beta)")

route_tab, traffic_tab = st.tabs(["Route Data", "Traffic Info"])


with route_tab:
    st.subheader("See traffic data of the chosen routes in a given day.")

    date = st.selectbox("Choose Date", ["Dec. 12, 2022"])
    time = st.selectbox("Choose Time", ["05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"])

    image_filename = "2022-12-05_" + time[:2] + ".png"

    if time:
        st.image("./media/"+image_filename)

with traffic_tab:
    st.subheader("See the clustered segments of each chosen route.")

    cluster = st.selectbox("Choose Route", ["Route0 - Pasig Palengke to LRT Santolan", "Route1 -Pasig City Hall to Kenneth", "Route2 - Pasig City Hall to Ligaya"])

    img_filename = cluster[:6]
    img_filename = img_filename.lower()

    if cluster:
        st.image('./media/'+ img_filename +'_clustered.png')
    
    st.markdown("""
        * Cluster A (_FAST_) - **Blue**
        * Cluster B (_AVERAGE_) - **Green**
        * Cluster C (_SLOW_) - **Yellow**
        * Cluster D (_VERY SLOW_) - **Red**
    """)