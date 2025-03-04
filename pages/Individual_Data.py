import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from activity import activity_by_department

params = st.query_params["lobbyist_id"]
activity = pd.read_csv('./datasets/LD_Lobbying_Activity.csv')

person_id = int(params)

activity_subset = activity[activity["LOBBYIST_ID"] == person_id]

first_name = activity_subset["LOBBYIST_FIRST_NAME"].iloc[0]
last_name = activity_subset["LOBBYIST_LAST_NAME"].iloc[0]

st.write(first_name + " " + last_name)

st.dataframe(activity_subset)

activity_by_department(activity_subset)