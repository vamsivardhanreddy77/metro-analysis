import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def crowd_prediction():
    st.title("🚇 Metro Station Intelligence Dashboard")

    if "datasets" not in st.session_state:
        st.error("Dataset not loaded.")
        return

    # Make safe copy
    df = st.session_state.datasets["metro_data"].copy()

    # ===============================
    # CLEAN NUMERIC COLUMNS
    # ===============================
    numeric_cols = [
        "Dist. From First Station(km)",
        "Opened(Year)",
        "Latitude",
        "Longitude"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows where essential numeric data is missing
    df = df.dropna(subset=["Latitude", "Longitude"])

    # ===============================
    # LINE SELECTION
    # ===============================
    selected_line = st.selectbox(
        "Select Metro Line",
        df["Metro Line"].dropna().unique()
    )

    line_df = df[df["Metro Line"] == selected_line]

    if line_df.empty:
        st.warning("No data available for this line.")
        return

    # ===============================
    # KPI METRICS
    # ===============================
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Stations", len(line_df))

    # Safe distance calculation
    max_distance = line_df["Dist. From First Station(km)"].max()
    if pd.notna(max_distance):
        col2.metric("Total Distance (km)", round(max_distance, 2))
    else:
        col2.metric("Total Distance (km)", "N/A")

    # Safe oldest year calculation
    oldest_year = line_df["Opened(Year)"].min()
    if pd.notna(oldest_year):
        col3.metric("Oldest Station Year", int(oldest_year))
    else:
        col3.metric("Oldest Station Year", "N/A")

    st.divider()

    # ===============================
    # INTERACTIVE MAP
    # ===============================
    st.subheader("🗺 Metro Line Map")

    map_df = line_df.rename(
        columns={
            "Latitude": "lat",
            "Longitude": "lon"
        }
    )

    st.map(map_df[["lat", "lon"]])

    st.divider()

    # ===============================
    # DISTANCE PROGRESSION
    # ===============================
    st.subheader("📏 Distance Progression")

    if pd.notna(max_distance):
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.lineplot(
            x="Dist. From First Station(km)",
            y="Station Names",
            data=line_df.sort_values("Dist. From First Station(km)"),
            marker="o",
            ax=ax
        )
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.info("Distance data not available for this line.")

    # ===============================
    # LAYOUT DISTRIBUTION
    # ===============================
    st.subheader("🏗 Station Layout Distribution")

    layout_counts = line_df["Layout"].value_counts()

    if not layout_counts.empty:
        fig2, ax2 = plt.subplots()
        ax2.pie(
            layout_counts.values,
            labels=layout_counts.index,
            autopct="%1.1f%%"
        )
        st.pyplot(fig2)
    else:
        st.info("Layout data not available.")

    st.divider()

    # ===============================
    # DATA TABLE
    # ===============================
    st.subheader("📋 Station Details")
    st.dataframe(line_df)
