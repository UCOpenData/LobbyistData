import streamlit as st
from sidebar import init_sidebar

st.set_page_config(page_title="Lobbyist Data App", layout="wide")

st.title("Welcome to the Lobbyist Data App!")
st.write("Use the sidebar to navigate to different pages.")

init_sidebar()