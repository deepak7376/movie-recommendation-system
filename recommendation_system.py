import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load movie data
movies = pd.read_csv('data/merged_movies.csv')

# Preprocessing
# movies['description'] = movies['description'].fillna('')
movies['genres'] = movies['genres'].fillna('')

# Combine features
movies['combined_features'] = movies['genres'] #+ ' ' + movies['description']

# Vectorize the combined features
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['combined_features'])

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Create a reverse mapping of indices and movie titles
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices.get(title)
    if idx is None:
        return []

    # Get the pairwise similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the top 15 most similar movies
    sim_scores = sim_scores[1:15]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 15 most similar movies
    return movies.iloc[movie_indices][['movieId', 'imdbId', 'title', 'genres']].to_dict('records')
