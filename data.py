import streamlit as st
import pandas as pd
import plotly.express as px

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

# def total_kasus():
#     df = load_data()
#     st.subheader("🦠 Total Kasus Covid-19🦠")
#     st.write(f"Total kasus dari kopit 19 {df["Total Cases"].sum()}")

def kolom_tertentu():
    df = load_data()
    st.subheader("Kolom tertentu")
    st.write(df.iloc[:, 2: 10])

def nama():
    st.markdown(
        "<p style='text-align: center;'>Charisa Martha / 184240003</p>",
        unsafe_allow_html=True
    )

# Total Kasus
# def total_case():
#     df = load_data()
#     total_kasus = df['New Cases'].sum()
#     return total_kasus

# def total_death():
#     df = load_data()
#     total_kematian = df['New Deaths'].sum()
#     return total_kematian

# def total_recovery ():
#     df = load_data()
#     total_sembuh = df['New Recovered'].sum()
#     return total_sembuh

# kolom 1
# def kolom() :
#     kasus = total_case()
#     kematian = total_death()
#     sembuh = total_recovery()

#     col1, col2, col3 = st.columns(3)
#     col1.metric(label="Total Kasus 📈", value=kasus, border=True)
#     col2.metric(label="Total Kematian 💀", value=kematian, border=True)
#     col3.metric(label="Total Sembuh ❤️‍🩹", value=sembuh, border=True)

# filter
def filter_data(df, year=None):
    if year:
        df = df[df['Date'].astype(str).str.contains(str(year))]
    return df

def select_year():
    return st.sidebar.selectbox(
        "Pilih Tahun 📆",
        options=["Semua Tahun", 2020, 2021, 2022],
        format_func=lambda x: str(x)
    )

def show_data(df):
    selected_columns = [
        'Location',
        'New Cases',
        'New Deaths',
        'New Recovered',
        'Total Cases',
        'Total Deaths',
        'Total Recovered'
    ]

    df_selected = df[selected_columns]
    st.subheader("Data Covid-19 Indonesia")
    st.dataframe(df_selected.head(10))

def total_case(df):
    total_kasus = df['Total Cases'].sum()
    return total_kasus

def total_death(df):
    total_mati = df['Total Deaths'].sum()
    return total_mati

def total_recovery(df):
    total_sembuh = df['Total Recovered'].sum()
    return total_sembuh

def kolom(df) :
    kasus = total_case(df)
    kematian = total_death(df)
    sembuh = total_recovery(df)

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Total Kasus 📈", value=kasus, border=True)
    col2.metric(label="Total Kematian 💀", value=kematian, border=True)
    col3.metric(label="Total Sembuh ❤️‍🩹", value=sembuh, border=True)

# pie chart
def pie_chart(df):
    total_matii = total_death(df)
    total_sembuh = total_recovery(df)

    # dataframe
    data ={
        'Status' : ['Meninggal', 'Sembuh'],
        'Jumlah' : [total_matii, total_sembuh]
    }

    fig = px.pie(
        data,
        names='Status',
        values='Jumlah',
        title='Perbandingan Total Kematian Vs Total Kesembuhan',
        hole=0.5,
        color_discrete_sequence=['#4de89f', '#ff6459']
    )

    st.plotly_chart(fig, use_container_width=True)