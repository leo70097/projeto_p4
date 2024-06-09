import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.database = 'helpdesk'
        self.user = 'root'
        self.password = ''

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print(f"Error: {e}")
            return None

    def close(self, connection):
        if connection.is_connected():
            connection.close()