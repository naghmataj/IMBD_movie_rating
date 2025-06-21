# app.py
import streamlit as st
import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="IMDb Dashboard", layout="wide")
st.title("🎬 IMDb Dashboard – Live from PostgreSQL")

# PostgreSQL Connection
@st.cache_resource
def get_connection():
    return psycopg2.connect(
        dbname="imdb_project",
        user="postgres",
        password="root123",
        host="localhost",
        port="5432"
    )

conn = get_connection()

# Query options
queries = {
    "Top 10 Genres by Movie Count": """
        SELECT genres, COUNT(DISTINCT id) AS count
        FROM movies
        GROUP BY genres
        ORDER BY count DESC
        LIMIT 10;
    """,
    "Top 10 Genres by Average Rating": """
        SELECT genres, ROUND(AVG(averagerating)::numeric, 2) AS avg_rating
        FROM movies
        GROUP BY genres
        ORDER BY avg_rating DESC
        LIMIT 10;
    """,
    "Movies Released Per Decade": """
        SELECT decade, COUNT(DISTINCT id) AS count
        FROM movies
        GROUP BY decade
        ORDER BY decade;
    """,
    "Rating Distribution": "SELECT averagerating FROM movies;",
    "Rating vs Votes": """
        SELECT averagerating, numvotes
        FROM movies
        WHERE numvotes < 100000;
    """
}

# Dropdown
selected = st.selectbox("📊 Choose Visualization", list(queries.keys()))
df = pd.read_sql(queries[selected], conn)

# Plotting
fig, ax = plt.subplots(figsize=(10,6))
sns.set(style="whitegrid")

if "by Movie Count" in selected:
    sns.barplot(x="count", y="genres", data=df, ax=ax, palette="viridis")
    ax.set_title("Top Genres by Movie Count")
elif "by Average Rating" in selected:
    sns.barplot(x="avg_rating", y="genres", data=df, ax=ax, palette="rocket")
    ax.set_title("Top Genres by Rating")
elif "Per Decade" in selected:
    sns.barplot(x="decade", y="count", data=df, ax=ax, palette="magma")
    ax.set_title("Movies Released Per Decade")
elif "Distribution" in selected:
    sns.histplot(df['averagerating'], bins=20, kde=True, color="skyblue", ax=ax)
    ax.set_title("Distribution of IMDb Ratings")
elif "Votes" in selected:
    sns.scatterplot(data=df, x='averagerating', y='numvotes', ax=ax, alpha=0.6)
    ax.set_title("Rating vs Votes")

st.pyplot(fig)
