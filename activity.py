import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    return pd.read_csv('./datasets/LD_Lobbying_Activity.csv')

def activity_by_department(data):
     department_counts = data['DEPARTMENT'].value_counts()
     top_departments = department_counts[:10]
     sns.set_style("whitegrid")
     fig, ax = plt.subplots(figsize=(10, 6))
     sns.barplot(y=top_departments.keys(), x=top_departments.values, palette="Blues_r", ax=ax)
     ax.set_xlabel("Count")
     ax.set_ylabel("Department")
     st.title("Top 10 departments with the most lobbying activity")
     st.pyplot(fig)

def main():
     data = load_data()
#      activity_by_department(data)
     print(data['CREATED_DATE'])


if __name__  == '__main__':
    main()