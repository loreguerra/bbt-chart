import psycopg2
import sys

from connect import connect_to_db

# add argparse for options via command line

# add new temperature and date
def add_temp(date, temp):
    print date, temp
    # conn = connect_to_db()
