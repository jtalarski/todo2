import psycopg2
import psycopg2.extras


DB_NAME = "python-to-do-app"
DB_HOST = "localhost"
DB_PORT = "5432"

con = psycopg2.connect(
    database=  DB_NAME, host= DB_HOST, cursor_factory=psycopg2.extras.RealDictCursor
) 

print ("Database Connected")

