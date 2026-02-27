import streamlit as st

def show_data_overview():
    st.title("Metro Dataset Overview")

    if "datasets" not in st.session_state:
        st.error("Dataset not loaded.")
        return

    df = st.session_state.datasets["metro_data"]

    st.subheader("First 10 Rows")
    st.dataframe(df.head(10))

    st.subheader("Dataset Info")
    st.write(f"Total Rows: {df.shape[0]}")
    st.write(f"Total Columns: {df.shape[1]}")

    st.subheader("Column Names")
    st.write(df.columns.tolist())
