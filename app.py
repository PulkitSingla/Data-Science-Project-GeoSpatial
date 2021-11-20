import streamlit as st
from multiapp import MultiApp
from apps import (
    home,
    housing,
    timelapse,
)

st.set_page_config(layout="wide")


apps = MultiApp()

# Add all your application here

apps.add_app("Home", home.app)
apps.add_app("Create Timelapse", timelapse.app)
apps.add_app("U.S. Real Estate Data", housing.app)


# The main app
apps.run()
