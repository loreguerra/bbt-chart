import requests
from requests_oauthlib import OAuth1

from credentials import *

url = u'https://api.twitter.com/1.1/account/settings.json'

consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret

query_oauth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret, signature_type='query')

r = request.get(url, auth=query_oauth)
