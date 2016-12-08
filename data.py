import psycopg2

from settings import db_info

database = db_info['database']
user = db_info['user']
password = db_info['password']

conn = psycopg2.connect(database=database, user=user, password=password)

def create_temps_table():
    cur = conn.cursor()
    cur.execute(''' CREATE TABLE BBT_CHART; ''')
    print 'Table created successfully'
    conn.commit()
