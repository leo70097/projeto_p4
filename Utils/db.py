import mysql.connector
from mysql.connector import Error

class Database:

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                db='helpdesk'
            )
            return connection
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")
            return None

    def close(self, connection):
        try:
            if connection.is_connected():
                connection.close()
                print("MySQL connection closed")
        except Error as e:
            print(f"Error closing MySQL connection: {e}")