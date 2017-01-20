import plotly.plotly as py
import plotly.graph_objs as go

from credentials import set_credentials

import psycopg2

from connect import connect_to_db

# set plotly credentials
set_credentials()

conn = connect_to_db()
cur = conn.cursor()

# selecting all rows
cur.execute("SELECT DATE, TEMP from BBT_CHART")
rows = cur.fetchall()
# sorting rows
rows = sorted(rows)

dates = list(row[0] for row in rows)
temps = list(row[1] for row in rows)

#post plotly chart via twitter and @mention originating account (me) - requests.post / convert to binary

data = go.Scatter(
    x = dates,
    y = temps
)

layout = go.Layout()


figure = go.Figure(data=[data], layout=layout)


plot_url = py.plot(figure, filename='bbt')
