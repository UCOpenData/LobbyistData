import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from activity import activity_by_department
try:
    params = st.query_params["lobbyist_id"]
    activity = pd.read_csv('./datasets/LD_Lobbying_Activity.csv')
    gifts = pd.read_csv('./datasets/LD_Gifts.csv')
    lobby_data = pd.read_csv('./datasets/LD_Lobbyists.csv')

    person_id = int(params)

    activity_subset = activity[activity["LOBBYIST_ID"] == person_id]
    gift_subset = gifts[gifts["LOBBYIST_ID"] == person_id]
    lobbyist_subset = lobby_data[lobby_data["LOBBYIST_ID"] == person_id]

    if (len(activity_subset) > 0):
        first_name = activity_subset["LOBBYIST_FIRST_NAME"].iloc[0]
        last_name = activity_subset["LOBBYIST_LAST_NAME"].iloc[0]
        st.write(first_name + " " + last_name)
        if (len(gift_subset) > 0):

            st.dataframe(gift_subset)

        

        st.dataframe(activity_subset)

        activity_by_department(activity_subset)
    else:
        first_name = lobbyist_subset["FIRST_NAME"].iloc[0]
        last_name = lobbyist_subset["LAST_NAME"].iloc[0]
        st.write(first_name + ' ' + last_name)
        st.write("No lobbying activity found for this lobbyist")
except:
    st.write("Please find a lobbyist in Lobbyist Search")



    
