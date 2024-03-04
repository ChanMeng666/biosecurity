from .db_connection import get_db_connection

def check_db_connection():
    global connection
    try:
        connection = get_db_connection()
        if connection.is_connected():
            print("Database connection is successful.")
        else:
            print("Failed to connect to the database.")
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
    finally:
        connection.close()

check_db_connection()