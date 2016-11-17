import requests
from requests_oauthlib import OAuth1

from credentials import *

url = 'https://api.twitter.com/1.1/account/settings.json'

consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

requests.get(url, auth=auth)
