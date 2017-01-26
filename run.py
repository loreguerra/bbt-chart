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

high_data = list(row for row in rows if row[1] >= 97.5)
reg_data = list(row for row in rows if row[1] < 97.5)

high_dates = list(row[0] for row in high_data)
reg_dates = list(row[0] for row in reg_data)

high_temps = list(row[1] for row in high_data)
reg_temps = list(row[1] for row in reg_data)

#post plotly chart via twitter and @mention originating account (me) - requests.post / convert to binary

data = [

    go.Scatter(
        x = reg_dates,
        y = reg_temps,
        mode = 'markers',
        marker = dict (
            size=10,
            color='rgb(199,199,199)'
        )
    ),

        go.Scatter(
            x = high_dates,
            y = high_temps,
            mode = 'markers',
            marker = dict (
                size=10,
                color='rgb(244,66,98)'
            )
        )

]

layout = go.Layout(
    yaxis= dict()
)


figure = go.Figure(data=data, layout=layout)


plot_url = py.plot(figure, filename='bbt')
