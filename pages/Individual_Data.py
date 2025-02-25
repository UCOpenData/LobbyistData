import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

params = st.query_params["lobbyist_id"]
data = pd.read_csv

st.write(params)