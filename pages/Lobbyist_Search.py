import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
@st.cache_data
def load_data():
    return pd.read_csv('./datasets/LD_Lobbyists.csv')
data = load_data()
search_query = st.text_input("Enter a lobbyist's name:", "")
if search_query:
    filtered_data = data[data["LAST_NAME"].str.contains(search_query, case=False, na=False)]
else:
    filtered_data = data

st.write(f"### Found {len(filtered_data)} Lobbyists")
for _, row in filtered_data.iterrows():
    lobbyist_name = f"{row['FIRST_NAME']} {row['LAST_NAME']}"
    lobbyist_url = f"/Individual_Data?lobbyist_id={row['LOBBYIST_ID']}"
    st.markdown(f"{lobbyist_name}")
    st.link_button(label = "see more", url = lobbyist_url )