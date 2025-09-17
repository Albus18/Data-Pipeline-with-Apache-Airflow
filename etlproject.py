from airflow import DAG
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.decorators import task
from datetime import datetime

LATITUDE = '51.5074'
LONGITUDE = '-0.1278'

MYSQL_CONN_ID = 'mysql_default123'
API_CONN_ID = 'open_meteo_api'

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 9, 14),
}


with DAG(
    dag_id='weather_etl_pipeline_mysql',
    default_args=default_args,
    schedule_interval='@daily',  # use schedule_interval instead of schedule
    catchup=False
) as dag:

    @task()
    def extract_weather_data():
        http_hook = HttpHook(http_conn_id=API_CONN_ID, method='GET')
        endpoint = f'/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&current_weather=true'
        response = http_hook.run(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch weather data: {response.status_code}")

    @task()
    def transform_weather_data(weather_data):
        current_weather = weather_data['current_weather']
        return {
            'latitude': float(LATITUDE),
            'longitude': float(LONGITUDE),
            'temperature': current_weather['temperature'],
            'windspeed': current_weather['windspeed'],
            'winddirection': current_weather['winddirection'],
            'weathercode': current_weather['weathercode']
        }

    @task()
    def load_weather_data(transformed):
        mysql_hook = MySqlHook(mysql_conn_id=MYSQL_CONN_ID)
        mysql_hook.run("""
            CREATE TABLE IF NOT EXISTS weather_data (
                latitude FLOAT,
                longitude FLOAT,
                temperature FLOAT,
                windspeed FLOAT,
                winddirection FLOAT,
                weathercode INT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        mysql_hook.run(
            """
            INSERT INTO weather_data 
            (latitude, longitude, temperature, windspeed, winddirection, weathercode)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            parameters=(
                transformed['latitude'],
                transformed['longitude'],
                transformed['temperature'],
                transformed['windspeed'],
                transformed['winddirection'],
                transformed['weathercode']
            )
        )

    weather = extract_weather_data()
    transformed = transform_weather_data(weather)
    load_weather_data(transformed)
