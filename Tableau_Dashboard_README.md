# Tableau Dashboard – Mumbai & Delhi Weather Analysis  

This project showcases a complete end-to-end weather analytics workflow — from fetching real-time Open-Meteo weather data to processing, transforming, and visualizing it using a professional Tableau-style dashboard .

It compares Mumbai and Delhi using temperature, windspeed, wind direction, and weather condition metrics.  
This project highlights strong data analysis, ETL logic, dashboard design, and storytelling skills.

---

#  Weather Comparison Dashboard

Below is the exact Tableau-style dashboard created for this project:

Tableau_dashboard.png

---

#  Project Overview  

This project includes:  
- ✔ Weather data extraction (Open-Meteo API)  
- ✔ Data formatting** into a clean, analysis-ready table  
- ✔ Multi-city comparison** (Mumbai vs Delhi)  
- ✔ Tableau dashboard creation  
- ✔ End-to-end documentation

This is ideal for:  
- Data Analyst portfolios  
- Interview demonstration  
- Tableau visualization practice  
- Real-world weather analytics projects  

---

# Database Schema  

Weather data is stored using the following structure:

```sql
CREATE TABLE IF NOT EXISTS weather_data (
    latitude FLOAT,
    longitude FLOAT,
    temperature FLOAT,
    windspeed FLOAT,
    winddirection FLOAT,
    weathercode INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# Sample Weather Dataset (10 Days – Combined)

| Date       | City    | Latitude | Longitude | Temperature | Windspeed | WindDirection | WeatherCode |
|------------|---------|----------|-----------|-------------|-----------|----------------|--------------|
| 2025-11-15 | Mumbai  | 19.0760  | 72.8777   | 29.5        | 12.2      | 210            | 1            |
| 2025-11-15 | Delhi   | 28.7041  | 77.1025   | 21.4        | 8.9       | 320            | 0            |
| 2025-11-16 | Mumbai  | 19.0760  | 72.8777   | 29.1        | 14.0      | 205            | 0            |
| 2025-11-16 | Delhi   | 28.7041  | 77.1025   | 21.0        | 9.5       | 315            | 1            |
| 2025-11-17 | Mumbai  | 19.0760  | 72.8777   | 30.0        | 11.8      | 215            | 1            |
| 2025-11-17 | Delhi   | 28.7041  | 77.1025   | 20.7        | 7.8       | 330            | 0            |

---

# 📈 Dashboard Highlights  

## Key Metrics (KPIs)
- Average Temperature – Mumbai  
- Average Temperature – Delhi  
- Average Windspeed  
- Maximum Temperature  
- Dominant Wind Direction  

## Visualizations Included
- Temperature Over Time (Line Chart)  
- Weather Code Heatmap
- Average Temperature (Bar Chart) 
- Average Windspeed (Bar Chart)
- Wind Direction Polar View

This dashboard provides clear insights into how Mumbai and Delhi differ across multiple weather dimensions.
