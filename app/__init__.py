from flask import Flask
from flask_cors import CORS
from tinydb import TinyDB

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS
    
    # Load configuration
    app.config.from_object('app.config.Config')

    # Initialize TinyDB
    app.config['DB'] = TinyDB('data/movie_cache.json')
    
    with app.app_context():
        from . import routes
        
    return app
