import requests
from .cache import cache_table

OMDB_API_KEY = '9db870d3'
OMDB_API_URL = 'http://www.omdbapi.com/'

def fetch_movie_details(imdbId_with_tt):
    response = requests.get(OMDB_API_URL, params={
        'i': imdbId_with_tt,
        'apikey': OMDB_API_KEY
    })
    if response.status_code == 200:
        data = response.json()
        return {
            'title': data.get('Title', 'Unknown'),
            'poster': data.get('Poster', 'https://via.placeholder.com/200x300?text=No+Image'),
            'genres': data.get('Genre', 'Unknown'),
            'year': data.get('Year', 'Unknown'),
            'rated': data.get('Rated', 'Unknown'),
            'released': data.get('Released', 'Unknown'),
            'runtime': data.get('Runtime', 'Unknown'),
            'director': data.get('Director', 'Unknown'),
            'writer': data.get('Writer', 'Unknown'),
            'actors': data.get('Actors', 'Unknown'),
            'plot': data.get('Plot', 'No plot available'),
            'language': data.get('Language', 'Unknown'),
            'country': data.get('Country', 'Unknown'),
            'awards': data.get('Awards', 'Unknown'),
            'ratings': data.get('Ratings', []),
            'metascore': data.get('Metascore', 'Unknown'),
            'imdbRating': data.get('imdbRating', 'Unknown'),
            'imdbVotes': data.get('imdbVotes', 'Unknown'),
            'imdbID': data.get('imdbID', 'Unknown'),
            'type': data.get('Type', 'Unknown'),
            'dvd': data.get('DVD', 'Unknown'),
            'boxOffice': data.get('BoxOffice', 'Unknown'),
            'production': data.get('Production', 'Unknown'),
            'website': data.get('Website', 'N/A'),
        }
    return {
        'title': 'Unknown',
        'poster': 'https://via.placeholder.com/200x300?text=No+Image',
        'genres': 'Unknown',
        'year': 'Unknown',
        'rated': 'Unknown',
        'released': 'Unknown',
        'runtime': 'Unknown',
        'director': 'Unknown',
        'writer': 'Unknown',
        'actors': 'Unknown',
        'plot': 'No plot available',
        'language': 'Unknown',
        'country': 'Unknown',
        'awards': 'Unknown',
        'ratings': [],
        'metascore': 'Unknown',
        'imdbRating': 'Unknown',
        'imdbVotes': 'Unknown',
        'imdbID': 'Unknown',
        'type': 'Unknown',
        'dvd': 'Unknown',
        'boxOffice': 'Unknown',
        'production': 'Unknown',
        'website': 'N/A',
    }

def get_movie_details(imdbId):
    imdbId_str = str(imdbId)
    imdbId_with_tt = 'tt' + imdbId_str

    cached_movie = cache_table.get(Movie.imdbID == imdbId_str)
    if cached_movie:
        return cached_movie['details']

    # Fetch details using the thread pool executor
    future = executor.submit(fetch_movie_details, imdbId_with_tt)
    movie_details = future.result()
    
    if movie_details['title'] != "Unknown":
        cache_table.insert({'imdbID': imdbId_str, 'details': movie_details})
    
    return movie_details
