import psycopg2
import sys

from connect import connect_to_db

# add new temperature and date from arguments in command line
# filename counts as first arg
args = sys.argv
date_to_edit = args[1] # second arg

# adding items to data
data = (date_to_edit)

# connect to database
conn = connect_to_db()
cur = conn.cursor()

# SQL for inserting values into db
SQL = "DELETE from BBT_CHART WHERE DATE = (%s);"

# execute SQL command plus data
cur.execute(SQL, data)

print "Entry deleted"
conn.commit()
conn.close()
