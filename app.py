import streamlit as st
from data import kolom, select_year, load_data, filter_data, show_data, kolom_tertentu, nama, pie_chart, select_location, bar_chart1, bar_chart2, map_chart

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
    # location1 = select_location1(df)
    # df_filtered = filter_data1(df, year)

    location = select_location(df)
    df_filtered = filter_data(df, year, location)
    kolom(df_filtered)
    pie_chart(df_filtered)
    bar_chart1(df_filtered)
    bar_chart2(df_filtered)
    map_chart(df_filtered)
elif menu == "Halaman Data":
    judul()
    year = select_year()
    df = load_data()
    df_filtered = filter_data(df, year)
    show_data(df_filtered)
    kolom_tertentu()
    nama()