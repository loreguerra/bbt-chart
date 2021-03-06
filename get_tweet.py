import requests
from requests_oauthlib import OAuth1

from datetime import datetime

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

# CHECK IF DATE ALREADY EXISTS

# http://stackoverflow.com/questions/4460262/running-a-python-script-with-cron
# https://twitter.com/search?f=tweets&vertical=default&q=to%3Abbt_chart%20from%3Alorenaelise&src=typd


def get_temp_data(tweet):
    tweet = tweet.split(' ')
    temp = tweet[1]
    return temp
    # temp = filter(lambda x: x.isdigit(), tweet)
    # temp = float(temp) / 100
    # return temp

def get_date(tweet):
    values_to_keep = [1,2,5]
    raw_date = tweet.split(' ')
    date = list(raw_date[x] for x in values_to_keep)
    date = ' '.join(date)
    date = datetime.strptime(date, '%b %d %Y')
    return date

temps = list(get_temp_data(tweet_data[i]['text']) for i in range(tweet_count))

dates = list(get_date(tweet_data[i]['created_at']) for i in range(tweet_count))


# dump data for viewing
# with open('data.json', 'w') as f:
#     json.dump(data, f)
