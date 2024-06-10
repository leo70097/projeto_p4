from Utils.db import Database
from datetime import datetime


class Ticket:
    
    """
    def __init__(self, data_hora, codigo_colaborador, estado_ticket,tipo_ticket):
        self.data_hora = data_hora
        self.codigo_colaborador = codigo_colaborador
        self.estado_ticket = estado_ticket
        self.tipo_ticket = tipo_ticket
    """

    def __init__(self, *args):
        #(Construtor Cópia)
        if len(args) == 1 and isinstance(args[0], Ticket):
            self.data_hora = args[0].data_hora
            self.codigo_colaborador = args[0].codigo_colaborador
            self.estado_ticket = args[0].estado_ticket
            self.tipo_ticket = args[0].tipo_ticket
        elif len(args) == 4:
            #Construtor por Parametros
            self.data_hora = args[0]
            self.codigo_colaborador = args[1]
            self.estado_ticket = args[2]
            self.tipo_ticket = args[3]
        else: 
            #(Construtor Default)
            self.data_hora = datetime.now()
            self.codigo_colaborador = 0
            self.estado_ticket = "porAtender"
            self.tipo_ticket = None




    def save(self):
        db = Database()
        connection = db.connect()
        if connection:
            cursor = connection.cursor()
            sql = "INSERT INTO ticket (data_hora,codigo_colaborador, estado_ticket, tipo_ticket) VALUES (%s, %s,%s,%s)"
            cursor.execute(sql, (self.id,self.data_hora, self.codigo_colaborador, self.estado_ticket, self.tipo_ticket))
            connection.commit()
            db.close(connection)