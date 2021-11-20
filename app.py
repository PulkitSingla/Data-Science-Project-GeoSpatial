from apps import (
    home,
    housing,
    timelapse,
)
import streamlit as st
from multiapp import MultiApp
from home import Home
from housing import Housing
from timelapse import Timelapse
from

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here

apps.add_app("Home", Home.app)
apps.add_app("Create Timelapse", Timelapse.app)
apps.add_app("U.S. Real Estate Data", Housing.app)


# The main app
apps.run()
