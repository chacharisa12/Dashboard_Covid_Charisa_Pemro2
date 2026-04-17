import streamlit as st
from data import*

# judul dashboard
def judul():
    st.title("📊 Dashboard COVID-19")
    st.write("Selamat datang di dashboard interaktif untuk menganalisis data COVID-19 di Indonesia")

st.sidebar.title("Navigation")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman Data"])
if menu == "Home":
    judul()
elif menu == "Halaman Data":
    judul()
    show_data()
    total_kasus()
    kolom_tertentu()
    nama()