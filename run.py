import plotly.plotly as py
import plotly.graph_objs as go

from credentials import set_credentials

import psycopg2

from connect import connect_to_db

# set plotly credentials
set_credentials()

conn = connect_to_db()
cur = conn.cursor()

# selecting date rows
cur.execute("SELECT DATE, TEMP from BBT_CHART")
rows = cur.fetchall()
rows = sorted(rows)

dates = list(row[1] for row in rows)
print dates

#post plotly chart via twitter and @mention originating account (me) - requests.post / convert to binary
# cycle day 1 separate graph
#add color marker for temp spikes

# trace = go.Scatter(
#     x = dates,
#     y = temps
# )
#
# data = [trace]
#
# plot_url = py.plot(data, filename='bbt')
# #save image, convert to binary, post to twitter, import auth from data
