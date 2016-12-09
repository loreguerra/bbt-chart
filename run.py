import plotly.plotly as py
import plotly.graph_objs as go

from credentials import set_credentials

import psycopg2

conn = psycopg2.connect(database='bbt_chart', user='lorena', password='')

# from data import temps, dates

set_credentials()

dates = dates
temps = temps

#post plotly chart via twitter and @mention originating account (me) - requests.post / convert to binary
# cycle day 1 separate graph
#add color marker for temp spikes
#change usernames to variables

trace = go.Scatter(
    x = dates,
    y= temps
)

data = [trace]

plot_url = py.plot(data, filename='bbt')
#save image, convert to binary, post to twitter, import auth from data
