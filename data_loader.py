import pandas as pd
import streamlit as st

DATA_FILE = "Delhi metro.csv"

def load_metro_data():
    """Load preloaded Delhi Metro dataset"""

    if "datasets" not in st.session_state:
        try:
            df = pd.read_csv(DATA_FILE)
            st.session_state.datasets = {
                "metro_data": df
            }
        except Exception as e:
            st.error(f" Error loading dataset: {e}")
            return None

    return st.session_state.datasets
