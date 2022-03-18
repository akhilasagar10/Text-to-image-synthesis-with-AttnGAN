import streamlit as st
from multiapp import MultiApp
import demo

app = MultiApp()
st.set_page_config(page_title="GAN Project", initial_sidebar_state="auto")


app.add_app("Bird GANs", demo.demo_gan)



# The main app
app.run()
