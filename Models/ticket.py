from Utils.db import Database
from datetime import datetime
from Utils.Constants import *


class Ticket:
    
    def __init__(self, tipo_ticket):
        self.data_hora = datetime.now()
        self.codigo_colaborador = None  # Inicialmente None, será atribuído ao técnico que pegar no ticket
        self.estado_ticket = TICKET_PENDING
        self.tipo_ticket = tipo_ticket

    def save(self):
        db = Database()
        connection = db.connect()
        if connection:
            cursor = connection.cursor()
            sql = "INSERT INTO ticket (data_hora, codigo_colaborador, estado_ticket, tipo_ticket) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (self.data_hora, self.codigo_colaborador, self.estado_ticket, self.tipo_ticket))
            connection.commit()
            db.close(connection)