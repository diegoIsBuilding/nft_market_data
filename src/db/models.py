import config
import psycopg2

connection = psycopg2.connect(
    host = config.hostname,
    dbname = config.database,
    user = config.username,
    password = config.password,
    port = config.port    
)



connection.close()