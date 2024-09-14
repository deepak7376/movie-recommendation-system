Testing the Backend
Using cURL:

Get all movies:
curl http://localhost:5000/movies


Get recommendations:
curl -X POST -H "Content-Type: application/json" -d '{"movie":"Toy Story (1995)"}' http://localhost:5000/recommend


Using Postman or Insomnia:
Send a POST request to http://localhost:5000/recommend with JSON body {"movie": "Inception"}.


http://www.omdbapi.com/?i=tt3896198&apikey=9db870d3

http://www.omdbapi.com/?i=tt0114709&apikey=9db870d3


Hosting a Flask backend and a static frontend (like an HTML site) separately on Heroku involves several steps. Here’s a guide on how to do it:

### 1. **Deploying the Flask Backend to Heroku**

**Step 1: Prepare Your Flask Backend**

Ensure your Flask app is ready for deployment. You should have a `Procfile`, `requirements.txt`, and optionally a `runtime.txt` if you need a specific Python version.

**File Structure:**
```
your_flask_backend/
│
├── app.py
├── requirements.txt
├── Procfile
└── runtime.txt (optional)
```

- **`requirements.txt`**: Lists all your Python dependencies.

  ```sh
  Flask==2.0.1
  flask-cors==3.0.10
  pandas==1.3.3
  requests==2.26.0
  tinydb==4.6.0
  ```

- **`Procfile`**: Tells Heroku how to run your app.

  ```
  web: python app.py
  ```

- **`runtime.txt`** (optional): Specifies the Python version.

  ```
  python-3.9.12
  ```

**Step 2: Initialize a Git Repository**

If you haven’t already, initialize a Git repository in your Flask backend directory.

```sh
cd your_flask_backend
git init
```

**Step 3: Commit Your Code**

```sh
git add .
git commit -m "Initial commit"
```

**Step 4: Create a Heroku App**

Create a new Heroku app and push your code.

```sh
heroku create your-flask-backend-app-name
git push heroku master
```

**Step 5: Set Environment Variables**

If your app uses environment variables (like API keys), set them using the Heroku CLI.

```sh
heroku config:set OMDB_API_KEY=your_omdb_api_key
```

**Step 6: Open Your App**

You can now open your Flask app in the browser.

```sh
heroku open
```

### 2. **Deploying the Static Frontend to Heroku**

**Step 1: Prepare Your Frontend**

Your frontend should be a static site (e.g., HTML, CSS, JavaScript files). Create a simple server using `Flask` or `Static Server` to serve these files.

**File Structure:**
```
your_frontend/
│
├── index.html
├── recommendation.html
└── Procfile
```

- **`Procfile`**: This file should contain the command to start your static server.

  ```
  web: python -m http.server 8000
  ```

**Note:** You can use the `http.server` module if you have Python 3.x. If you’re using a different server, adjust the command accordingly.

**Step 2: Initialize a Git Repository**

Initialize a Git repository in your frontend directory.

```sh
cd your_frontend
git init
```

**Step 3: Commit Your Code**

```sh
git add .
git commit -m "Initial commit"
```

**Step 4: Create a Heroku App**

Create a new Heroku app for your frontend and push your code.

```sh
heroku create your-frontend-app-name
git push heroku master
```

**Step 5: Open Your App**

You can now open your static site in the browser.

```sh
heroku open
```

### 3. **Connecting Frontend and Backend**

1. **API Calls:** Ensure your frontend makes API calls to the correct backend URL. In your JavaScript, replace `'http://localhost:5000/movies'` with the URL of your Heroku backend app.

   ```javascript
   async function fetchMovies() {
       const response = await fetch('https://your-flask-backend-app-name.herokuapp.com/movies');
       const movies = await response.json();
       displayMovies(movies);
   }
   ```

2. **CORS:** Make sure your Flask backend allows requests from your frontend’s domain. You should configure CORS to allow your frontend's domain.

   ```python
   from flask_cors import CORS

   app = Flask(__name__)
   CORS(app, resources={r"/*": {"origins": "https://your-frontend-app-name.herokuapp.com"}})
   ```

### Summary

1. **Deploy Flask Backend**:
   - Prepare the Flask app.
   - Initialize Git and commit code.
   - Create and deploy to a Heroku app.
   - Set environment variables and open the app.

2. **Deploy Static Frontend**:
   - Prepare the static files.
   - Initialize Git and commit code.
   - Create and deploy to a Heroku app.
   - Open the static site.

3. **Connect**:
   - Update your frontend to call the correct backend API URLs.
   - Ensure CORS settings are configured properly.

This setup ensures that your frontend and backend are deployed separately but can communicate with each other.

{
    "Title": "Guardians of the Galaxy Vol. 2",
    "Year": "2017",
    "Rated": "PG-13",
    "Released": "05 May 2017",
    "Runtime": "136 min",
    "Genre": "Action, Adventure, Comedy",
    "Director": "James Gunn",
    "Writer": "James Gunn",
    "Actors": "Chris Pratt, Zoe Saldana, Dave Bautista, Vin Diesel",
    "Plot": "The Guardians must fight to keep their newfound family together as they unravel the mystery of Peter Quill's true parentage.",
    "Language": "English",
    "Country": "USA",
    "Awards": "Nominated for 1 Oscar. 7 wins & 41 nominations total.",
    "Poster": "https://m.media-amazon.com/images/M/MV5BMjA2MTkxOTI2NF5BMl5BanBnXkFtZTgwNDMwMzMwMDI@._V1_SX300.jpg",
    "Ratings": [
        {
            "Source": "Internet Movie Database",
            "Value": "7.6/10"
        }
    ],
    "Metascore": "67",
    "imdbRating": "7.6",
    "imdbVotes": "380,870",
    "imdbID": "tt3896198",
    "Type": "movie",
    "DVD": "22 Aug 2017",
    "BoxOffice": "$389,813,101",
    "Production": "Walt Disney Pictures",
    "Website": "N/A",
    "Response": "True"
}
