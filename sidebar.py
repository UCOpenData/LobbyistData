import streamlit as st

def init_sidebar():
    st.sidebar.page_link('pages/Lobbyist_Search.py', label='Lobbyist Search')
    st.sidebar.page_link('pages/Department_Search.py', label='Department Search')
    st.sidebar.page_link('pages/Top_10_Charts.py', label='Top 10 Charts')
    st.sidebar.page_link('pages/video.py', label='Video of progression')