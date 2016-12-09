import psycopg2

from settings import db_info

# set database info variables
database = db_info['database']
user = db_info['user']
password = db_info['password']

# open connection function
def connect_to_db():
    conn = psycopg2.connect(database=database, user=user, password=password)
    print 'Connected to %s' % database
    return conn

connect_to_db()
