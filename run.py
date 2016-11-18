import plotly.plotly as py
import plotly.graph_objs as go

from credentials import set_credentials

set_credentials()

# days = [10, 11, 12, 13, 14]
# temps = [97.36, 97.43, 97.37, 98.18, 96.9]

dates = ['11-18-2016', '11-17-2016', '11-16-2016']
temps = [97.36, 97.32, 96.69]

#post plotly chart via twitter and @mention originating account (me)
#add color marker for cycle day 1
#add color marker for temp spikes
#separate months and graph separately or on top of each other?

trace = go.Scatter(
    x = dates,
    y= temps
)

data = [trace]

plot_url = py.plot(data, filename='bbt')
