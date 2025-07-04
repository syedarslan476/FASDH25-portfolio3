
import plotly.express as px
import pandas as pd

# load csv file

df = pd.read_csv('../../data/dataframes/topic-model/topic-model.csv')
print(df.columns) #check for columns
print(df.head())  #check for rows

#removing unclassified articles(articles with no topics assigned)

df = df[df["Topic"] != -1]  #ai document code 1 + exercise 14.2


#remove rows where all topic keywords are stopwords
#stop words from NLTK 
stop_words = { 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 
    'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 
    'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 
    'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 
    'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 
    'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 
    'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 
    'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 
    'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 
    'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 
    'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 
    'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'al', 'said', 'don', 'should', 'now'}
# checking for topics which has all keywords as stopwords
def is_all_stopwords(row):  # ai code 2
    words = [row['topic_1'], row['topic_2'], row['topic_3'], row['topic_4']]
   # lowercase to check for storp words and select the topics that has all the values as stopword
    return all(word.lower() in stop_words for word in words)

# Update the dataframe to keep only the rows where not all topic words are stopwords
df = df[~df.apply(is_all_stopwords, axis=1)]

print(df)  # Printing the updated dataframe


# Print all topic keywords for manual review
# Group by topic and get the first row of keywords for each topic
topic_keywords = df.groupby("Topic")[["topic_1", "topic_2", "topic_3", "topic_4"]].first().reset_index()

# Loop through each topic and print its keywords
for _, row in topic_keywords.iterrows():   #ai code 3
    topic_num = row["Topic"] #Get the topic number

    #combine the four keywords into one line, separating by commas
    words = ", ".join([row["topic_1"], row["topic_2"], row["topic_3"], row["topic_4"]])

    #print the topic number and its keywords
    print(f"Topic {topic_num}: {words}")

# Define each topic to its relevant category
category_map = {
    # Conflict
    1: "Conflict", 5: "Conflict", 6: "Conflict", 8: "Conflict", 23: "Conflict",
    24: "Conflict", 44: "Conflict", 51: "Conflict", 73: "Conflict",

    # Humanitarian
    3: "Humanitarian", 13: "Humanitarian", 21: "Humanitarian", 22: "Humanitarian",
    30: "Humanitarian", 35: "Humanitarian", 39: "Humanitarian", 42: "Humanitarian",
    57: "Humanitarian", 58: "Humanitarian", 70: "Humanitarian", 74: "Humanitarian",
    75: "Humanitarian", 10: "Humanitarian", 28: "Humanitarian", 

    # Diplomacy
    4: "Diplomacy", 7: "Diplomacy", 11: "Diplomacy", 12: "Diplomacy", 14: "Diplomacy",
    15: "Diplomacy", 17: "Diplomacy", 18: "Diplomacy", 19: "Diplomacy", 25: "Diplomacy",
    31: "Diplomacy", 36: "Diplomacy", 37: "Diplomacy", 53: "Diplomacy", 59: "Diplomacy",
    60: "Diplomacy", 61: "Diplomacy", 66: "Diplomacy", 77: "Diplomacy", 45: "Diplomacy",
}

#  filtering to Keep only relevant topics
df = df[df["Topic"].isin(category_map.keys())]

# new column 'Narrative_Category' by mapping each topic number to its category
df["Narrative_Category"] = df["Topic"].map(category_map)

#️Create full date and month-year column
df["date"] = pd.to_datetime(df[["year", "month", "day"]])
df["month_year"] = df["date"].dt.to_period("M").astype(str)

# Keep only data from 2023-10-07 onwards
start_date = pd.to_datetime("2023-09-07")
df = df[df["date"] >= start_date]

#  Group by month and narrative category
grouped = df.groupby(["month_year", "Narrative_Category"]).size().reset_index(name="Article_Count")


# Create a line char 


fig = px.line(
    grouped,
    x="month_year",              # Timeline on X-axis
    y="Article_Count",           # Number of articles
    color="Narrative_Category",  # One line per category
    markers=True,                # Adds dots to show each point
    title="Narrative Shift in Al Jazeera’s Gaza Coverage (Since Oct 7, 2023)",
    labels={
        "month_year": "Month",
        "Article_Count": "Number of Articles",
        "Narrative_Category": "Narrative Focus"
    }
)

# Rotate labels to prevent crowding
fig.update_layout(xaxis_tickangle=-45)


# Add annotation (example: highlight October 2023 spike)
fig.add_annotation(
    x="2023-10",  # Month to annotate
    y=grouped[(grouped["month_year"] == "2023-10")]["Article_Count"].max(),  # Y position
    text="Start of Gaza Conflict(month of oct)",  # Annotation text
    showarrow=True,
    arrowhead=1,
    ax=0,
    ay=-40,
    bgcolor="white",
    bordercolor="black"
)

#show the graph
fig.show()

# Save to HTML
fig.write_html("../output/Jafar Uddin.html")
print("Line graph of Narrative Shift in Al Jazeera's Gaza Coverage saved as 'Jafar Uddin.html'")


