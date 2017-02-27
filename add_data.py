import psycopg2
import sys

from connect import connect_to_db

# add new date, temp, cycle day, LH test from arguments in command line
# filename counts as first arg
args = sys.argv
date = args[1]
temp = args[2]
cd = args[3]
lh = args[4]

# adding items to data
data = (date, temp, cd, lh)

# connect to database
conn = connect_to_db()
cur = conn.cursor()

# SQL for inserting values into db
SQL = "INSERT INTO BBT_CHART (DATE, TEMP, CYCLE_DAY, LH_TEST) VALUES (%s, %s, %s, %s);"

# execute SQL command plus data
cur.execute(SQL, data)

print "New data added"
conn.commit()
conn.close()
