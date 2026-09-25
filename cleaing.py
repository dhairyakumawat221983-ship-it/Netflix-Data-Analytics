

import sys
import pandas as pd

INPUT_PATH = sys.argv[1] if len(sys.argv) > 1 else "netflix_titles.csv"
OUTPUT_PATH = "netflix_titles_cleaned.csv"


df = pd.read_csv("C:\\Users\\Dhairya\\OneDrive\\Desktop\\netflix prject\\netflix_titles.csv")
print(f"Loaded {len(df)} rows, {len(df.columns)} columns")




for col in ["director", "cast", "country"]:
    df[col] = df[col].fillna("Unknown")


df["date_added"] = df["date_added"].str.strip()
df["date_added"] = pd.to_datetime(df["date_added"], format="%B %d, %Y", errors="coerce")

df["rating"] = df["rating"].fillna("Not Rated")

mask_bad_rating = df["rating"].str.contains("min", na=False)
df.loc[mask_bad_rating, "duration"] = df.loc[mask_bad_rating, "rating"]
df.loc[mask_bad_rating, "rating"] = "Not Rated"

df["duration"] = df["duration"].fillna("Unknown")
df["duration_num"] = df["duration"].str.extract(r"(\d+)").astype(float)
df["duration_unit"] = df["duration"].apply(
    lambda x: "Season(s)" if "Season" in str(x) else ("min" if "min" in str(x) else None)
)


df["primary_country"] = df["country"].apply(lambda x: x.split(",")[0].strip())


df["primary_genre"] = df["listed_in"].apply(lambda x: x.split(",")[0].strip())


current_year = pd.Timestamp.now().year
bad_years = df[(df["release_year"] < 1900) | (df["release_year"] > current_year)]
if len(bad_years):
    print(f"Warning: {len(bad_years)} rows have suspicious release_year values")



before = len(df)
df = df.drop_duplicates()
df = df.drop_duplicates(subset=["title", "type", "director"], keep="first")
print(f"Dropped {before - len(df)} duplicate rows")


df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month_name()


df.to_csv(OUTPUT_PATH, index=False)
print(f"Saved cleaned data -> {OUTPUT_PATH}")