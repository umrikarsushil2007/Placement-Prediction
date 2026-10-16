import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from src.data.load_data import load_data

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHARTS_DIR = os.path.join(BASE_DIR, "App", "static", "charts")
RESULTS_DIR = os.path.join(BASE_DIR, "Results")
os.makedirs(CHARTS_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

def basic_eda(df):
    print("Print first 5 rows of the dataset.")
    print(df.head())
    print("Print last 5 rows of the dataset.")
    print(df.tail())
    print("Print 25 to 35 rows of the dataset.")
    print(df.iloc[25:36])
    print("Print sample o f10 records of the dataset.")
    print(df.sample(n=10))
    print("Column names of the dataset.")
    print(df.columns)
    print("="*50)
    print((df.dtypes))
    print("Complete informatin of the dataset.")
    print(df.info())
    print("Describe the dataset.")
    print(df.describe())
    print("Null values of the dataset.")
    print(df.isnull().sum())
    print("Duplicate values of the dataset.")
    print(df.duplicated().sum())
    missing = df.isnull().sum()
    print("Missing values of the dataset.")
    print(missing[missing>0])
    print(df["PlacementStatus"].value_counts())
    count = df["PlacementStatus"].value_counts()
    plt.figure(figsize=(6, 5))
    plt.bar(count.index.astype(str), count.values)
    plt.title("Distribution of Placement Status")
    plt.xlabel("Placement Status")
    plt.ylabel("Count")
    plt.savefig(os.path.join(RESULTS_DIR, "placement_status.png"))
    plt.close()

def univariable(df):
    plt.figure(figsize=(6, 5))
    plt.hist(df["CGPA"], bins=10)
    plt.title("Histogram of CGPA")
    plt.xlabel("CGPA")
    plt.ylabel("Frequency")
    plt.savefig(os.path.join(CHARTS_DIR, "cgpa_histogram.png"))
    plt.close()

def gender_distribution(df):
    gendercount = df["Gender"].value_counts()
    plt.figure(figsize=(6, 5))
    plt.pie(gendercount.values, labels=gendercount.index, autopct="%1.1f%%", startangle=90)
    plt.title("Distribution of Gender")
    plt.savefig(os.path.join(RESULTS_DIR, "gender_count.png"))
    plt.close()

def bivariate_eda(df):
    # --- PLOT 1: Scatter Plot ---
    plt.figure(figsize=(6, 5))
    scatter_data = df.dropna(subset=["CGPA", "AptitudeTestScore"])
    plt.scatter(scatter_data["CGPA"], scatter_data["AptitudeTestScore"])
    plt.title("CGPA vs Aptitude Test Score")
    plt.xlabel("CGPA")
    plt.ylabel("Aptitude Test Score")
    plt.savefig(os.path.join(CHARTS_DIR, "scatter.png"))
    plt.close()

    plt.figure(figsize=(6, 5))
    placed = df[df["PlacementStatus"] == 1]["CGPA"]
    not_placed = df[df["PlacementStatus"] == 0]["CGPA"]
    plt.boxplot([placed, not_placed], tick_labels=["placed", "not placed"])
    plt.title("CGPA vs Placement Status")
    plt.xlabel("Placement Status")
    plt.ylabel("CGPA")
    plt.savefig(os.path.join(CHARTS_DIR, "GGPA_PlacementStatus.png"))
    plt.close()

    plt.figure(figsize=(6, 5))
    count = pd.crosstab(df["Gender"], df["PlacementStatus"])
    count.plot(kind="bar", ax=plt.gca())
    plt.title("Gender vs Placement Status")
    plt.xlabel("Gender")
    plt.ylabel("Placement Status")
    plt.savefig(os.path.join(CHARTS_DIR, "Gender_Placement.png"))
    plt.close()

def multivsriated(df):
    # Select only numerical columns
    data = df[["CGPA", "AptitudeTestScore", "PlacementStatus"]]
    correlation = data.corr()
    plt.figure(figsize=(6, 5))
    sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.savefig(os.path.join(CHARTS_DIR, "correlation_heatmap_3 attributes.png"))
    plt.close()

    coorelation = df.corr(numeric_only=True)
    plt.figure(figsize=(6, 5))
    sns.heatmap(coorelation, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.savefig(os.path.join(CHARTS_DIR, "correlation_heatmap.png"))
    plt.close()

if __name__ == "__main__":
    df = load_data()
    basic_eda(df)
    univariable(df)
    gender_distribution(df)
    bivariate_eda(df)
    multivsriated(df)