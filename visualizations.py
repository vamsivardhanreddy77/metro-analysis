import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data():
    st.title("📊 Metro Visualizations")

    if "datasets" not in st.session_state:
        st.error("Dataset not loaded.")
        return

    df = st.session_state.datasets["metro_data"]

    st.subheader("Stations Per Metro Line")

    line_counts = df["Metro Line"].value_counts()

    fig, ax = plt.subplots()
    sns.barplot(x=line_counts.index, y=line_counts.values, ax=ax)
    plt.xticks(rotation=45)
    plt.ylabel("Number of Stations")
    st.pyplot(fig)

    st.subheader("Station Layout Distribution")

    layout_counts = df["Layout"].value_counts()

    fig2, ax2 = plt.subplots()
    ax2.pie(layout_counts.values, labels=layout_counts.index, autopct="%1.1f%%")
    st.pyplot(fig2)
