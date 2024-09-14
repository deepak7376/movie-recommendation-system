import requests

# OMDb API key and base URL
OMDB_API_KEY = '9db870d3'
OMDB_API_URL = 'http://www.omdbapi.com/'

# Sample IMDb ID (without 'tt' prefix)
sample_imdb_id = '46889'  # Example: "The Shawshank Redemption"

# Prepend 'tt' to the IMDb ID
imdb_id_with_tt = 'tt' + sample_imdb_id

# Fetch details from OMDb API
response = requests.get(OMDB_API_URL, params={
    'i': imdb_id_with_tt,
    'apikey': OMDB_API_KEY
})

# Check if the response is successful
if response.status_code == 200:
    data = response.json()
    print("Movie Details:")
    print(f"Title: {data.get('Title', 'Unknown')}")
    print(f"Poster: {data.get('Poster', 'https://via.placeholder.com/200x300?text=No+Image')}")
    print(f"Genres: {data.get('Genre', 'Unknown')}")
    print(f"Year: {data.get('Year', 'Unknown')}")
    print(f"Rated: {data.get('Rated', 'Unknown')}")
    print(f"Released: {data.get('Released', 'Unknown')}")
    print(f"Runtime: {data.get('Runtime', 'Unknown')}")
    print(f"Director: {data.get('Director', 'Unknown')}")
    print(f"Writer: {data.get('Writer', 'Unknown')}")
    print(f"Actors: {data.get('Actors', 'Unknown')}")
    print(f"Plot: {data.get('Plot', 'No plot available')}")
    print(f"Language: {data.get('Language', 'Unknown')}")
    print(f"Country: {data.get('Country', 'Unknown')}")
    print(f"Awards: {data.get('Awards', 'Unknown')}")
    print(f"Ratings: {data.get('Ratings', [])}")
    print(f"Metascore: {data.get('Metascore', 'Unknown')}")
    print(f"IMDB Rating: {data.get('imdbRating', 'Unknown')}")
    print(f"IMDB Votes: {data.get('imdbVotes', 'Unknown')}")
    print(f"IMDB ID: {data.get('imdbID', 'Unknown')}")
    print(f"Type: {data.get('Type', 'Unknown')}")
    print(f"DVD: {data.get('DVD', 'Unknown')}")
    print(f"Box Office: {data.get('BoxOffice', 'Unknown')}")
    print(f"Production: {data.get('Production', 'Unknown')}")
    print(f"Website: {data.get('Website', 'N/A')}")
else:
    print(f"Failed to fetch data: {response.status_code}")
