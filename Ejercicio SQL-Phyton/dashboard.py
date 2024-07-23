import pandas as pd
from datetime import datetime
import streamlit as st
import altair as alt

# =============================================================================
# ------------------------------ Importar Datos -------------------------------
# =============================================================================
station_col_names = ['id', 'station', 'municipality', 'lat', 'lng']

station_df = pd.read_csv("data_stations.txt", names=station_col_names, header=None, delimiter=',', quotechar="'", on_bad_lines='skip')

trips_col_names = ['id', 'duration', 'start_date', 'start_station', 'end_date', 'end_station', 'bike_number', 'sub_type', 'zip_code', 'birth_date', 'gender']

trips_df = pd.read_csv('data_trips.txt', names=trips_col_names, header=None, delimiter=',', quotechar="'", on_bad_lines='skip')

# =============================================================================
# ------------------------------- Limpiar Datos -------------------------------
# =============================================================================
# Comprobar que los valores de 'sub_type' solo son 'Registered' y 'Casual'
trips_df['sub_type'].unique()

# Rellenar los valores Nan con 'Not Known'
trips_df['gender'] = trips_df['gender'].fillna('Not Known')

# Sustituir las entradas con valor 'Male ' por 'Male'
trips_df['gender'] = trips_df['gender'].replace('Male ', 'Male')

# Comprobar que los valores de 'gender' solo son 'Male' y 'Female'
trips_df['gender'].unique()

# Convertir fechas
trips_df['start_date'] = pd.to_datetime(trips_df['start_date'])
trips_df['end_date'] = pd.to_datetime(trips_df['end_date'])

# Eliminar bicicletas sin codigo
trips_df = trips_df[trips_df['bike_number'] != ' ']

# =============================================================================
# ----------------------------- Normalizar Datos ------------------------------
# =============================================================================
bikes_df = trips_df[['bike_number']].drop_duplicates().reset_index(drop=True)

people_df = trips_df[['zip_code', 'birth_date', 'gender']].drop_duplicates().reset_index(drop=True)

trips_df = trips_df.merge(people_df, on=['zip_code', 'birth_date', 'gender'], how='left', suffixes=('', '_people'))

trips_df = trips_df.merge(bikes_df, on='bike_number', how='left', suffixes=('', '_bike'))

# =============================================================================
# ------------------------------------- 1 -------------------------------------
# =============================================================================
mean_trip = trips_df['duration'].mean()

total_trips = trips_df['id'].count()

# =============================================================================
# ------------------------------------- 2 -------------------------------------
# =============================================================================
current_year = datetime.now().year

ages_df = trips_df[['birth_date', 'duration']]

ages_df = ages_df.dropna()
ages_df = ages_df[ages_df['birth_date'] > 0]
ages_df['age'] = current_year - ages_df['birth_date']
ages_df = ages_df.drop(columns=['birth_date'])

minutes_by_age = ages_df.groupby('age')['duration'].sum().reset_index()

# =============================================================================
# ------------------------------------- 3 -------------------------------------
# =============================================================================
real_trips = trips_df[trips_df['duration'] > 1]
real_trips_count = real_trips.groupby('bike_number')['id'].count()

# =============================================================================
# ------------------------------------- 4 -------------------------------------
# =============================================================================
bike_trip_counts = trips_df.groupby('bike_number')['id'].count()

obsolescence_df = bike_trip_counts.to_frame(name='num_trips').reset_index()
obsolescence_df['obsolescence'] = obsolescence_df['num_trips'] / 1800
obsolescence_df = obsolescence_df.drop(columns=['num_trips'])

# =============================================================================
# ------------------------------------- 5 -------------------------------------
# =============================================================================
bikes_trip_count = trips_df.groupby('bike_number')['id'].count().reset_index()
bikes_trip_count.columns = ['bike_number', 'num_trips']

# =============================================================================
# ------------------------------------- 6 -------------------------------------
# =============================================================================
null_trips = trips_df[trips_df['duration'] < 60]

null_trip_counts = null_trips.groupby('bike_number')['id'].count().reset_index()
null_trip_counts.columns = ['bike_number', 'num_null_trips']

top_10_null_trips = null_trip_counts.sort_values(by='num_null_trips', ascending=False).head(10)

# =============================================================================
# ------------------------------------- 7 -------------------------------------
# =============================================================================
bike_age_usage = trips_df[['id','birth_date', 'duration', 'bike_number']]

bike_age_usage = bike_age_usage.dropna()
bike_age_usage = bike_age_usage[bike_age_usage['birth_date'] > 0.0]
bike_age_usage['age'] = current_year - bike_age_usage['birth_date']
bike_age_usage = bike_age_usage.drop(columns=['birth_date'])

