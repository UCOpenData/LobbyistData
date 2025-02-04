import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    return pd.read_csv('./datasets/LD_Lobbyists.csv')

def main():
    data = load_data()
    st.sidebar.header("Filters")
    state_counts = data["STATE"].value_counts().reset_index()
    state_counts.columns = ["State", "Count"]
    top_states = state_counts.head(10)
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(y=top_states["State"], x=top_states["Count"], palette="Blues_r", ax=ax)
    ax.set_xlabel("Count")
    ax.set_ylabel("State")
    ax.set_title("Top 10 Most Common States in Lobbyist Data")
    st.title("Top 10 Most Common States in Lobbyist Data")
    st.pyplot(fig)
    company_counts = data["EMPLOYER_NAME"].value_counts().reset_index()
    company_counts.columns = ["Employer", "Count"]
    top_companies = company_counts.head(20)
    fig_1, ax_1 = plt.subplots(figsize=(5, 6))
    sns.barplot(y=top_companies["Employer"], x=top_companies["Count"], palette="Blues_r", ax=ax_1)
    ax_1.set_xlabel("Count")
    ax_1.set_ylabel("Employer")
    ax_1.set_title("Top 10 Most Common Employers in Lobbyist Data")
    st.title("Top 10 Most Common Employers in Lobbyist Data")
    st.pyplot(fig_1)


if __name__  == '__main__':
    main()

