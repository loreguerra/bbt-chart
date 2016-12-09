import psycopg2
import sys

from connect import connect_to_db

# add argparse for options via command line

# add new temperature and date
args = sys.argv
date = args[1]
temp = args[2]

data = (date, temp)

conn = connect_to_db()
cur = conn.cursor()
SQL = "INSERT INTO BBT_CHART (DATE, TEMP) VALUES (%s, %s);"
cur.execute(SQL, data)
conn.commit()
conn.close()
