import pandas as pd


def set_ratings(movie, ratings):
    print(movie, ratings)
    try:
        df1 = pd.read_csv('ratings.csv', header=None, index_col=0)
        df1.columns = ['pos', 'neg']
        df2 = pd.DataFrame(data=[[ratings['pos'], ratings['neg']]], index=[movie], columns=['pos', 'neg'])
        # Rather than concat, use df.loc[movie] to update the ratings for movie, rather than appending
        pd.concat([df1, df2], axis=0).to_csv('ratings.csv', columns=['pos', 'neg'], header=False)
    except FileNotFoundError:
        df = pd.DataFrame(data=[[ratings['pos'], ratings['neg']]], index=[movie], columns=['pos', 'neg'])
        df.to_csv('ratings.csv', columns=['pos', 'neg'], header=False)
