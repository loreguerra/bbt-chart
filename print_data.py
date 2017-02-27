import psycopg2
import sys

from connect import connect_to_db

# connect to database
conn = connect_to_db()
cur = conn.cursor()

# SQL for inserting values into db
SQL = "SELECT * FROM BBT_CHART ORDER BY DATE;"

# execute SQL command plus data
cur.execute(SQL)

# add rows to variable
rows = cur.fetchall()

# loop over rows, for each row, create temporary variables to hold info
for row in rows:
    # loop and list keys/values, convert to string and assign to vars
    a, b, c, d = list(str(row[i]) for i in range(0,4))
    # print variables with string formatting
    print '%s \n%s \ncycle day: %s \nLH test: %s\n' % (a, b, c, d)

conn.commit()
conn.close()
