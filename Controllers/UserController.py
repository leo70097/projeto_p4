from aifc import Error
from Models.Users import Users
from Utils.db import Database
class UserController:
    
    @staticmethod
    def register(nome, password, cargo):
        db = Database()
        connection = db.connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Users (nome, pass, cargo) VALUES (%s, %s, %s)", (nome, password, cargo))
            connection.commit()
            cursor.close()
            connection.close()

    @staticmethod
    def login(nome, password):
        db = Database()
        connection = db.connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Users WHERE nome = %s AND pass = %s", (nome, password))
            user = cursor.fetchone()
            cursor.close()
            connection.close()
            if user:
                return Users(*user)
        return None