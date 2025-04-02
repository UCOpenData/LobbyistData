import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
@st.cache_data
def load_data():
    return pd.read_csv('./datasets/LD_Lobbying_Activity.csv')
data = load_data()
departments_list = sorted(data["DEPARTMENT"].unique())
search_query = st.text_input("Enter a department's name:", "")

filtered_departments = list(filter(lambda x: search_query.lower() in x.lower(), departments_list))

st.write(f"### Found {len(filtered_departments)} Departments")
for department in filtered_departments:
    department_url = f"/Department_Data?department_name={department}"
    st.markdown(f"{department}")
    st.link_button(label = "see more", url = department_url)