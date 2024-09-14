import pandas as pd
from flask import request, jsonify, render_template, current_app as app
from concurrent.futures import ThreadPoolExecutor
from .services import get_movie_details
from recommendation_system import get_recommendations

# Load the merged movie data
movies = pd.read_csv('data/merged_movies.csv')

# Initialize a ThreadPoolExecutor for concurrent requests
executor = ThreadPoolExecutor(max_workers=10)

@app.route('/')
def index():
    print("Index route was accessed.")
    return render_template('index.html')

@app.route('/recommendations')
def recommendations():
    print("recommendations route was accessed.")
    movie_title = request.args.get('movie')
    # Example logic for recommendations
    return render_template('recommendations.html', movie_title=movie_title)

@app.route('/movies', methods=['GET'])
def get_movies():
    sampled_movies = movies[['movieId', 'imdbId', 'title', 'genres']]#.sample(n=30, random_state=1)
    
    movie_details = []
    for _, row in sampled_movies.iterrows():
        # details = get_movie_details(row['imdbId'])
        details = {}
        details['title'] = row['title']
        details['genres'] = row['genres']
        movie_details.append(details)
    
    return jsonify(movie_details)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    movie_title = data.get('movie')

    if not movie_title:
        return jsonify({'error': 'No movie title provided'}), 400

    recommendations = get_recommendations(movie_title)
    
    if not recommendations:
        return jsonify({'error': 'Movie not found or no recommendations available'}), 404

    movie_details = []
    for movie in recommendations:
        # details = get_movie_details(movie['imdbId'])
        details = {}
        details['title'] = movie['title']
        details['genres'] = movie['genres']
        movie_details.append(details)

    return jsonify(movie_details)
