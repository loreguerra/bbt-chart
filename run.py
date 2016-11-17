import plotly.plotly as py
import plotly.graph_objs as go

import requests
from requests.auth import OAuth1

from credentials import *

set_credentials()

days = [10, 11, 12, 13, 14]
temps = [97.36, 97.43, 97.37, 98.18, 96.9]

#install twitter tools, get data, clean up data, organize data
#gather data from @mentions on bbt_chart timeline with run.py
#post plotly chart via twitter and @mention originating account (me)
#add color marker for cycle day 1
#add color marker for temp spikes

trace = go.Scatter(
    x = days,
    y= temps
)

data = [trace]

plot_url = py.plot(data, filename='bbt')
