import mysql.connector

db_user = "root"
db_pass = "123456"
db_host = "localhost"
db_name = "biosecurity"

def get_db_connection():
    connection = mysql.connector.connect(
        user=db_user,
        password=db_pass,
        host=db_host,
        database=db_name
    )
    return connection