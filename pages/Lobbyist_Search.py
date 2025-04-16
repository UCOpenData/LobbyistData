import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sidebar import init_sidebar
from thefuzz import fuzz

init_sidebar()

@st.cache_data
def load_data():
    return pd.read_csv('./datasets/LD_Lobbyists.csv')

def run_search(data, query):
    lobbyists = pd.DataFrame({"ID": data["LOBBYIST_ID"],
                                     "NAME": data["FIRST_NAME"] + " " + data["LAST_NAME"]})

    lobbyists["SCORE"] = [fuzz.ratio(query.upper(), name) +
                                 2 * fuzz.partial_ratio(query.upper(), name) for name in lobbyists["NAME"]]

    lobbyists_nodups = lobbyists.drop_duplicates(subset = ["ID"])

    lobbyists_sorted = lobbyists_nodups.sort_values(by = "SCORE", ascending = False)

    lobbyists_filtered = lobbyists_sorted[lobbyists_sorted["SCORE"] > 200]

    st.write(f"### Found {len(lobbyists_filtered)} Lobbyists")

    for _, row in lobbyists_filtered.iterrows():
        lobbyist_url = f"/Individual_Data?lobbyist_id={row['ID']}"
        st.markdown(row['NAME'])
        st.link_button(label = "see more", url = lobbyist_url )

lobbyist_data = load_data()
search_query = st.text_input("Enter a lobbyist's name:", None)

if search_query is not None:
    run_search(lobbyist_data, search_query)