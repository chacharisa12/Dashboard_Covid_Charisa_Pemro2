import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_tags import st_tags_sidebar

# dfungsi 
def load_data():
    df = pd.read_csv('covid_19_indonesia_time_series_all.csv')
    df = df[df["Location"] != "Indonesia"]
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

# filter lokasi
# def filter_data1(df, year=None, location=None):
#     if year and year != "Semua Tahun":
#         df = df[df["Date"].dt.year == int(year)]
#     if location and location != "Semua Provinsi":
#         df = df[df["Location"] == location]
#     return df

# def select_location1(df):
#     locations = ["Semua Provinsi"] + sorted (df['Location'].unique())
#     return st.sidebar.selectbox(
#         "Pilih Provinsi 📍",
#         options= locations
#     )

# FILTER LOKASI MULTISELECT
def filter_data(df, year=None, location=None):

    if year != "Semua Tahun":
        df = df[df["Date"].dt.year == int(year)]

    if location:
        df = df[df["Location"].isin(location)]

    return df

# PILIH PROVINSI
def select_location(df):
    locations = sorted(df["Location"].unique())

    selected = st_tags_sidebar(
        label="Pilih Provinsi 📍",
        text="Tekan enter setelah pilih",
        value=[],
        suggestions=locations,
        maxtags=34,
        key="1"
    )

    return selected

# filter
# def filter_data(df, year=None):
#     if year != "Semua Tahun":
#         df = df[df['Date'].astype(str).str.contains(str(year))]
#     return df

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
    latest = df.sort_values("Date").groupby("Location", as_index=False).last()
    return latest["Total Cases"].sum()

def total_death(df):
    latest = df.sort_values("Date").groupby("Location", as_index=False).last()
    return latest["Total Deaths"].sum()  

def total_recovery(df):
    latest = df.sort_values("Date").groupby("Location", as_index=False).last()
    return latest["Total Recovered"].sum() 

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

# barchart kematian terbanyak
def bar_chart1(df):
    df_last = df.sort_values('Date').groupby('Location', as_index=False).last()

    top5 = df_last.nlargest(5, 'Total Deaths')

    fig = px.bar(
        top5,
        x='Location',
        y='Total Deaths',
        color='Total Deaths',
        color_continuous_scale='Reds',
        title='5 Provinsi dengan Kematian Tertinggi',
        labels={'Total Deaths': 'Total Kematian', 'Location': 'Provinsi'}
    )

    fig.update_layout(xaxis_title='Provinsi', yaxis_title='Total Kematian', title_x=0.5)

    st.plotly_chart(fig, use_container_width=True)

# bar dengan kesembuhan terbanyak
def bar_chart2(df):
    df_last = df.sort_values('Date').groupby('Location', as_index=False).last()

    top5 = df_last.nlargest(5, 'Total Recovered')

    fig = px.bar(
        top5,
        x='Location',
        y='Total Recovered',
        color='Total Recovered',
        color_continuous_scale='greens',
        title='5 Provinsi dengan Kesembuhan Tertinggi',
        labels={'Total Recovered': 'Total Kesembuhan', 'Location': 'Provinsi'}
    )

    fig.update_layout(xaxis_title='Provinsi', yaxis_title='Total Kesembuhan', title_x=0.5)

    st.plotly_chart(fig, use_container_width=True)

# map chart
def map_chart(df, year=None):
    df['Date'] = pd.to_datetime(df['Date'])

    if year:
        df = df[df['Date'].dt.year == year]

    df_agg = df.groupby(['Location', 'Latitude', 'Longitude'], as_index=False) ['New Cases'].sum()
    df_map = df_agg.dropna(subset=['Latitude', 'Longitude', 'New Cases'])

    if df_map.empty:
        st.info("Tidak ada data")
        return
    
    fig = px.scatter_mapbox(
        df_map,
        lat="Latitude",
        lon='Longitude',
        size='New Cases',
        color='New Cases',
        hover_name='Location',
        zoom=3,
        center={'lat':-2.5, "lon": 118},
        size_max=20,
        opacity=0.7,
        color_continuous_scale='OrRd',
        title=f"Sebaran Kasus Baru Covid-19 di Indonesia ({year if year else 'Semua Tahun'})"
    )

    fig.update_layout(
        mapbox_style="carto-positron",
        height=600,
        margin={"r":0, "t":0, "l":0, "b":0}
    )

    st.plotly_chart(fig, use_container_width=True)