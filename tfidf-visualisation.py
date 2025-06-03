import pandas as pd
import plotly.express as px

# Load high similarity & same topic data from the new filename
df = pd.read_csv("TF-IDF_output.csv")

# Adding some topic keywords
topic_keywords = {
    38: "protests, violence, UN, Gaza, ceasefire",
    27: "media, narrative, journalism, Western bias",
    15: "Netanyahu, elections, Likud, right-wing",
    4:  "UN, resolutions, international law, Palestine",
    9:  "Hamas, rockets, retaliation, airstrikes",
}

# Count number of similar pairs per topic
topic_counts = df['topic_1'].value_counts().reset_index()
topic_counts.columns = ['topic_num', 'pair_count']

# Map topic keywords
topic_counts['topic_keywords'] = topic_counts['topic_num'].map(topic_keywords)
topic_counts = topic_counts.dropna(subset=["topic_keywords"])

# Plotting the graph
fig = px.bar(topic_counts,
             x='topic_keywords',
             y='pair_count',
             title="High-Similarity Document Pairs by Topic",
             labels={'topic_keywords': 'Topic (Keywords)', 'pair_count': 'Number of Similar Pairs'},
             color='pair_count',
             text='pair_count')

fig.update_layout(xaxis_tickangle=45)

# Save interactive and static visualizations with new filenames
fig.write_html("final_analysis_TF-IDF.html")
fig.write_image("final_analysis_TF-IDF.png", scale=2)

print("Analysis completed and saved as:")
print(" - final_analysis_TF-IDF.html")
print(" - final_analysis_TF-IDF.png")
