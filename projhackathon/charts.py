import json
import pandas as pd
import matplotlib.pyplot as plt

# Load job data
with open("jobs_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Function to plot and save bar charts
def plot_top(field, filename, title, top_n=5):
    top_data = df[field].value_counts().head(top_n)
    plt.figure(figsize=(8, 4))
    top_data.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title(title)
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f"static/{filename}")
    plt.close()

# Generate charts
plot_top("Job_Title", "top_titles.png", "Top 5 Job Titles")
plot_top("Company", "top_companies.png", "Top 5 Companies")
plot_top("Location", "top_locations.png", "Top 5 Locations")