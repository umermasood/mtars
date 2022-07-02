import os
import requests
import pandas as pd

# Fetch the bearer token environment variable (used for authentication to access various API endpoints)
bearer_token = os.environ.get('BEARER_TOKEN')


def bearer_oauth(r):
    """
    Method required by bearer token authentication
    :param r:
    :return: r
    """
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


# Method for connecting to the API endpoint
def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


# Function for fetching tweets from the API and storing them
def fetch_tweets_from_api(query_params: dict, movie: str):
    """
    GET /2/tweets/search/recent Endpoint

    Rate Limit:
    - 180 requests / 15 minutes (PER USER)
    - 450 requests / 15 minutes (PER APP)

    Tweet Cap:
    - Yes

    Special Attributes:
    - 10 default results per response
    - 100 max results per response
    - 512 query length
    - Only core operator for queries are allowed
    :param query_params
    :param movie
    :return next_token
    """

    search_api_endpoint_url = "https://api.twitter.com/2/tweets/search/recent"

    # Search endpoint request for tweets
    json_response = connect_to_endpoint(search_api_endpoint_url, query_params)
    # print(json.dumps(json_response, indent=4, sort_keys=True))

    try:
        # next_token for paginating response documents for the matched query
        next_token = json_response['meta']['next_token']
    except KeyError:
        print("next_token doesn't exist")
        next_token = ''

    # Pandas dataframe for response tweets
    df = pd.DataFrame(data=json_response['data'])

    # Replace spaces with underscores
    filename = movie.replace(' ', '_')

    # Append the dataframe tweets to existing movie tweets
    # Append newly fetched tweets in the movie.csv in the tweets directory
    df.to_csv(f'tweets/{filename}.csv', mode='a', index=False, header=False)

    # Reading all tweets of the movie
    csv_df = pd.read_csv(f'tweets/{filename}.csv',
                         header=None, on_bad_lines='skip')
    # Renaming the dataframe header
    csv_df = csv_df.rename(columns={0: 'id', 1: 'text'})

    return next_token


def fetch_tweets_and_store(movies: list, request_count: int) -> None:
    # Loop through all movies
    for movie in movies:
        print('Fetching tweets for :', movie)
        # query_params for the first request without next_token
        query_params = {'query': f'"{movie}" lang:en', 'max_results': '100'}

        # Make first request for the movie and fetch it's next_token
        next_token = fetch_tweets_from_api(query_params, movie)

        # keep paginating - fetch more tweets until next_token is nil
        for _ in range(request_count):
            # if there's no next token, stop paginating
            if next_token == '':
                break
            else:
                # different query param for next_token query
                query_params = {'query': f'"{movie}" lang:en',
                                'max_results': '100', 'next_token': next_token}

                next_token = fetch_tweets_from_api(query_params, movie)

        # For every movie make ```request_count``` no of API requests
        # then continue for the next movie
