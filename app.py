import streamlit as st
from multiapp import MultiApp
from apps import App
from App import (
    home,
    housing,
    timelapse,
    rois
)

st.set_page_config(layout="wide")


App = MultiApp()

# Add all your application here

App.add_app("Home", home.app)
App.add_app("Create Timelapse", timelapse.app)
App.add_app("U.S. Real Estate Data", housing.app)


# The main app
App.run()
