
import plotly.express as px
import pandas as pd

# Load the csv file

df = pd.read_csv('../../data/dataframes/topic-model/topic-model.csv')

# Print the names of all colums in the Dataframe
print(df.columns)

# print the first 10 rows
print(df.head())


#print all topic keywords for manual review
topic_keywords = df.groupby("Topic")[["topic_1", "topic_2", "topic_3", "topic_4"]].first().reset_index()

# Loop through each topic and print its number and associate keywords to get all the discoverd topics
for _, row in topic_keywords.iterrows(): #ai code 2
    topic_num = row["Topic"]
    words = ", ".join([row["topic_1"], row["topic_2"], row["topic_3"], row["topic_4"]])
    print(f"Topic {topic_num}: {words}")





