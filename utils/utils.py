import pandas as pd

# Load the CSV files
movies_df = pd.read_csv('ml-latest-small/movies.csv')
movie_ids_df = pd.read_csv('ml-latest-small/links.csv')

# Merge on 'movieId' column
merged_df = pd.merge(movies_df, movie_ids_df, on='movieId')

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('merged_movies.csv', index=False)
