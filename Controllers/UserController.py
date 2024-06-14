from aifc import Error
from Models.Users import Users
from Utils.db import Database
class UserController:
    
    """
    Classe responsável pelo controle de operações relacionadas aos usuários.

    Métodos:
        - register(nome, password, cargo): Registra um novo usuário no sistema.
        - login(nome, password): Realiza o login de um usuário.
    """

    @staticmethod
    def register(nome, password, cargo):
        """
        Registra um novo usuário no sistema.

        Parâmetros:
        nome (str): O nome do usuário.
        password (str): A senha do usuário.
        cargo (str): O cargo do usuário (utilizador ou tecnico).

        """
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
        db = Database() # Conecta ao banco de dados
        connection = db.connect()
        if connection: # Abre um cursor para executar comandos SQL
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Users WHERE nome = %s AND pass = %s", (nome, password))
            user = cursor.fetchone()
            cursor.close()
            connection.close()
            if user:
                return Users(*user)
        return None