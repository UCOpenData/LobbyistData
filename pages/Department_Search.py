import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sidebar import init_sidebar
from thefuzz import fuzz

init_sidebar()

@st.cache_data
def load_data():
    return pd.read_csv('./datasets/LD_Lobbying_Activity.csv')

def run_search(data, query):
    departments = pd.DataFrame({"NAME": data})

    departments['SCORE'] = [fuzz.ratio(query.upper(), name) +
                                 2 * fuzz.partial_ratio(query.upper(), name) for name in departments['NAME']]
    
    departments_sorted = departments.sort_values(by = "SCORE", ascending = False)
    
    departments_filtered = departments_sorted[departments_sorted['SCORE'] > 200]

    st.write(f"### Found {len(departments_filtered)} Departments")

    for _, row in departments_filtered.iterrows():
        department_url = f"/Department_Data?department_name={row['NAME']}"
        st.markdown(f"{row['NAME']}")
        st.link_button(label = "see more", url = department_url)

activity_data = load_data()

departments_list = sorted(activity_data["DEPARTMENT"].unique())
search_query = st.text_input("Enter a department's name:", None)

if search_query is not None:
    run_search(departments_list, search_query)