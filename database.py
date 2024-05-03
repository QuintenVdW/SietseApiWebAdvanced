import mysql.connector
from .config import DB_HOST, DB_USER, DB_PASSWORD

def connect_to_database():
    try:
        connection = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD)
        return connection
    except mysql.connector.Error as error:
        print("Error connecting to database:", error)
        return error

def execute_sql_query(sql_query, query_parameters=None):
    connection = connect_to_database()
    result = ''
    try:
        cursor = connection.cursor()
        cursor.execute(sql_query, query_parameters)
        if sql_query.upper().startswith("SELECT"):
            result = cursor.fetchall()
        else:
            connection.commit()
            result = True

        cursor.close()

    except mysql.connector.Error as exception:
        print("Error executing SQL query:", exception)
        result = exception

    finally:
        if connection.is_connected():
            connection.close()

        return result
