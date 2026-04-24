# WindBorne Systems — Sensors Intern Application  
**Candidate:** Abhishek Patil  

---

## Engineering Summary

This project is an Atmospheric Intelligence Hub that integrates real-world air quality sensor data (EPA AQS) with meteorological data (ERA5) to analyze, validate, and understand atmospheric behavior.

The system mimics a real-world sensing pipeline by transforming raw environmental measurements into reliable insights through:
- Data fusion
- Temporal alignment
- Quality control
- Multi-scale analysis

---

## Why This is Relevant to Sensor Systems

Although this project is software-based, it directly works on real atmospheric sensor data.

Each EPA AQS station acts as a physical sensor node measuring pollutants such as PM2.5, NO₂, and O₃.

This system focuses on:
- Sensor data alignment (timestamp synchronization)
- Handling missing data (sensor outages)
- Cross-validation across nearby stations
- Environmental effects on sensor readings
- Reliability and consistency of measurements

These are core challenges in real-world atmospheric sensing systems.

---

## System Flow
EPA AQS Sensors + ERA5 Weather Data
↓
Data Alignment & Cleaning
↓
Sensor-Level Analysis
↓
Interactive Dashboard
↓
Insights & Forecasting

---

## Key Component: Time-Aligned Data Fusion Layer

### Operating Principle

EPA AQS and ERA5 datasets originate from different systems and must be aligned before analysis.

This component:
1. Converts timestamps into a unified hourly format  
2. Matches pollutant data with meteorological conditions  
3. Preserves station-level granularity  
4. Handles missing values  
5. Produces a unified atmospheric dataset  

### Why It Matters

Incorrect alignment leads to misleading conclusions.

This is similar to real sensor pipelines where:
- Time synchronization is critical  
- Measurement context determines accuracy  
- Misalignment introduces systematic errors  

---

## Physical Sensor Insight: PM2.5 Measurement

PM2.5 sensors typically operate using light scattering:

- A light source emits a beam  
- Air with particles passes through  
- Particles scatter light  
- A photodetector measures intensity  
- Signal converts to concentration  

### Practical Challenges

- Humidity affects readings  
- Particle composition varies  
- Calibration is required  
- Sensor drift over time  

In this project, EPA AQS data represents processed outputs from such sensors, allowing analysis of:
- Station reliability  
- Measurement consistency  
- Environmental influence  

---

## Ease of Use Feature: Interactive Dashboard

A key usability feature is the multi-scale dashboard:

Users can:
- Select pollutant (PM2.5, NO₂, O₃)  
- Change time scale (hourly → yearly)  
- Compare stations  
- Visualize trends quickly  

### Design Choice

The goal was to reduce analysis friction and allow rapid exploration without writing code.

---

## Live Dashboard

👉 https://israp-airmaps-5cn2zgxninaiwzgc5acex7.streamlit.app/?jr_id=69cc11b6891d7b11cfcaa415#atmospheric-intelligence-hub

---

## What This System Demonstrates

- Sensor data processing pipeline design  
- Handling missing and noisy measurements  
- Multi-source data fusion  
- Real-world atmospheric analysis  
- System thinking for environmental sensing  

---

## Future Improvements

- Sensor drift detection  
- Anomaly detection  
- Calibration bias correction  
- Spatial correlation modeling  
- Forecasting using LSTM-CNN and GNN  

---

## Links

- Resume: https://drive.google.com/file/d/1VwQZnez2cj3dvY2fh6-PjFuyCBK2Z2FD/view?usp=sharing  
- GitHub: https://github.com/Abhipatilap09/windborne-sensors-intern  