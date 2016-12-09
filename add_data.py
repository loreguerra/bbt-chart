import psycopg2
import sys

from connect import connect_to_db

# add argparse for options via command line

# add new temperature and date
conn = connect_to_db()
cur = conn.cursor()
print sys.argv
