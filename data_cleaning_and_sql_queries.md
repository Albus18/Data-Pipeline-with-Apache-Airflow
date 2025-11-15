# 🌦️ Weather Data Cleaning & SQL Queries

## 📌 Data Cleaning

### 1) Remove Missing Values

```sql
SELECT *
FROM weather_data
WHERE temperature IS NULL
   OR windspeed IS NULL
   OR winddirection IS NULL
   OR weathercode IS NULL;
```

```sql
DELETE FROM weather_data
WHERE temperature IS NULL;
```

### 2) Ensure Correct Data Types

```sql
ALTER TABLE weather_data
MODIFY latitude FLOAT,
MODIFY longitude FLOAT,
MODIFY temperature FLOAT,
MODIFY windspeed FLOAT,
MODIFY winddirection FLOAT,
MODIFY weathercode INT;
```

### 3) Remove Duplicate Records

```sql
DELETE t1
FROM weather_data t1
INNER JOIN weather_data t2
  ON t1.latitude = t2.latitude
 AND t1.longitude = t2.longitude
 AND t1.timestamp > t2.timestamp;
```

## 📊 SQL Queries for Analysis

### 1) Average Temperature by City

```sql
SELECT city, AVG(temperature) AS avg_temperature
FROM weather_data
GROUP BY city;
```

### 2) Maximum and Minimum Temperature

```sql
SELECT 
    MAX(temperature) AS max_temperature,
    MIN(temperature) AS min_temperature
FROM weather_data;
```

### 3) Fetch Weather Data for a Specific Date

```sql
SELECT *
FROM weather_data
WHERE date = '2025-11-15';
```

### 4) Compare Average Windspeed Across Cities

```sql
SELECT city, AVG(windspeed) AS avg_windspeed
FROM weather_data
GROUP BY city;
```

### 5) Temperature Trend Over Time

```sql
SELECT date, city, temperature
FROM weather_data
ORDER BY date ASC;
```
