import os
import requests


def fetch_trending_movies():
    # Endpoint url
    tmdb_key = os.environ.get('TMDB_API_KEY')
    tmdb_endpoint_url = f'https://api.themoviedb.org/3/movie/popular?api_key={tmdb_key}&language=en-US'

    # List of trending movies
    trending_movies = []

    # Connecting to the API endpoint and fetching trending movies
    response = requests.get(tmdb_endpoint_url).json()
    for movie in response['results']:
        trending_movies.append(movie['original_title'])
    return trending_movies
