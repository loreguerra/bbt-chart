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

high_temps = list(row for row in rows if row[1] >= 97.5)
reg_temps = list(row for row in rows if row[1] < 97.5)

reg_temp_dates = list(row[0] for row in reg_temps)
reg_temp_data = list(row[1] for row in reg_temps)

high_temps_dates = []
high_temp_data = []

#post plotly chart via twitter and @mention originating account (me) - requests.post / convert to binary

data = [

    go.Scatter(
        x = dates,
        y = temps,
        mode = 'lines+markers',
        marker = dict (
            size=10,
            color='rgb(199,199,199)'
        )
    )
]

layout = go.Layout(
    yaxis= dict()
)


figure = go.Figure(data=data, layout=layout)


plot_url = py.plot(figure, filename='bbt')
