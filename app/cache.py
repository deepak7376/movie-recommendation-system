from tinydb import TinyDB, Query

# Initialize TinyDB
db = TinyDB('data/movie_cache.json')
cache_table = db.table('cache')
Movie = Query()
