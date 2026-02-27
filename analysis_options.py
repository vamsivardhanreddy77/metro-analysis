import streamlit as st
from visualizations import visualize_data
from crowd_prediction import crowd_prediction

def analysis_options():
    st.title("📈 Metro Analytics")

    choice = st.selectbox(
        "Choose Analysis",
        ["Visualizations", "Station Insights"]
    )

    if choice == "Visualizations":
        visualize_data()
    else:
        crowd_prediction()
