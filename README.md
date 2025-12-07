# 🚀 ETL Pipeline Project

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen)

An automated **ETL (Extract, Transform, Load)** pipeline written in
Python.\
This project demonstrates how to extract raw data, clean and transform
it, then load it into a structured destination such as a database or
file.

This repository is ideal for: - Data engineering students\
- ETL beginners\
- Anyone building automated data pipelines

------------------------------------------------------------------------

## 📁 Project Structure

    etl/
    │
    ├── DATASETS/               # Input / output datasets
    │
    ├── main.py                 # Main ETL orchestrator
    ├── extraction.py           # Extract logic
    ├── transformation.py       # Data cleaning & transformation
    ├── loading.py              # Load logic (files or DB)
    │
    ├── dbconfig.py             # Database connection config
    ├── requirements.txt        # Dependencies
    └── README.md              

------------------------------------------------------------------------

## 🧠 ETL Workflow

### **1. Extract**

-   Reads data from CSV/JSON/API/Database (depending on your pipeline
    setup)
-   Located in: `extraction.py`

### **2. Transform**

-   Cleans missing values\
-   Standardizes formats\
-   Applies feature transformations\
-   Located in: `transformation.py`

### **3. Load**

-   Saves cleaned data into:
    -   CSV files\
    -   Databases (MySQL, PostgreSQL, etc.)\
-   Located in: `loading.py`

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### **1. Clone the repository**

``` bash
git clone https://github.com/Zakaria-codes/etl
cd etl
```

### **2. (Optional) Create a virtual environment**

``` bash
python -m venv venv
# Activate:
# Windows:
venv\Scriptsctivate
# Linux/macOS:
source venv/bin/activate
```

### **3. Install dependencies**

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🚀 Running the ETL Pipeline

Run the entire pipeline:

``` bash
python main.py
```

Or run only one step (if you prefer manual debugging):

### Extract only

``` bash
python extraction.py
```

### Transform only

``` bash
python transformation.py
```

### Load only

``` bash
python loading.py
```

------------------------------------------------------------------------

## 🧪 Example Workflow

``` bash
python main.py --input DATASETS/source.csv --output DATASETS/cleaned_output.csv
```

------------------------------------------------------------------------

## 📦 Dependencies

Key libraries used:

-   pandas
-   numpy
-   sqlalchemy
-   mysql-connector-python
-   python-dotenv

------------------------------------------------------------------------

## 🛠️ Configuration

Modify your DB settings in:

    dbconfig.py

------------------------------------------------------------------------

## 🧩 Features

✔ Extracts datasets from multiple sources\
✔ Cleans and transforms data automatically\
✔ Loads the final dataset into files or DB\
✔ Modular structure\
✔ Easy to extend

------------------------------------------------------------------------

## 🧭 Roadmap

-   [ ] Add API extraction\
-   [ ] Add logging\
-   [ ] Add Airflow scheduling\
-   [ ] Add unit tests\
-   [ ] Add Docker support

------------------------------------------------------------------------

## 🤝 Contributing

1.  Fork repository\
2.  Create branch\
3.  Commit changes\
4.  Push\
5.  Open PR

