import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

@st.cache_data
def load_data():
    return pd.read_csv('./datasets/LD_Lobbying_Activity.csv')

def activity_by_department(activity):
    department_counts = activity['DEPARTMENT'].value_counts()
    top_departments = department_counts[:10]
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(y=top_departments.keys(), x=top_departments.values, palette="Blues_r", ax=ax)
    ax.set_xlabel("Count")
    ax.set_ylabel("Department")
    st.title("Top 10 departments with the most lobbying activity")
    st.pyplot(fig)

def year_slider():
    date = st.slider("Select date",
                     min_value = datetime(2014,1,1),
                     max_value = datetime(2024,12,1),
                     value = datetime(2014,1,1),
                     step = timedelta(days = 1))
    return date

def main():
    activity = load_data()
    activity['DATE'] = pd.to_datetime(activity['PERIOD_START'])
    date = year_slider()
    activity_upto_date = activity[(activity['DATE'] < date) | (activity['DATE'] == date)]
    activity_by_department(activity_upto_date)


if __name__  == '__main__':
    main()