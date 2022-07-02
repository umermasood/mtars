# ---------------------------------------------------------------------------- #
#                              FLASK BACKEND
# ---------------------------------------------------------------------------- #

from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/mtarsrating', methods=['GET'])
def get_mtars_rating():
    """
    Accepts a movie name as an argument and returns its MTARS rating
    :return: response -> i.e. 7.5
    """
    movie_name = request.args.get('movie', type=str)

    # Here we will return the MTARS Rating for the movie
    return {'response': f'{movie_name} rating'}
