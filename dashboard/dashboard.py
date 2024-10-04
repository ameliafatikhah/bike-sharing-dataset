import streamlit as st
import pandas as pd
import plotly.graph_objects as go  
import plotly.express as px
import types

@st.cache_data(hash_funcs={types.FunctionType: id})
def load_data():
    day_url = 'https://raw.githubusercontent.com/ameliafatikhah/bike-sharing-dataset/refs/heads/main/bike-sharing-dataset/day.csv'
    df_day = pd.read_csv(day_url)
    return df_day

df_day = load_data()

st.title("Bike Share Dashboard")

st.sidebar.title("Biodata:")
st.sidebar.markdown("**• Nama: Amelia Fatikhah**")
st.sidebar.markdown("**• ID Bangkit:  m180b4kx0459**")

st.sidebar.title("Dataset Bike Share")
if st.sidebar.checkbox("Tampilkan Dataset"):
    st.subheader("Raw Dataset")
    st.write(df_day)

if st.sidebar.checkbox("Tampilkan Ringkasan Parameter Statistik"):
    st.subheader("Ringkasan Statistik")
    st.write(df_day.describe())

st.sidebar.title("Pilihan Visualisasi")
visualization_option = st.sidebar.radio("Pilih visualisasi:", ["Penggunaan Sepeda Berdasarkan Musim Tahun 2011 & 2012",
                                                               "Penggunaan Sepeda Berdasarkan Cuaca Tahun 2011 & 2012"])

season = {1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'}
df_day['season'] = df_day['season'].map(season)

weather = {1:'Cuaca Cerah', 2:'Cuaca Mendung', 3:'Cuaca Bersalju', 4:'Cuaca Hujan'}
df_day['weathersit'] = df_day['weathersit'].map(weather)

if visualization_option == "Penggunaan Sepeda Berdasarkan Musim Tahun 2011 & 2012":
    st.header("Grafik Pie Penyewaan Sepeda Berdasarkan Musim")
    df_2011 = df_day[df_day['yr'] == 0]
    df_2012 = df_day[df_day['yr'] == 1]
    
    figure_2011 = px.pie(df_2011, values='cnt', names='season', title='Jumlah Penyewaan Sepeda Berdasarkan Musim (2011)')
    figure_2011.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(figure_2011)  # Use st.plotly_chart

    figure_2012 = px.pie(df_2012, values='cnt', names='season', title='Jumlah Penyewaan Sepeda Berdasarkan Musim (2012)')
    figure_2012.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(figure_2012)  # Use st.plotly_chart

elif visualization_option == "Penggunaan Sepeda Berdasarkan Cuaca Tahun 2011 & 2012":
    st.header("Grafik Penyewaan Sepeda Berdasarkan Cuaca")
    df_2011 = df_day[df_day['yr'] == 0]
    df_2012 = df_day[df_day['yr'] == 1]
    
    figure_weather_2011 = px.pie(df_2011, values='cnt', names='weathersit', title='Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca (2011)')
    figure_weather_2011.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(figure_weather_2011) 
    
    figure_weather_2012 = px.pie(df_2012, values='cnt', names='weathersit', title='Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca (2012)')
    figure_weather_2012.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(figure_weather_2012)  