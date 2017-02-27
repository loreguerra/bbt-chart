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

rows = cur.fetchall()

for row in rows:
    print row[0] + '\n'


conn.commit()
conn.close()
