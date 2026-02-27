import streamlit as st
from data_loader import load_metro_data
from data_overview import show_data_overview
from visualizations import visualize_data
from crowd_prediction import crowd_prediction

st.set_page_config(page_title="Delhi Metro Analytics", page_icon="🚇", layout="wide")

st.sidebar.title(" Delhi Metro Analytics")

option = st.sidebar.radio(
    "Select Section",
    ["Data Overview", "Visualizations", "Station Insights"]
)

datasets = load_metro_data()

if datasets is None:
    st.stop()

if option == "Data Overview":
    show_data_overview()

elif option == "Visualizations":
    visualize_data()

elif option == "Station Insights":
    crowd_prediction()
