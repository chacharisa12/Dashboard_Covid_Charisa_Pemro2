import streamlit as st
from data import kolom, select_year, load_data, filter_data, show_data, kolom_tertentu, nama, pie_chart

# judul dashboard
def judul():
    st.title("📊 Dashboard COVID-19")
    st.write("Selamat datang di dashboard interaktif untuk menganalisis data COVID-19 di Indonesia")

st.sidebar.title("Navigation")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman Data"])
if menu == "Home":
    judul()
    # pilih tahun
    year = select_year()
    # load & filter data
    df = load_data()
    df_filtered = filter_data(df, year)
    kolom(df_filtered)
    pie_chart(df_filtered)
elif menu == "Halaman Data":
    judul()
    year = select_year()
    df = load_data()
    df_filtered = filter_data(df, year)
    show_data(df_filtered)
    kolom_tertentu()
    nama()