import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from activity import activity_by_department

params = st.query_params["lobbyist_id"]
data = pd.read_csv('./datasets/LD_Lobbying_Activity.csv')

person_id = int(params)

activity_subset = data[data["LOBBYIST_ID"] == person_id]

st.dataframe(activity_subset)

activity_by_department(activity_subset)