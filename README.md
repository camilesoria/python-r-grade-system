# 🎓 Student Grade Management System & Analytics

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![R](https://img.shields.io/badge/R-4.0%2B-blue) ![SQLite](https://img.shields.io/badge/SQLite-Database-green) ![Status](https://img.shields.io/badge/Status-Educational%20Project-orange)

A full-stack data project that implements a CRUD (Create, Read, Update, Delete) system in Python to manage student records, persists data in a SQLite database, and performs statistical analysis and visualization using R.

## 📖 Project Overview

I built this project during my **second semester in Information Systems** to bridge the gap between application logic, database management, and data science.

The goal was to move beyond simple scripts and build a connected system:

1.  **Python** acts as the frontend/backend, managing user input and database connections.

2.  **SQLite** serves as the persistent storage layer.

3.  **R** connects to that same database to perform statistical analysis (mean, distribution) and generate visualizations.


## 🛠️ Key Features

### 🐍 Python (The Application Layer)

* **Complete CRUD Operations:** Users can add, view, update, and delete student records via a console interface.
* **Robust Input Validation:**
    * Custom-written logic to validate email formats (checking for `@` and `.`).

    * Grade validation (ensuring values are 0-100).

* **Error Handling:** Catches database connection errors to prevent crashes.

* **SQL Injection Prevention:** Uses parameterized queries (`?` placeholders) to ensure data security.

* **User Experience:** Nested menu loops allow users to perform multiple operations without restarting the program.

### 📊 R (The Analytics Layer)

* **Direct Database Connection:** Uses `RSQLite` to pull live data from the Python-generated database.
* **Data Cleaning:** Uses `dplyr` pipelines to categorize students (e.g., "Approved", "Excellent").
* **Visualization:** Generates histograms and boxplots using `ggplot2` to analyze grade distributions.

## 🤝 The Development Process (Human + AI)

This project represents a "hybrid" learning approach.

* **My Contribution (The Logic):** I designed the application flow, wrote the custom validation algorithms (loops/conditionals), and built the user interface (CLI). I also implemented the "Update" logic to handle specific field changes.
* **AI Mentorship (The Structure):** I utilized AI to learn and understand the architectural best practices for connecting Python to SQLite and to learn the specific syntax for modern R libraries (`dplyr`/`ggplot2`).

## 🚀 How to Run

### Prerequisites

* Python 3.x
* R and RStudio

### 1. Run the Python Application

```bash
python main.py
```

Follow the on-screen menu to create users and add grades.

### 2. Run the Analysis

Open analysis.R in RStudio or run via terminal:

```bash

Rscript analysis.R
```

This will generate statistical summaries and save a user_data.csv file.


## 📈 Future Improvements

* Add a **graphical user interface (GUI)**.

* Add **more advanced** analytics.

* Improve Python logic with better **error handling/organization**.
