# Data-Pipeline-with-Apache-Airflow
Built an automated ETL pipeline to extract live weather data from APIs, transform it, and load it into structured storage for analysis.

# 🌦️ Live Weather Data — Mumbai & Delhi

| Date       | Latitude | Longitude | Temperature (°C) | Windspeed (km/h) | Wind Direction (°) | Weather Code |
|------------|----------|-----------|------------------|------------------|--------------------|--------------|
| 2025-11-15 | 19.0760  | 72.8777   | 29.5             | 12.2             | 210                | 1            |
| 2025-11-16 | 19.0760  | 72.8777   | 29.1             | 14.0             | 205                | 0            |
| 2025-11-17 | 19.0760  | 72.8777   | 30.0             | 11.8             | 215                | 1            |
| 2025-11-18 | 19.0760  | 72.8777   | 30.4             | 13.5             | 220                | 2            |
| 2025-11-19 | 19.0760  | 72.8777   | 29.8             | 10.9             | 200                | 3            |
| 2025-11-20 | 19.0760  | 72.8777   | 29.2             | 12.7             | 195                | 1            |
| 2025-11-21 | 19.0760  | 72.8777   | 29.7             | 11.0             | 210                | 0            |
| 2025-11-22 | 19.0760  | 72.8777   | 30.1             | 13.3             | 218                | 1            |
| 2025-11-23 | 19.0760  | 72.8777   | 30.3             | 12.5             | 225                | 2            |
| 2025-11-24 | 19.0760  | 72.8777   | 30.0             | 11.8             | 215                | 0            |
| 2025-11-15 | 28.7041  | 77.1025   | 21.4             | 8.9              | 320                | 0            |
| 2025-11-16 | 28.7041  | 77.1025   | 21.0             | 9.5              | 315                | 1            |
| 2025-11-17 | 28.7041  | 77.1025   | 20.7             | 7.8              | 330                | 0            |
| 2025-11-18 | 28.7041  | 77.1025   | 20.4             | 8.2              | 335                | 1            |
| 2025-11-19 | 28.7041  | 77.1025   | 20.1             | 7.5              | 340                | 2            |
| 2025-11-20 | 28.7041  | 77.1025   | 19.8             | 8.0              | 345                | 0            |
| 2025-11-21 | 28.7041  | 77.1025   | 19.5             | 9.1              | 350                | 1            |
| 2025-11-22 | 28.7041  | 77.1025   | 19.2             | 8.7              | 355                | 0            |
| 2025-11-23 | 28.7041  | 77.1025   | 19.0             | 8.3              | 5                  | 1            |
| 2025-11-24 | 28.7041  | 77.1025   | 18.7             | 7.9              | 10                 | 0            |


Data Cleaning

Before loading the dataset into SQL or Tableau, the following cleaning steps were performed:

1) Remove Missing Values

Check for null values in key columns:

SELECT *
FROM weather_data
WHERE temperature IS NULL
   OR windspeed IS NULL
   OR winddirection IS NULL
   OR weathercode IS NULL;


If any appear, drop or fill:

DELETE FROM weather_data
WHERE temperature IS NULL;

2) Ensure Correct Data Types
ALTER TABLE weather_data
MODIFY latitude FLOAT,
MODIFY longitude FLOAT,
MODIFY temperature FLOAT,
MODIFY windspeed FLOAT,
MODIFY winddirection FLOAT,
MODIFY weathercode INT;

3) Remove Duplicate Records

Weather data may repeat for the same timestamp:

DELETE t1 FROM weather_data t1
INNER JOIN weather_data t2
WHERE 
    t1.timestamp > t2.timestamp
    AND t1.latitude = t2.latitude
    AND t1.longitude = t2.longitude;



Basic SQL Queries for Analysis
1) Get Average Temperature by City
SELECT city, AVG(temperature) AS avg_temperature
FROM weather_data
GROUP BY city;

2) Maximum and Minimum Temperature
SELECT 
    MAX(temperature) AS max_temp,
    MIN(temperature) AS min_temp
FROM weather_data;

3) Fetch Data for a Specific Date
SELECT *
FROM weather_data
WHERE date = '2025-11-15';

4) Compare Windspeed Between Cities
SELECT city, AVG(windspeed) AS avg_windspeed
FROM weather_data
GROUP BY city;

5) Trend Analysis – Temperature Over Time
SELECT date, city, temperature
FROM weather_data
ORDER BY date ASC;
