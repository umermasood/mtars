# ---------------------------------------------------------------------------- #
#                              FLASK BACKEND
# ---------------------------------------------------------------------------- #
import os
import pandas as pd
from flask import Flask, request
from tmdb import fetch_trending_movies
from twitterapi import fetch_tweets_and_store
from preprocess import remove_duplicate_tweets
from apscheduler.schedulers.background import BackgroundScheduler

ITERATION_COUNT = 0

app = Flask(__name__)


# ---------------------------------------------------------------------------- #
#                              RATING ENDPOINT
# ---------------------------------------------------------------------------- #
@app.route('/mtarsrating', methods=['GET'])
def get_mtars_rating():
    """
    Accepts a movie name as an argument and returns its MTARS rating
    :return: response -> i.e. 7.5
    """
    movie_name = request.args.get('movie', type=str)

    df = pd.read_csv('./ratings.csv', index_col=0)
    try:
        rating = df.loc[movie_name]['rating']
    except KeyError:
        rating = 0.0

    # Here we will return the MTARS Rating for the movie
    return {'response': f'{rating}'}


# ---------------------------------------------------------------------------- #
#                              BACKEND ITERATION
# ---------------------------------------------------------------------------- #
def backend_iteration():
    trending_movies = fetch_trending_movies()
    print(trending_movies)

    # For each movie, pull tweets from the Twitter API
    fetch_tweets_and_store(trending_movies, request_count=10)

    # At this point, raw data have been fetched for every trending movie

    # For every movie, remove duplicates from the raw data
    remove_duplicate_tweets(trending_movies)

    global ITERATION_COUNT
    ITERATION_COUNT += 1
    print(f'Iteration {str(ITERATION_COUNT)} Ended')


# ---------------------------------------------------------------------------- #
#                              JOB SCHEDULER
#
# Automates the entire process of fetching, preprocessing and classifying tweets
# ---------------------------------------------------------------------------- #
if not app.debug or os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=backend_iteration,
                      trigger="interval", minutes=60)
    scheduler.start()
    backend_iteration()


# ---------------------------------------------------------------------------- #
#                              ENTRY POINT
# ---------------------------------------------------------------------------- #
if __name__ == '__main__':
    app.run()
