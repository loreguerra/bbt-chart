import psycopg2

from settings import db_info

import sys

# add getopt for options via command line

database = db_info['database']
user = db_info['user']
password = db_info['password']

def connect_to_db():
    conn = psycopg2.connect(database=database, user=user, password=password)
    return conn

def create_temps_table():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE BBT_CHART
            (ID INT PRIMARY KEY  NOT NULL,
            DATE DATE   NOT NULL,
            TEMP REAL   NOT NULL);""")
    print 'Table created successfully'
    conn.commit()
    conn.close()

def add_temp():

connect_to_db()
create_temps_table()
