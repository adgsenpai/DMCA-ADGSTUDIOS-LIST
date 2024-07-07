import pandas as pd
from tqdm import tqdm

# Define the file path and the domain to filter
file_path = './google-websearch-copyright-removals/urls-no-action-taken.csv'
target_domain = 'adgstudios.co.za'

# Initialize an empty list to store the filtered rows
filtered_rows = []

# Define the chunk size
chunk_size = 100000  # Adjust the chunk size as necessary

# Get the total number of lines in the file for progress tracking
total_lines = sum(1 for _ in open(file_path, encoding='latin1'))  # Change the encoding as needed

# Calculate the number of chunks
total_chunks = (total_lines // chunk_size) + 1

# Read the file in chunks and filter the rows
for chunk in tqdm(pd.read_csv(file_path, chunksize=chunk_size, encoding='latin1'), total=total_chunks):
    filtered_chunk = chunk[chunk['Domain'] == target_domain]
    filtered_rows.append(filtered_chunk)

# Concatenate all filtered chunks into a single DataFrame
filtered_df = pd.concat(filtered_rows, ignore_index=True)

# save to filtered_urls
filtered_df.to_csv('filtered_urls.csv', index=False)

# save timestamp
import datetime
now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
with open('timestamp.txt', 'w') as f:
    f.write(timestamp)