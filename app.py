import tweepy
import os
from decouple import config
import requests

CONSUMER_KEY=config('CONSUMER_KEY')
CONSUMER_SECRET=config('CONSUMER_SECRET')
ACCESS_TOKEN=config('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET=config('ACCESS_TOKEN_SECRET')
BEARER_TOKEN=config('BEARER_TOKEN')

session = requests.session()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    redirect_url = auth.get_authorization_url()
    auth._get_request_token
    user = api.get_user("@pittsburgtoilet")
    api.update_status(status="And then I got in.")
except tweepy.TweepError:
    print('Error! Failed to get request token.')