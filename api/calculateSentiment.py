import pandas as pd
from setRatings import set_ratings
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def calculate_sentiment(movies: list):
    # list of sentiment dictionaries containing sentiment scores
    sentiments = []

    for movie in movies:
        print('Calculating Sentiment for', movie)
        # Replace whitespaces in movie names with underscores to target the filenames
        filename = movie.replace(' ', '_')
        # read the raw data for the movie and store it in the dataframe
        try:
            df = pd.read_csv(f'tweets/{filename}.csv', header=None, on_bad_lines='skip')
            if len(df.columns) == 2:
                df.columns = ['id', 'text']
            elif len(df.columns) == 3:
                df.columns = ['id', 'text', 'sentiment']

            for tweet in df['text']:
                score = SentimentIntensityAnalyzer().polarity_scores(text=tweet)
                neg_score = score['neg']
                pos_score = score['pos']

                if neg_score > pos_score:
                    sentiments.append('neg')
                elif pos_score > neg_score:
                    sentiments.append('pos')
                else:
                    sentiments.append('neu')

            sentiment_col = pd.Series(data=sentiments, dtype=str)
            df['sentiment'] = sentiment_col
            df.to_csv(f'tweets/{filename}.csv', mode='w+', index=None, header=None)

            ratings = sentiment_col.value_counts().to_dict()
            # update ratings
            set_ratings(movie, ratings)
        except FileNotFoundError:
            continue
