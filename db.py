import mysql.connector
import connect

def get_db_connection():
    return mysql.connector.connect(
        user=connect.db_user,
        password=connect.db_pass,
        host=connect.db_host,
        database=connect.db_name,
        autocommit=True
    )

def get_cursor(connection):
    return connection.cursor(dictionary=True, buffered=True)
