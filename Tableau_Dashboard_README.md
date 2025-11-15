# 📊 Tableau Dashboard – Mumbai & Delhi Weather Analysis  

This project showcases a complete end-to-end weather analytics workflow — from fetching real-time Open-Meteo weather data to processing, transforming, and visualizing it using a **professional Tableau-style dashboard**.

It compares **Mumbai** and **Delhi** over a 10-day period using temperature, windspeed, wind direction, and weather condition metrics.  
This project highlights strong data analysis, ETL logic, dashboard design, and storytelling skills.

---

# 🌦️ Weather Comparison Dashboard

Below is the exact Tableau-style dashboard created for this project:

![Weather Dashboard](Tableau_dashboard.png)

> Replace `Tableau_dashboard.png` with the actual file name after uploading the image to your repository.

---

# ⭐ Project Overview  

This project includes:  
- ✔ **Weather data extraction** (Open-Meteo API)  
- ✔ **Data formatting** into a clean, analysis-ready table  
- ✔ **Multi-city comparison** (Mumbai vs Delhi)  
- ✔ **Tableau dashboard creation**  
- ✔ **End-to-end documentation**  

This is ideal for:  
- Data Analyst portfolios  
- Interview demonstration  
- Tableau visualization practice  
- Real-world weather analytics projects  

---

# 🧱 Database Schema  

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

# 📊 Sample Weather Dataset (10 Days – Combined)

| Date       | City    | Latitude | Longitude | Temperature | Windspeed | WindDirection | WeatherCode |
|------------|---------|----------|-----------|-------------|-----------|----------------|--------------|
| 2025-11-15 | Mumbai  | 19.0760  | 72.8777   | 29.5        | 12.2      | 210            | 1            |
| 2025-11-15 | Delhi   | 28.7041  | 77.1025   | 21.4        | 8.9       | 320            | 0            |
| 2025-11-16 | Mumbai  | 19.0760  | 72.8777   | 29.1        | 14.0      | 205            | 0            |
| 2025-11-16 | Delhi   | 28.7041  | 77.1025   | 21.0        | 9.5       | 315            | 1            |
| 2025-11-17 | Mumbai  | 19.0760  | 72.8777   | 30.0        | 11.8      | 215            | 1            |
| 2025-11-17 | Delhi   | 28.7041  | 77.1025   | 20.7        | 7.8       | 330            | 0            |

*(table continues…)*

---

# 📈 Dashboard Highlights  

## 🔹 Key Metrics (KPIs)
- Average Temperature – Mumbai  
- Average Temperature – Delhi  
- Average Windspeed  
- Maximum Temperature  
- Dominant Wind Direction  

## 🔹 Visualizations Included
- 📉 **Temperature Over Time** (Line Chart)  
- 📚 **Weather Code Heatmap**  
- 📊 **Average Temperature (Bar Chart)**  
- 🌬 **Average Windspeed (Bar Chart)**  
- 🧭 **Wind Direction Polar View**  

This dashboard provides clear insights into how Mumbai and Delhi differ across multiple weather dimensions.

---

# 🛠 How to Run the Project

### 1️⃣ Install required libraries  
```bash
pip install requests pandas
```

### 2️⃣ Run your data extraction script  
```bash
python weather_fetch.py
```

### 3️⃣ Export dataset  
Convert the processed data to a CSV file:
```
weather_data.csv
```

### 4️⃣ Build the Tableau Dashboard  
- Open Tableau  
- Import `weather_data.csv`  
- Recreate visuals using the layout shown above  

---

# 🎯 Why This Project Is Impressive  
This project demonstrates real, job-ready skills:

- End-to-end data handling  
- Clean data modeling  
- Effective visualization choices  
- Multi-city comparison logic  
- Beautiful dashboard design  
- Great documentation  

Perfect for resumes, GitHub portfolios, and interviews.

---

# 🚀 Future Enhancements  
- Add more cities (Chennai, Bangalore, Kolkata)  
- Add humidity, precipitation, pressure metrics  
- Use Airflow to automate hourly data extraction  
- Publish dashboard online (Tableau Public)  
- Build a Streamlit weather analytics web app  

---

# 👨‍💻 Author  
**Ayush Lakra**  
Aspiring Data Analyst • Python | Tableau | SQL

If this project helped or inspired you, please ⭐ star the repository!
