import pandas as pd
import plotly.express as px
import os

os.makedirs("Atiya_kiyani_Length_count_Task", exist_ok=True)

# Step 1: Import data
data = pd.read_csv("C:/Users/ATIYA/Downloads/FASDH25/FASDH25-portfolio3/data/dataframes/length/length.csv")
print("Dataset imported successfully.")

# Step 2: Create a date column in YYYY-MM format for monthly-level analysis
data["month_str"] = data["month"].astype(str).str.zfill(2)
data["year_month"] = pd.to_datetime(data["year"].astype(str) + "-" + data["month_str"])

# Step 3: Summarize article lengths per year
year_summary = data.groupby("year")["length"].agg(total_words="sum", average_words="mean", articles="count").reset_index()
print("Annual statistics preview:")
print(year_summary.head())

# Plot 1: Yearly total word count
fig_total_year = px.bar(year_summary, x="year", y="total_words",
                        title="Total Words Published Annually",
                        labels={"total_words": "Total Word Count", "year": "Year"})
fig_total_year.write_html("Atiya_kiyani_Length_count_Task/atiya1_total_words_year.html")
print("Plot 1 saved: atiya1_total_words_year.html")

# Plot 2: Yearly average article length
fig_avg_year = px.line(year_summary, x="year", y="average_words",
                       title="Mean Article Length per Year",
                       markers=True,
                       labels={"average_words": "Average Word Count", "year": "Year"})
fig_avg_year.write_html("Atiya_kiyani_Length_count_Task/atiya2_avg_words_year.html")
print("Plot 2 saved: atiya2_avg_words_year.html")

# Step 4: Monthly statistics
monthly_stats = data.groupby("year_month")["length"].agg(monthly_total="sum", monthly_avg="mean", count="count").reset_index()

# Plot 3: Monthly total article length
fig_total_month = px.line(monthly_stats, x="year_month", y="monthly_total",
                          title="Monthly Total Words in Articles",
                          markers=True,
                          labels={"monthly_total": "Total Words", "year_month": "Month"})
fig_total_month.write_html("Atiya_kiyani_Length_count_Task/atiya3_total_words_month.html")
print("Plot 3 saved: atiya3_total_words_month.html")

# Step 5: Categorize article lengths into Short, Medium, Long
def categorize_length(x):
    if x < 300:
        return "Short"
    elif x <= 800:
        return "Medium"
    else:
        return "Long"

data["length_group"] = data["length"].apply(categorize_length)

# Group by month and length group
type_distribution = data.groupby(["year_month", "length_group"]).size().reset_index(name="article_count")

# Plot 4: Monthly trend of length categories
fig_length_trend = px.line(type_distribution, x="year_month", y="article_count", color="length_group",
                           title="Monthly Distribution of Article Length Types",
                           labels={"year_month": "Month", "article_count": "Number of Articles", "length_group": "Length Category"},
                           markers=True)
fig_length_trend.update_layout(xaxis_tickangle=45)
fig_length_trend.write_html("Atiya_kiyani_Length_count_Task/atiya4_length_type_trend.html")
print("Plot 4 saved: atiya4_length_type_trend.html")
