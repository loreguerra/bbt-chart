import psycopg2
import sys

from connect import connect_to_db

# edit data from arguments in command line
# filename counts as first arg
args = sys.argv
date_to_edit = args[1] # second arg
new_lh = args[2] #third arg

# adding items to data
data = (new_lh, date_to_edit)

# connect to database
conn = connect_to_db()
cur = conn.cursor()

# SQL for inserting values into db
SQL = "UPDATE BBT_CHART SET LH_TEST = (%s) WHERE DATE = (%s);"

# execute SQL command plus data
cur.execute(SQL, data)

print "LH changed"
conn.commit()
conn.close()
