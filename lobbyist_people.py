import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv('./datasets/Lobbyist_Data_-_Lobbyists_20250121.csv')

def main():
    data = load_data()
    st.sidebar.header("Filters")
    location_counts = data.groupby(["STATE"]).size().reset_index(name="COUNT")
    top_locations = location_counts.sort_values(by="COUNT", ascending=False).head(10)
    top_locations = top_locations.sort_values(by="COUNT", ascending=True)
    st.title("Top 10 Most Common Locations in Lobbyist Data")
    st.bar_chart(top_locations.set_index("STATE")["COUNT"])

if __name__  == '__main__':
    main()

