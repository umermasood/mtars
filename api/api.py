# ---------------------------------------------------------------------------- #
#                              FLASK BACKEND
# ---------------------------------------------------------------------------- #
import os
import re
import pandas as pd
from flask import Flask, request, jsonify
from tmdb import fetch_trending_movies
from twitterapi import fetch_tweets_and_store
from preprocess import remove_duplicate_tweets
from calculateSentiment import calculate_sentiment
from apscheduler.schedulers.background import BackgroundScheduler

ITERATION_COUNT = 0

app = Flask(__name__, static_folder='../build', static_url_path='/')


# ---------------------------------------------------------------------------- #
#                              ROOT ENDPOINT
# ---------------------------------------------------------------------------- #
@app.route('/')
def index():
    return app.send_static_file('index.html')


# ---------------------------------------------------------------------------- #
#                              RATING ENDPOINT
# ---------------------------------------------------------------------------- #
@app.route('/api/mtarsrating', methods=['GET'])
def get_mtars_rating():
    """
    Accepts a movie name as an argument and returns its MTARS rating
    :return: response -> i.e. 7.5
    """
    movie_name = request.args.get('movie', type=str)

    df = pd.read_csv('ratings.csv', header=None, index_col=0)
    df.columns = ['pos', 'neg']

    sentiment = df.loc[movie_name]

    rating = {'pos': int(sentiment.pos), 'neg': int(sentiment.neg)}
    print(rating)

    # Here we will return the MTARS Rating for the movie
    return {'response': rating}


# ---------------------------------------------------------------------------- #
#                              BACKEND ITERATION
# ---------------------------------------------------------------------------- #
def backend_iteration():
    # trending_movies = fetch_trending_movies()
    # # Valid trending movie names
    # movies = []
    # regexp = re.compile(r'[A-Z]')
    #
    # for movie in trending_movies:
    #     if bool(regexp.match(movie)):
    #         movies.append(movie)
    # # Print trending movies
    # print(movies)
    #
    # # For each movie, pull tweets from the Twitter API
    # # fetch_tweets_and_store(movies, request_count=10)
    #
    # # At this point, raw data have been fetched for every trending movie
    #
    # # For every movie, remove duplicates from the raw data
    # print('Removing duplicates')
    # remove_duplicate_tweets(movies)
    #
    # # Perform sentiment analysis of all tweets of every movie
    # print('Calculating sentiment')
    # calculate_sentiment(movies)

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
                      trigger="interval", hours=24)
    scheduler.start()
    # backend_iteration()


# ---------------------------------------------------------------------------- #
#                              ENTRY POINT
# ---------------------------------------------------------------------------- #
if __name__ == '__main__':
    app.run()
