# CampusPulse Intelligence: Smart Campus Operations & Sustainability Analytics

## 📊 Project Overview

**CampusPulse Intelligence** is a data analytics project designed to analyze campus operations and sustainability-related data.

The project provides insights into:

* ⚡ Electricity consumption and cost
* 🍽️ Canteen food preparation and waste
* 🎓 Student attendance
* 💰 Campus operating costs

The project uses **Python, SQL, Power BI, Power Query, and DAX** to clean, analyze, visualize, and present campus data.

> **Note:** The dataset used in this project is synthetic and created for analytics practice and demonstration purposes.

## 🎯 Project Objectives

* Analyze electricity consumption across campus buildings.
* Monitor electricity costs and energy usage.
* Identify food waste patterns by meal and food item.
* Analyze student attendance patterns.
* Understand operating costs by department and category.
* Build an interactive Power BI dashboard for decision support.

## 🔎 Key Insights

Based on the analysis:

* The campus recorded **1.43 million+ kWh** of energy consumption.
* Total electricity cost was approximately **₹11.47 million**.
* Food waste accounted for approximately **11.63%** of total food prepared.
* Food waste cost was approximately **₹3.21 million**.
* Overall student attendance was **81.89%**.
* **198 students** were identified below the 75% attendance threshold.
* Operating costs totaled approximately **₹20.46 million**.
* Power BI dashboards were used to analyze energy, food waste, attendance, and operating-cost patterns.

## 🗂️ Dataset

The project contains synthetic datasets covering:

* **Students** — student and academic information
* **Attendance** — student attendance records
* **Electricity** — building-level energy consumption and electricity costs
* **Canteen** — food preparation and waste information
* **Operating Costs** — campus expenses by department and category

The datasets were cleaned and analyzed using Python before being used for SQL and Power BI analysis.

## 🛠️ Tools & Technologies

* **Python** — Data cleaning, analysis and visualization
* **SQL** — Data querying and analysis
* **Power Query** — Data transformation
* **Power BI** — Interactive dashboards
* **DAX** — KPI and analytical measures
* **GitHub** — Project documentation and version control

## 📁 Project Structure

```text
CampusPulse_Intelligence/
│
├── 01_Data/
│   ├── students.csv
│   ├── attendance.csv
│   ├── electricity.csv
│   ├── canteen.csv
│   ├── operating_costs.csv
│   ├── students_clean.csv
│   ├── attendance_clean.csv
│   ├── electricity_clean.csv
│   ├── canteen_clean.csv
│   └── operating_costs_clean.csv
│
├── 03_SQL/
│   ├── campuspulse.db
│   └── SQL queries
│
├── 05_PowerBI/
│   └── CampusPulse_Intelligence.pbix
│
├── 06_Screenshots/
│   ├── campus_overview.png
│   ├── energy_electricity.png
│   ├── canteen_food_waste.png
│   ├── student_attendance.png
│   └── operations_cost.png
│
└── python/
    ├── Data cleaning scripts
    ├── Analysis scripts
    └── Visualization scripts
```

## 📈 Key KPIs

| KPI                           |            Value |
| ----------------------------- | ---------------: |
| Total Students                |            2,000 |
| Overall Attendance            |           81.89% |
| Total Energy Consumption      | 1,429,574.16 kWh |
| Total Electricity Cost        |   ₹11,466,586.46 |
| Total Food Prepared           |          581,087 |
| Total Food Waste              |           67,588 |
| Food Waste Percentage         |           11.63% |
| Food Waste Cost               |    ₹3,205,005.55 |
| Total Operating Cost          |   ₹20,458,817.83 |
| Students Below 75% Attendance |              198 |

## 🔄 Project Workflow

```text
Raw Data
   ↓
Python Data Cleaning
   ↓
Cleaned CSV Files
   ↓
SQL Analysis
   ↓
Power Query Transformation
   ↓
DAX Measures
   ↓
Power BI Dashboard
   ↓
Business Insights
```

## 📊 Power BI Dashboard

### Campus Over
