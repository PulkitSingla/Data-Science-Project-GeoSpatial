import streamlit as st
from multiapp import MultiApp
from home import Home
from housing import Housing
from timelapse import Timelapse
# from apps import (
#    home,
#    housing,
#    timelapse,
#    rois
# )

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here

apps.add_app("Home", Home())
apps.add_app("Create Timelapse", Timelapse())
apps.add_app("U.S. Real Estate Data", Housing())


# The main app
apps.run()
