import streamlit as st
import pandas as pd

# dfungsi 
def load_data():
    df = pd.read_csv('dataset\covid_19_indonesia_time_series_all.csv')
    return df

# menampilkan data dalam tabel
def show_data():
    df = load_data()
    st.subheader("🦠 Data Kasus Covid 19🦠")
    st.dataframe(df.head(10))

    st.subheader("📊 Statistika Deskriptif Dataset")
    st.write(df.describe())

def total_kasus():
    df = load_data()
    st.subheader("🦠 Total Kasus Covid-19🦠")
    st.write(f"Total kasus dari kopit 19 {df["Total Cases"].sum()}")

def kolom_tertentu():
    df = load_data()
    st.subheader("Kolom tertentu")
    st.write(df.iloc[:, 2: 10])

def nama():
    st.markdown(
        "<p style='text-align: center;'>Charisa Martha / 184240003</p>",
        unsafe_allow_html=True
    )