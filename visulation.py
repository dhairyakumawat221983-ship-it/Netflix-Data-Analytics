
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

INPUT_PATH = sys.argv[1] if len(sys.argv) > 1 else "netflix_titles_cleaned.csv"
OUT_DIR = "charts"
os.makedirs(OUT_DIR, exist_ok=True)


df = pd.read_csv(INPUT_PATH, parse_dates=["date_added"])
print(f"Loaded {len(df)} rows for visualization")

plt.rcParams["figure.dpi"] = 110

# --- Chart 1: Movies vs TV Shows
plt.figure(figsize=(5, 5))
df["type"].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.ylabel("")
plt.title("Movies vs TV Shows on Netflix")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/01_type_split.png")
plt.close()


plt.figure(figsize=(8, 5))
df["year_added"].value_counts().sort_index().plot(kind="bar", color="#E50914")
plt.title("Titles Added to Netflix per Year")
plt.xlabel("Year Added")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/02_titles_per_year.png")
plt.close()


plt.figure(figsize=(8, 5))
top_countries = df[df["primary_country"] != "Unknown"]["primary_country"].value_counts().head(10)
top_countries.sort_values().plot(kind="barh", color="#E50914")
plt.title("Top 10 Countries by Number of Titles")
plt.xlabel("Number of Titles")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/03_top_countries.png")
plt.close()


plt.figure(figsize=(8, 5))
top_genres = df["primary_genre"].value_counts().head(10)
top_genres.sort_values().plot(kind="barh", color="#221f1f")
plt.title("Top 10 Primary Genres")
plt.xlabel("Number of Titles")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/04_top_genres.png")
plt.close()

plt.figure(figsize=(8, 5))
movie_durations = df[(df["type"] == "Movie") & (df["duration_unit"] == "min")]["duration_num"]
movie_durations.plot(kind="hist", bins=30, color="#E50914", edgecolor="white")
plt.title("Movie Duration Distribution")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/05_movie_duration_dist.png")
plt.close()


plt.figure(figsize=(8, 5))
df["rating"].value_counts().plot(kind="bar", color="#564d4d")
plt.title("Titles by Content Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/06_rating_breakdown.png")
plt.close()

print(f"Saved 6 charts -> {OUT_DIR}/")