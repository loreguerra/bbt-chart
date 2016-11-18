import requests
from requests_oauthlib import OAuth1

import json

from credentials import *

url = 'https://api.twitter.com/1.1/search/tweets.json?f=tweets&q=to%3Abbt_chart%20from%3Alorenaelise'

consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

r = requests.get(url, auth=auth)
data = r.json()

tweet_data = data['statuses']
tweet_count = len(tweet_data)

dates = []

def get_temp(tweet):
    temp = filter(lambda x: x.isdigit(), tweet)
    temp = float(temp) / 100
    return temp

# def get_date(tweet):
#

temps = list(get_temp(tweet_data[i]['text']) for i in range(tweet_count))

print tweet_data[0]['created_at']
# may have to reverse lists to display correctly - 0 is newest tweet and should be oldest

# date is 'created_at'

# dump data for viewing
# with open('data.json', 'w') as f:
#     json.dump(data, f)
