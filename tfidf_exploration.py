import pandas as pd

# Load data
df_tfidf = pd.read_csv('data/dataframes/tfidf/tfidf-over-0.3.csv')
df_topic = pd.read_csv('data/dataframes/topic-model/topic-model.csv')

# Rename topic column for clarity
topic_df = df_topic.rename(columns={'Topic': 'topic_num'})

# Merge topic_num for filename-1 # merging is done taking help from chatgpt
df_tfidf = df_tfidf.merge(
    topic_df[['file', 'topic_num']].rename(columns={'file': 'filename-1', 'topic_num': 'topic_1'}),
    on='filename-1', how='left'
)

# Merge topic_num for filename-2
df_tfidf = df_tfidf.merge(
    topic_df[['file', 'topic_num']].rename(columns={'file': 'filename-2', 'topic_num': 'topic_2'}),
    on='filename-2', how='left'
)
# Add filtering remove rows with -1 in topic columns         # took help from chatgpt
df_tfidf = df_tfidf[(df_tfidf['topic_1'] != -1) & (df_tfidf['topic_2'] != -1)]

# Filter pairs with same topic
same_topic = df_tfidf[df_tfidf['topic_1'] == df_tfidf['topic_2']]

print(f"Pairs sharing the same topic: {len(same_topic)}")

# High similarity (>0.75) and same topic
high_sim_same_topic = same_topic[same_topic['similarity'] > 0.75]

print(f"High similarity pairs sharing same topic: {len(high_sim_same_topic)}")
print(high_sim_same_topic.head())

# Save result
high_sim_same_topic.to_csv('TF-IDF_output.csv', index=False)
