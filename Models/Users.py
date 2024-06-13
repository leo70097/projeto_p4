from aifc import Error
from Utils.db import Database

class Users:
    
    def __init__(self, id, nome, password, cargo):
        self.id = id
        self.nome = nome
        self.password = password
        self.cargo = cargo