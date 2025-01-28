import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv('./datasets/Lobbyist_Data_-_Lobbyists_20250121.csv')

def main():
    data = load_data()
    st.sidebar.header("Filters")

if __name__  == '__main__':
    main()

