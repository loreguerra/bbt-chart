import plotly.plotly as py
import plotly.graph_objs as go

from credentials import set_credentials

from data import temps, dates

set_credentials()

# days = [10, 11, 12, 13, 14]
# temps = [97.36, 97.43, 97.37, 98.18, 96.9]

dates = dates
temps = temps

#post plotly chart via twitter and @mention originating account (me)
#add hashtag for date
#add color marker for cycle day 1
#add color marker for temp spikes
#separate months and graph separately or on top of each other?

trace = go.Scatter(
    x = dates,
    y= temps
)

data = [trace]

plot_url = py.plot(data, filename='bbt')
