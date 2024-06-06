import tweepy

from config import api_key, api_secret, bearer_token, access_token, access_token_secret

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

client.create_tweet(text="testing...")