bike_age_usage = bike_age_usage.groupby(['age', 'bike_number'])['id'].count().reset_index()
bike_age_usage.columns = ['age', 'bike_number', 'num_trips']

most_used_bike_per_age = bike_age_usage.loc[bike_age_usage.groupby('age')['num_trips'].idxmax()]

# =============================================================================
# ------------------------------------- 8 -------------------------------------
# =============================================================================
trips_ge3 = trips_df[(trips_df['duration'] >= 3)]

trips_ge3_counts = trips_ge3.groupby('bike_number')['id'].count()

bikes_over_2000_trips = trips_ge3_counts[trips_ge3_counts > 2000].reset_index()
bikes_over_2000_trips.columns = ['bike_number', 'num_trips']

# =============================================================================
# ------------------------------------- 9 -------------------------------------
# =============================================================================
trips_per_year = trips_df[['id', 'start_date']]
trips_per_year['year'] = trips_per_year['start_date'].dt.year
trips_per_year['day_of_year'] = trips_per_year['start_date'].dt.day_of_year

trips_per_year = trips_per_year.groupby(['year', 'day_of_year']).count().reset_index()
trips_per_year = trips_per_year.drop(columns=['start_date'])
trips_per_year.columns = ['year', 'day_of_year', 'trips']

trips_per_month = trips_df[['id', 'start_date']]
trips_per_month['year'] = trips_per_month['start_date'].dt.year
trips_per_month['month'] = trips_per_month['start_date'].dt.month

trips_per_month = trips_per_month.groupby(['year', 'month']).count().reset_index()
trips_per_month = trips_per_month.drop(columns=['start_date'])
trips_per_month.columns = ['year', 'month', 'trips']

trips_per_day_of_week = trips_df.groupby(trips_df['start_date'].dt.day_name())['id'].count()

# =============================================================================

# =============================================================================
# --------------------------------- Dashboard ---------------------------------
# =============================================================================

total_real_trips = real_trips_count.sum()
total_registered_bikes = real_trips_count.count()

st.title('Análisis de Trayectos')

col0_1, col0_2, col0_3 = st.columns(3)
with col0_1:
	st.header('Duración media de los viajes')
	st.subheader(f"{mean_trip:.2f} minutos")

with col0_2:
	st.header('Nº total de trayectos')
	st.subheader(total_trips)

with col0_3:
	st.header('Edad promedio de los usuarios')
	st.subheader(f"{ages_df['age'].mean():.2f}")

col0_4, col0_5, col0_6 = st.columns(3)
with col0_4:
	st.header('Nº de bicicletas')
	st.subheader(real_trips_count.count())
with col0_5:
	st.header('Nº total de viajes reales')
	st.subheader(total_real_trips)
with col0_6:
	#porcenjae de obsolescencia
	st.header('Porcentaje de obsolescencia')
	st.subheader(f"{obsolescence_df['obsolescence'].mean()*100:.2f}%")

st.header('Minutos de bicicleta según edad del cliente')
st.bar_chart(minutes_by_age.set_index('age'))

col1, col2 = st.columns(2)
with col1:
	st.header('Bicicleta más usada según edades de los conductores')
	st.dataframe(most_used_bike_per_age)

with col2:
	st.header('Bicicletas con más de 2,000 viajes de al menos 3 minutos')
	st.dataframe(bikes_over_2000_trips)

col3, col4 = st.columns(2)
with col3:
	st.header('Bicicletas y número de viajes realizados')
	st.dataframe(bikes_trip_count)

with col4:
	st.header('Top 10 bicicletas con más viajes nulos')
	st.dataframe(top_10_null_trips)

st.header('Análisis temporal de los datos')
st.subheader('Viajes por año')

trips_per_year_chart = alt.Chart(trips_per_year).mark_line().encode(
	x=alt.X('day_of_year', title='Día del año'),
	y=alt.Y('trips', title='Número de viajes'),
	color='year:N'
).interactive()
st.altair_chart(trips_per_year_chart, use_container_width=True)

st.subheader('Viajes por mes')
trips_per_month_chart = alt.Chart(trips_per_month).mark_bar().encode(
	x=alt.X('month', title='Mes', scale=alt.Scale(domain=(1, 12))),
	y=alt.Y('trips', title='Número de viajes'),
	color='year:N'
).interactive()
st.altair_chart(trips_per_month_chart, use_container_width=True)

st.subheader('Viajes por día de la semana')
st.bar_chart(trips_per_day_of_week)

st.header('Obsolescencia del parque de bicicletas')
st.bar_chart(obsolescence_df['obsolescence'])