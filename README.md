# 🎬 imbd_movie_rating

In this project, we analyze **IMDb's Top-Rated Movies** dataset using Python, SQL, and a live dashboard. The goal is to load, clean, transform, store, and visualize movie data to uncover meaningful trends about genres, ratings, and audience preferences over time.

## 📌 Project Highlights

- 🔄 ETL Pipeline: Extract data from CSV → Transform using `pandas` → Load into PostgreSQL  
- 💾 PostgreSQL Database: Store structured and cleaned movie data  
- 📊 SQL-Powered Visualizations: Generate insights directly from the database  
- 🌐 Interactive Dashboard: Built using Streamlit with real-time SQL queries

## 🧰 Tech Stack

- **Python** – Data manipulation, ETL  
- **Pandas** – Data loading, cleaning, transformation  
- **PostgreSQL** – Database to store structured data  
- **psycopg2** – PostgreSQL connector for Python  
- **Streamlit** – Interactive dashboard frontend  
- **Seaborn / Matplotlib** – Data visualizations

## 📁 Project Structure

imbd_top_rating/  
├── Dashboard/ – Streamlit `app.py` and config file  
├── visuals_DB/ – Folder storing saved PNG visualizations  
├── imdb.ipynb – Jupyter notebook for data cleaning and ETL  
├── IMDb_top_rated_data.xlsx – Original dataset file  
├── queries.sql – SQL file with analysis queries  
└── README.md – This documentation file

---

## 🚀 Project Workflow

### ✅ Step 1: Environment Setup

Install the required libraries:

```bash
pip install pandas psycopg2-binary streamlit matplotlib seaborn

### ✅ Step 2: Load & Clean Data (ETL Process)

Using `imdb.ipynb`, we:

- Load the `IMDb_top_rated_data.xlsx` dataset  
- Clean the `genres` column  
- Convert `releaseYear` to integer  
- Add a new column for `decade`  
- Split rows with multiple genres using `explode()`  
- Standardize column names  

---

### ✅ Step 3: Store in PostgreSQL

- Connect to PostgreSQL using `psycopg2`  
- Create the `movies` table  
- Insert cleaned data into the table  

**Table schema:**

```sql
CREATE TABLE movies (
    id TEXT,
    title TEXT,
    genres TEXT,
    averagerating FLOAT,
    numvotes INTEGER,
    releaseyear INTEGER,
    decade INTEGER,
    PRIMARY KEY (id, genres)
);

### ✅ Step 4: Run SQL Queries

SQL queries stored in `queries.sql` include:

- Top genres by movie count  
- Average rating by genre  
- Movies released per decade  
- Rating distribution  
- Ratings vs Votes correlation  

---

### ✅ Step 5: Streamlit Dashboard

To launch the interactive dashboard:

```bash
cd Dashboard
streamlit run app.py

## 📊 Visualizations Include

- Top 10 Genres by Number of Movies  
- Top 10 Genres by Average Rating  
- Number of Movies per Decade  
- Distribution of IMDb Ratings  
- Scatter Plot: Ratings vs Number of Votes  

All charts update dynamically using real-time data from the PostgreSQL database.

---

## ✅ Conclusion

By completing this project, we:

- Cleaned and transformed the IMDb dataset  
- Stored structured data in a PostgreSQL database  
- Created live, SQL-powered visual dashboards  
- Gained valuable insights into movie ratings, genres, and trends over time  

This project demonstrates an end-to-end approach to **data engineering**, **SQL analysis**, and **dashboard development**.
