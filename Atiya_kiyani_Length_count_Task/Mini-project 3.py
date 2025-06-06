import pandas as pd
import plotly.express as px
import os

# Set the folder path and list files
folder_path = 'C:/Users/ATIYA/Downloads/FASDH25/FASDH25-portfolio3/data/dataframes/length'
files = os.listdir(folder_path)
print("Files in 'length' folder:", files)

# Step 1: Load the data
df = pd.read_csv(folder_path + '/length.csv')

# Step 2: Print column names and preview
print("Columns:", df.columns)
print(df.head())

# Step 3: Group by year and calculate average length
df_yearly = df.groupby('year', as_index=False)['length'].mean()

# Step 4: Plot average length by year
fig1 = px.line(df_yearly, x='year', y='length', title='Average Article Length by Year')
fig1.write_html("atiya-kiyani-Mini-project_bar.html")
fig1.show()

# Step 5: Group by month and calculate average length
df_monthly = df.groupby('month', as_index=False)['length'].mean()

# Step 6: Plot average length by month
fig2 = px.bar(df_monthly, x='month', y='length', title='Average Article Length by Month')
fig2.write_html("atiya-kiyani-mini-project_line.html")
fig2.show()
