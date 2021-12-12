#Import Library yang dibutuhkan
#Import pandas sebagai analisis data (cleaning data, reading data, plotting, correlations dsb)
import pandas as pd
#Import Streamlit sebagai Platform aplikasi/framework
import streamlit as st
#Import datetime
from datetime import date
#Import Prophet -> fbprophet Machine Learning dari facebook untuk memprediksi data
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
#Import Plotly sebagai grafis data
from plotly import graph_objs as go

#Inisialisasi waktu awal dari data yang akan dibaca
START = "2004-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

#Judul Aplikasi
st.title('APLIKASI MEMPREDIKSI GARIS KEMISKINAN BERDASARKAN PENDAPATAN PERKAPITA WILAYAH INDONESIA')

#Item Box Datasets
datasets = (
    "Indonesia", "Aceh", "Bali", "Banten", "Bengkulu", "DI Yogyakarta", "DKI Jakarta", "Gorontalo", "Jambi", "Jawa Barat", 
    "Jawa Tengah", "Jawa Timur", "Kalimantan Barat", "Kalimantan Selatan", "Kalimantan Tengah", "Kalimantan Timur", 
    "Kep. Bangka Belitung", "Kep. Riau", "Lampung", "Maluku", "Maluku Utara", "Nusa Tenggara Barat", "Nusa Tenggara Timur", 
    "Papua", "Papua Barat", "Riau", "Sulawesi Barat", "Sulawesi Selatan", "Sulawesi Tengah", "Sulawesi Tenggara", 
    "Sulawesi Utara", "Sumatera Barat", "Sumatera Selatan", "Sumatera Utara")
selected_datasets = st.selectbox('Select dataset for prediction', datasets)

#Slider untuk memilih berapa tahun prediksi dimasa depan
n_years = st.slider('Years of prediction:', 1, 4)
period = n_years * 365

#Load data 'Garis_Kemiskinan_Clean.csv'
@st.cache
def load_data(ticker):
    data = pd.read_csv('Garis_Kemiskinan_Clean.csv')
    return data
	
data_load_state = st.text('Loading data...')
data = load_data(selected_datasets)
data_load_state.text('Loading data... done!')

#Menampilkan Raw Data/Data mentah yang belum diproses
st.subheader('Raw data')
st.write(data)

#Menampilkan Data spesifik
st.subheader(selected_datasets)

#Menghapus kolom satuan dan sumber serta memindahkan kolom tanggal kedepan
data = data.drop(columns=['Satuan', 'Sumber'])
first_column = data.pop('Tanggal')
data.insert(0, 'Tanggal', first_column)
data['Tanggal'] = pd.to_datetime(data.Tanggal)

#Pemilihan datasets
if selected_datasets=='Indonesia':
    i='Indonesia'
    data = data[['Tanggal',i]]
if selected_datasets=='Aceh':
    i='Aceh'
    data = data[['Tanggal',i]]
if selected_datasets=='Bali':
    i='Bali'
    data = data[['Tanggal',i]]
if selected_datasets=='Banten':
    i='Banten'
    data = data[['Tanggal',i]]
if selected_datasets=='Bengkulu':
    i='Bengkulu'
    data = data[['Tanggal',i]]
if selected_datasets=='DI Yogyakarta':
    i='DI Yogyakarta'
    data = data[['Tanggal',i]]
if selected_datasets=='DKI Jakarta':
    i='DKI Jakarta'
    data = data[['Tanggal',i]]
if selected_datasets=='Gorontalo':
    i='Gorontalo'
    data = data[['Tanggal',i]]
if selected_datasets=='Jambi':
    i='Jambi'
    data = data[['Tanggal',i]]
if selected_datasets=='Jawa Barat':
    i='Jawa Barat'
    data = data[['Tanggal',i]]
if selected_datasets=='Jawa Tengah':
    i='Jawa Tengah'
    data = data[['Tanggal',i]]
if selected_datasets=='Jawa Timur':
    i='Jawa Timur'
    data = data[['Tanggal',i]]
if selected_datasets=='Kalimantan Barat':
    i='Kalimantan Barat'
    data = data[['Tanggal',i]]
if selected_datasets=='Kalimantan Selatan':
    i='Kalimantan Selatan'
    data = data[['Tanggal',i]]
if selected_datasets=='Kalimantan Tengah':
    i='Kalimantan Tengah'
    data = data[['Tanggal',i]]
if selected_datasets=='Kalimantan Timur':
    i='Kalimantan Timur'
    data = data[['Tanggal',i]]
if selected_datasets=='Kep. Bangka Belitung':
    i='Kep. Bangka Belitung'
    data = data[['Tanggal',i]]
if selected_datasets=='Kep. Riau':
    i='Kep. Riau'
    data = data[['Tanggal',i]]
if selected_datasets=='Lampung':
    i='Lampung'
    data = data[['Tanggal',i]]
if selected_datasets=='Maluku':
    i='Maluku'
    data = data[['Tanggal',i]]
if selected_datasets=='Maluku Utara':
    i='Maluku Utara'
    data = data[['Tanggal',i]]
if selected_datasets=='Nusa Tenggara Barat':
    i='Nusa Tenggara Barat'
    data = data[['Tanggal',i]]
if selected_datasets=='Nusa Tenggara Timur':
    i='Nusa Tenggara Timur'
    data = data[['Tanggal',i]]
if selected_datasets=='Papua':
    i='Papua'
    data = data[['Tanggal',i]]
if selected_datasets=='Papua Barat':
    i='Papua Barat'
    data = data[['Tanggal',i]]
if selected_datasets=='Riau':
    i='Riau'
    data = data[['Tanggal',i]]
if selected_datasets=='Sulawesi Barat':
    i='Sulawesi Barat'
    data = data[['Tanggal',i]]
if selected_datasets=='Sulawesi Selatan':
    i='Sulawesi Selatan'
    data = data[['Tanggal',i]]
if selected_datasets=='Sulawesi Tengah':
    i='Sulawesi Tengah'
    data = data[['Tanggal',i]]
if selected_datasets=='Sulawesi Tenggara':
    i='Sulawesi Tenggara'
    data = data[['Tanggal',i]]
if selected_datasets=='Sulawesi Utara':
    i='Sulawesi Utara'
    data = data[['Tanggal',i]]
if selected_datasets=='Sumatera Barat':
    i='Sumatera Barat'
    data = data[['Tanggal',i]]
if selected_datasets=='Sumatera Selatan':
    i='Sumatera Selatan'
    data = data[['Tanggal',i]]
if selected_datasets=='Sumatera Utara':
    i='Sumatera Utara'
    data = data[['Tanggal',i]]

data

# Plotting raw data, Menampilkan chart grafis data mentah
def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Tanggal'], y=data[i], name="stock_open"))
	fig.layout.update(
        title_text='Time Series data with Rangeslider wilayah '+i,
        xaxis_title="Tahun",
        yaxis_title="Pendapatan Perkapita (Rp)", 
        xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
plot_raw_data()

# Prediksi forecast dengan Machine Learning Facebook (Prophet)
df_train = data[['Tanggal',i]]
df_train = df_train.rename(columns={"Tanggal": "ds", i: "y"})
m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Menampilkan Plot
st.subheader('Forecast data')
st.write(forecast)
    
st.write(f'Forecast plot untuk {n_years} tahun')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)
