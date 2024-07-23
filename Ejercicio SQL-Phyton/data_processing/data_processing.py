import pandas as pd
from datetime import datetime
import streamlit as st
import altair as alt

# =============================================================================
# ------------------------------ Importar Datos -------------------------------
# =============================================================================
station_col_names = ['id', 'station', 'municipality', 'lat', 'lng']

station_df = pd.read_csv("data_stations.txt", names=station_col_names, header=None, delimiter=',', quotechar="'", on_bad_lines='skip')
station_df

trips_col_names = ['id', 'duration', 'start_date', 'start_station', 'end_date', 'end_station', 'bike_number', 'sub_type', 'zip_code', 'birth_date', 'gender']

trips_df = pd.read_csv('data_trips.txt', names=trips_col_names, header=None, delimiter=',', quotechar="'", on_bad_lines='skip')
trips_df

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
bikes_df

people_df = trips_df[['zip_code', 'birth_date', 'gender']].drop_duplicates().reset_index(drop=True)
people_df

trips_df = trips_df.merge(people_df, on=['zip_code', 'birth_date', 'gender'], how='left', suffixes=('', '_people'))
trips_df

trips_df = trips_df.merge(bikes_df, on='bike_number', how='left', suffixes=('', '_bike'))
trips_df

# =============================================================================
# -----------------------------------------------------------------------------
# =============================================================================

# =============================================================================
# --------------------------------- Métricas ----------------------------------
# 1. ¿Cual es la media de la duración de los viajes? ¿ Numero total de trayectos ?
# 2. Minutos de bicileta segun edad del cliente
# 3. Y si tienes en cuenta sólo los viajes reales (supongamos que son los que duran más de 1
# 	minuto) ¿Cuántas bicicletas hay registradas?
# 4. Distribucion del grado de obsolescencia del parque de bicicletas , considerando que la
# 	vida util es de 1.800 viajes
# 5. ¿Puedes mostrarme una tabla con las bicicletas y el número de viajes que han realizado?
# 6. ¿Puedes mostrarme una tabla con las 10 bicicletas con más viajes nulos realizados (los de
# 	menos de 60 segundos?
# 7. ¿Cual es la bicicleta que más se ha usado segun las edades de los conductores?
# 8. ¿Qué bicicletas han sido usadas en más de 2.000 viajes de al menos 3 minutos?
# 9. Análisis temporal de los datos
# =============================================================================


# =============================================================================
# ------------------------------------- 1 -------------------------------------
# =============================================================================
mean_trip = trips_df['duration'].mean()
print("Duración media (minutos):", mean_trip)

total_trips = trips_df['id'].count()
print("Número total de trayectos:", total_trips)

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
minutes_by_age

# =============================================================================
# ------------------------------------- 3 -------------------------------------
# =============================================================================
real_trips = trips_df[trips_df['duration'] > 1]
real_trips_count = real_trips.groupby('bike_number')['id'].count()
print('Viajes totales reales:', real_trips_count.sum())
print('Bicicletas totales registradas:', real_trips_count.count())

# =============================================================================
# ------------------------------------- 4 -------------------------------------
# =============================================================================
bike_trip_counts = trips_df.groupby('bike_number')['id'].count()

obsolescence_df = bike_trip_counts.to_frame(name='num_trips').reset_index()
obsolescence_df['obsolescence'] = obsolescence_df['num_trips'] / 1800
obsolescence_df = obsolescence_df.drop(columns=['num_trips'])

obsolescence_df['obsolescence'].describe()

# =============================================================================
# ------------------------------------- 5 -------------------------------------
# =============================================================================
bikes_trip_count = trips_df.groupby('bike_number')['id'].count().reset_index()
bikes_trip_count.columns = ['bike_number', 'num_trips']
bikes_trip_count

# =============================================================================
# ------------------------------------- 6 -------------------------------------
# =============================================================================
null_trips = trips_df[trips_df['duration'] < 60]

null_trip_counts = null_trips.groupby('bike_number')['id'].count().reset_index()
null_trip_counts.columns = ['bike_number', 'num_null_trips']

top_10_null_trips = null_trip_counts.sort_values(by='num_null_trips', ascending=False).head(10)
top_10_null_trips

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
most_used_bike_per_age

# =============================================================================
# ------------------------------------- 8 -------------------------------------
# =============================================================================
trips_ge3 = trips_df[(trips_df['duration'] >= 3)]

trips_ge3_counts = trips_ge3.groupby('bike_number')['id'].count()

bikes_over_2000_trips = trips_ge3_counts[trips_ge3_counts > 2000].reset_index()
bikes_over_2000_trips.columns = ['bike_number', 'num_trips']

bikes_over_2000_trips

# =============================================================================
# ------------------------------------- 9 -------------------------------------
# =============================================================================
trips_per_year = trips_df[['id', 'start_date']]
trips_per_year['year'] = trips_per_year['start_date'].dt.year
trips_per_year['day_of_year'] = trips_per_year['start_date'].dt.day_of_year

trips_per_year = trips_per_year.groupby(['year', 'day_of_year']).count().reset_index()
trips_per_year = trips_per_year.drop(columns=['start_date'])
trips_per_year.columns = ['year', 'day_of_year', 'trips']
trips_per_year

trips_per_month = trips_df[['id', 'start_date']]
trips_per_month['year'] = trips_per_month['start_date'].dt.year
trips_per_month['month'] = trips_per_month['start_date'].dt.month

trips_per_month = trips_per_month.groupby(['year', 'month']).count().reset_index()
trips_per_month = trips_per_month.drop(columns=['start_date'])
trips_per_month.columns = ['year', 'month', 'trips']
trips_per_month

trips_per_day_of_week = trips_df.groupby(trips_df['start_date'].dt.day_name())['id'].count()
trips_per_day_of_week

# =============================================================================