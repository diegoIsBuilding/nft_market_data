import config
import psycopg2

connection = None
cursor = None

try:
    #This will open a session to the database where we will be able to perform 
    #database querys and other stuff
    connection = psycopg2.connect(
        host = config.hostname,
        dbname = config.database,
        user = config.username,
        password = config.password,
        port = config.port    
    )

    cursor = connection.cursor()
    
except Exception as error:
    print(error)
    
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()