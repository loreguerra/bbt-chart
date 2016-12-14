import psycopg2
import sys

from connect import connect_to_db

# add argparse for options via command line

# add new temperature and date from arguments in command line
# filename counts as first arg
args = sys.argv
date = args[1] # second arg
temp = args[2] # third arg

# adding items to data
data = (date, temp)

# connect to database
conn = connect_to_db()
cur = conn.cursor()

# SQL for inserting values into db
SQL = "INSERT INTO BBT_CHART (DATE, TEMP) VALUES (%s, %s);"

# execute SQL command plus data
cur.execute(SQL, data)

print "Temperature data added"
conn.commit()
conn.close()
