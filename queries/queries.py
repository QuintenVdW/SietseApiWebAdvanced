import mysql.connector
from mysql.connector import Error
from ..config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def create_connection():
    # Function to create a connection to the MySQL database.
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def get_recent_community_tiles():
    # Function to retrieve recent tiles added after the first 4 static ones.
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM CommunityPosts ORDER BY timestamp DESC LIMIT 4, 100"
            cursor.execute(query)
            recent_tiles = cursor.fetchall()
            return recent_tiles
        except Error as e:
            print(f"Error executing SQL query: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection closed")
    return None
