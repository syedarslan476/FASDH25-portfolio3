import pandas as pd
import plotly.express as px
import os

# STEP 1: Create the output folder
output_folder = "Atiya_kiyani_Length_count_Task"
os.makedirs(output_folder, exist_ok=True)

# STEP 2: Load the dataset
df = pd.read_csv("C:/Users/ATIYA/Downloads/FASDH25/FASDH25-portfolio3/data/dataframes/length/length.csv")

# STEP 3: Basic summary
print("Columns:", df.columns)
print(df.head())

# STEP 4: Group by year to get total, average, and count
year_summary = df.groupby("year")["length"].agg(
    total_words="sum",
    average_words="mean",
    articles="count"
).reset_index()

# STEP 5: Plot 1 - Total Words by Year
fig1 = px.bar(year_summary, x="year", y="total_words",
              title="Total Words Published by Year",
              labels={"total_words": "Total Words", "year": "Year"})
fig1.write_html(f"{output_folder}/atiya1_total_words_year.html")
fig1.show()

# STEP 6: Plot 2 - Average Words by Year
fig2 = px.line(year_summary, x="year", y="average_words",
               title="Average Article Length by Year",
               markers=True,
               labels={"average_words": "Average Words", "year": "Year"})
fig2.write_html(f"{output_folder}/atiya2_avg_words_year.html")
fig2.show()

# STEP 7: Group by month for total words
month_summary = df.groupby("month")["length"].sum().reset_index()
fig3 = px.bar(month_summary, x="month", y="length",
              title="Total Words Published by Month",
              labels={"length": "Total Words", "month": "Month"})
fig3.write_html(f"{output_folder}/atiya3_total_words_month.html")
fig3.show()

# STEP 8: Categorize article length
df["length_type"] = df["length"].apply(lambda x: "Short (<300)" if x < 300 else
                                                  "Medium (300–800)" if x <= 800 else
                                                  "Long (>800)")

df["year_month"] = pd.to_datetime(df["year"].astype(str) + "-" + df["month"].astype(str).str.zfill(2))
length_type_summary = df.groupby(["year_month", "length_type"]).size().reset_index(name="count")

# STEP 9: Plot 4 - Line plot of article count by length type over time
fig4 = px.line(length_type_summary, x="year_month", y="count", color="length_type",
               title="Monthly Trends of Article Length Types",
               markers=True,
               labels={"count": "Number of Articles", "year_month": "Month", "length_type": "Length Type"})
fig4.update_layout(xaxis_tickangle=45)
fig4.write_html(f"{output_folder}/atiya4_length_type_trend.html")
fig4.show()
