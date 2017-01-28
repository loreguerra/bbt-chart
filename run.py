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
cur.execute("SELECT * from BBT_CHART")
rows = cur.fetchall()
# sorting rows
rows = sorted(rows)

# put all data into lists for graphing as x,y underlaying graph
all_dates = list(row[0] for row in rows)
all_temps = list(row[1] for row in rows)

# separate high and regular dates and temps based on temp
high_data = list(row for row in rows if row[1] >= 97.6)
reg_data = list(row for row in rows if row[1] < 97.6)

# separate high temp dates and reg temp dates into lists for use as x axis
high_dates = list(row[0] for row in high_data)
reg_dates = list(row[0] for row in reg_data)

# separate high temps and reg temps into lists for use as y axis
high_temps = list(row[1] for row in high_data)
reg_temps = list(row[1] for row in reg_data)

# list dates for cycle day 1
cycle_days = list(row[0] for row in rows if row[2] == 'cd1')
cycle_day_temps = list(row[1] for row in rows if row[2] == 'cd1')

# list dates for positive LH test
pos_lh = list(row[0] for row in rows if row[3] == '+')
pos_lh_temps = list(row[1] for row in rows if row[3] == '+')

#post plotly chart via twitter and @mention originating account (me) - requests.post / convert to binary

data = [

    go.Scatter(           # first layer line graph for total data
        x = all_dates,
        y = all_temps,
        mode = 'lines',
        marker = dict (
            color='rgb(199,199,199)'
        ),
        showlegend = False,
        hoverinfo = 'skip',
    ),
        go.Scatter(      # second layer dot graph for positive LH
            x = pos_lh,
            y = pos_lh_temps,
            mode = 'markers',
            marker = dict (
                size=15,
                color='rgb(2, 209, 171)'
            ),
            name = 'Positive LH',
            hoverinfo = 'skip',
        ),

    go.Scatter(          # third layer dot graph for regular data
        x = reg_dates,
        y = reg_temps,
        mode = 'markers',
        marker = dict (
            size=10,
            color='rgb(199,199,199)'
        ),
        name = 'Normal temps'
    ),

        go.Scatter(      # fourth layer dot graph for high data
            x = high_dates,
            y = high_temps,
            mode = 'markers',
            marker = dict (
                size=10,
                color='rgb(244,66,98)'
            ),
            name = 'High temps'
        ),

            go.Scatter(      # fifth layer dot graph for cycle day 1
                x = cycle_days,
                y = cycle_day_temps,
                mode = 'markers',
                marker = dict (
                    size=10,
                    color='rgb(116,66,244)'
                ),
                name = 'Cycle day 1',
                hoverinfo = 'skip',
            ),


]

layout = go.Layout(
    yaxis= dict()
)


figure = go.Figure(data=data, layout=layout)


plot_url = py.plot(figure, filename='bbt')
