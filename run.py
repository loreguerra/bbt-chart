import plotly.plotly as py
import plotly.graph_objs as go
from set_credentials import set_credentials

set_credentials()

days = [10, 11, 12, 13]
temps = [97.36, 97.43, 97.37, 98.18]

trace = go.Scatter(
    x = days,
    y= temps
)

data = [trace]

plot_url = py.plot(data, filename='bbt')
