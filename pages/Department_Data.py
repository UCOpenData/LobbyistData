import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def activity_by_client(activity):
    client_counts = activity['CLIENT_NAME'].value_counts()
    top_clients = client_counts[:10]
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(y=top_clients.keys(), x=top_clients.values, palette="Blues_r", ax=ax)
    ax.set_xlabel("Count")
    ax.set_ylabel("Client")
    st.title("Top 10 clients with the most lobbying activity")
    st.pyplot(fig)

params = st.query_params["department_name"]
activity = pd.read_csv('./datasets/LD_Lobbying_Activity.csv')

department_name = str(params)

activity_subset = activity[activity["DEPARTMENT"] == department_name]

if (len(activity_subset) > 0):
    st.write(department_name)

    st.dataframe(activity_subset)

    activity_by_client(activity_subset)
else:
    st.write("No lobbying activity found for this department")
