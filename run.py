import plotly.plotly as py
import plotly.graph_objs as go

from credentials import set_credentials

from data import temps, dates

set_credentials()

# dates = [10, 11, 12, 13, 14, 15]
# temps = [97.36, 97.43, 97.37, 98.18, 96.9, 97.24]

dates = dates
temps = temps

#twitter api only goes back so far. Post to database?
#still post chart to twitter?
#post plotly chart via twitter and @mention originating account (me) - requests.post / convert to binary
#add hashtag for date
# cycle day 1 separate graph
#add color marker for temp spikes
#separate months and graph separately or on top of each other?
#change usernames to variables

trace = go.Scatter(
    x = dates,
    y= temps
)

data = [trace]

plot_url = py.plot(data, filename='bbt')
#save image, convert to binary, post to twitter, import auth from data
