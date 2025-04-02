import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

@st.cache_data
def load_lobbyists_data():
    return pd.read_csv('./datasets/LD_Lobbyists.csv')

def load_activity_data():
    return pd.read_csv('./datasets/LD_Lobbying_Activity.csv')

def year_slider():
    date = st.slider("Select date",
                     min_value = datetime(2014,1,1),
                     max_value = datetime(2024,12,1),
                     value = datetime(2014,1,1),
                     step = timedelta(days = 1))
    return date

def by_state(data, is_activity):
    state_counts = data["STATE"].value_counts().reset_index()
    state_counts.columns = ["State", "Count"]
    top_states = state_counts.head(10)
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(y=top_states["State"], x=top_states["Count"], palette="Blues_r", ax=ax)
    ax.set_xlabel("Count")
    ax.set_ylabel("State")

    if is_activity:
        ax.set_title("Top 10 States with the most lobbying activity")
    else:
        ax.set_title("Top 10 Most Common States in Lobbyist Registry")
    st.pyplot(fig)

def by_employee(data, is_activity):
    if is_activity:
        company_counts = data["CLIENT_NAME"].value_counts().reset_index()
    else:
        company_counts = data["EMPLOYER_NAME"].value_counts().reset_index()
    company_counts.columns = ["Employer", "Count"]
    top_companies = company_counts.head(20)
    fig_1, ax_1 = plt.subplots(figsize=(5, 6))
    sns.barplot(y=top_companies["Employer"], x=top_companies["Count"], palette="Blues_r", ax=ax_1)
    ax_1.set_xlabel("Count")
    ax_1.set_ylabel("Employer")
    if is_activity:
        ax_1.set_title("Top 10 Employers with the most lobbying activity")
    else:
        ax_1.set_title("Top 10 Most Common Employers in Lobbyist Registry")
    st.pyplot(fig_1)

def by_department(activity):
    department_counts = activity['DEPARTMENT'].value_counts()
    top_departments = department_counts[:10]
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(y=top_departments.keys(), x=top_departments.values, palette="Blues_r", ax=ax)
    ax.set_xlabel("Count")
    ax.set_ylabel("Department")
    ax.set_title("Top 10 departments with the most lobbying activity")
    st.pyplot(fig)

lobbyists = load_lobbyists_data()

by_state(lobbyists, False)
by_employee(lobbyists, False)

dict_state_lobbyist = dict(lobbyists.drop_duplicates(subset=['LOBBYIST_ID'])[["LOBBYIST_ID", "STATE"]].values)

activity = load_activity_data()

activity['DATE'] = pd.to_datetime(activity['PERIOD_START'])
activity['STATE'] = [dict_state_lobbyist[id] for id in activity['LOBBYIST_ID']]

date = year_slider()
activity_upto_date = activity[(activity['DATE'] < date) | (activity['DATE'] == date)]

by_state(activity_upto_date, True)
by_employee(activity_upto_date, True)
by_department(activity_upto_date)