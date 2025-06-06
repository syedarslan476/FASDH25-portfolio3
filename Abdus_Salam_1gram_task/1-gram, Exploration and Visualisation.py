import pandas as pd
import nltk
from nltk.corpus import stopwords
import plotly.express as px
# Note: For most of the code I have taken help from the respective lecture of n grams.
# Load unigram dataset
df = pd.read_csv('../data/dataframes/n-grams/1-gram/1-gram-year.csv')

# Top 20 unigrams by total count
top_unigrams = df.sort_values(by='count-sum', ascending=False).head(20)
print(top_unigrams)

# Unigrams containing "gaza"
print(df[df['1-gram'].str.contains('gaza', case=False, na=False)].sort_values(by='count-sum', ascending=False))

# Unigrams that are exactly "war"
print(df[df['1-gram'].str.lower() == 'war'].sort_values(by='count-sum', ascending=False))

# Most frequent unigrams (based on repetition in data, not total counts)
print(df['1-gram'].value_counts().head(10))

# Define violence-related keywords
violence_keywords = ['attack', 'bomb', 'kill', 'strike', 'casualty']

# Filter unigrams related to violence #chatgpt conversation 1
violence_df = df[df['1-gram'].str.contains('|'.join(violence_keywords), case=False, na=False)].copy()

# Create a 'keyword' column that stores which keyword matched #chatgpt conversation 2
def find_keyword(text):
    for word in violence_keywords:
        if word in text.lower():
            return word
    return None

violence_df['keyword'] = violence_df['1-gram'].apply(find_keyword)

# Group by year and keyword, then sum counts
stacked_data = violence_df.groupby(['year', 'keyword'])['count-sum'].sum().reset_index()

# Create stacked bar chart
fig = px.bar(
    stacked_data,
    x='year',
    y='count-sum',
    color='keyword',
    title='Violence-Related Terms: Yearly Breakdown (Stacked)',
    labels={'count-sum': 'Total Mentions', 'year': 'Year'},
    barmode='stack',
)

# Improve x-axis to show every year
fig.update_layout(xaxis=dict(dtick=1))

# Show the plot
fig.show()

# Save to HTML
fig.write_html("Abdus salam.html")
print("Stacked bar chart saved as violence_stacked_bar.html")
