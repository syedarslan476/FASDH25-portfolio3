import pandas as pd

# Define the input file from the previous script's output
input_file = 'TF-IDF_output.csv'
df = pd.read_csv('TF-IDF_output.csv')

# Create the Edges List 
edges = df[['filename-1', 'filename-2', 'similarity']].copy()
edges.columns = ['Source', 'Target', 'Weight']

#Extract nodes from filename-1 and topic_1 # Took help from chatgpt
source_nodes = df[['filename-1', 'topic_1']].copy()
source_nodes.columns = ['Id', 'topic']

# Extract nodes from filename-2 and topic_2
target_nodes = df[['filename-2', 'topic_2']].copy()
target_nodes.columns = ['Id', 'topic']

# Combine both sets of nodes and remove duplicates based on 'Id'
nodes = pd.concat([source_nodes, target_nodes]).drop_duplicates(subset='Id').reset_index(drop=True)

# Add a 'Label' column, which is typically the same as 'Id' for display in graph tools
nodes['Label'] = nodes['Id']

#Save to CSV Files
edges.to_csv('TF-IDF-edges.csv', encoding='utf-8-sig', index=False)
nodes.to_csv('TF-IDF-nodes.csv', encoding='utf-8-sig', index=False)


