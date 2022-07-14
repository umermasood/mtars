"""
This file is for managing preprocessing for the raw Tweet Data.

potential functions:

remove duplicates
tokenization
stopwords removal
special characters removal
"""

import pandas as pd


def remove_duplicate_tweets(movies: list):
    for movie in movies:
        print('Removing duplicates for', movie)
        # Replace whitespaces in movie names with underscores to target the filenames
        filename = movie.replace(' ', '_')
        try:
            # read the raw data for the movie and store it in the dataframe
            df = pd.read_csv(f'tweets/{filename}.csv', header=None, on_bad_lines='skip')
            df = df.rename(columns={0: 'id', 1: 'text'})
            # Delete duplicate tweets
            df = df.drop_duplicates(subset='id')
            # Overwrite the original raw data file with unique tweets
            df.to_csv(f'tweets/{filename}.csv', index=False, header=None)
        except FileNotFoundError:
            continue
