###########################################
#Program to determine how certain user's tweets affect the stock market
#
#By Brian Worts
#
#
############################################


import os
import tweepy as tw
import pandas as pd

consumer_key= 'XjBv633JZ25I2eICiKfpgN6PF'
consumer_secret= 'wUkPdrC1ICoTimKAItB5mJHBPEQ0gjW4Yf20jQOYtB4HqzoIGS'
access_key= '1215408444649414662-HMMWb7GQwTytSshzQGbfhznta8afqG'
access_secret= '9CUgx59KJueOmP0nclZ2kxDiHLqE9B6OkHJJ69mYZGciy'


def get_tweets(username):
    auth = tw.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_key, access_secret) 

    api = tw.API(auth) 
    number_of_tweets= 5
    
    tweets = api.user_timeline(screen_name=username, count = number_of_tweets) 
    
    tweets_for_csv = [{tweet.text, tweet.created_at} for tweet in tweets]
    
    df = pd.DataFrame()
    
    
    for j in tweets_for_csv: 
        tmp=pd.DataFrame({'Tweet': [j]})
        df = df.append(tmp, ignore_index = True)

    print(df)

def main():
    username = "realDonaldTrump"
    get_tweets(username)
    
main()