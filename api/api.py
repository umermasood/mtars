# ---------------------------------------------------------------------------- #
#                              FLASK BACKEND
# ---------------------------------------------------------------------------- #
import os
from flask import Flask, request
from tmdb import fetch_trending_movies
from apscheduler.schedulers.background import BackgroundScheduler


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

    # Here we will return the MTARS Rating for the movie
    return {'response': f'{movie_name} rating'}


# ---------------------------------------------------------------------------- #
#                              BACKEND ITERATION
# ---------------------------------------------------------------------------- #
def backend_iteration():
    trending_movies = fetch_trending_movies()
    print(trending_movies)


# ---------------------------------------------------------------------------- #
#                              JOB SCHEDULER
#
# Automates the entire process of fetching, preprocessing and classifying tweets
# ---------------------------------------------------------------------------- #
def job_scheduler():
    if not app.debug or os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        scheduler = BackgroundScheduler()
        scheduler.add_job(func=backend_iteration,
                          trigger="interval", seconds=5)
        scheduler.start()


# ---------------------------------------------------------------------------- #
#                              ENTRY POINT
# ---------------------------------------------------------------------------- #
job_scheduler()
