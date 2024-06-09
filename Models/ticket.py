from Utils.db import Database

class Ticket:
    
    def __init__(self, data_hora, codigo_colaborador, estado_ticket,tipo_ticket):
        self.data_hora = data_hora
        self.codigo_colaborador = codigo_colaborador
        self.estado_ticket = estado_ticket
        self.tipo_ticket = tipo_ticket

    def save(self):
        db = Database()
        connection = db.connect()
        if connection:
            cursor = connection.cursor()
            sql = "INSERT INTO ticket (data_hora,codigo_colaborador, estado_ticket, tipo_ticket) VALUES (%s, %s,%s,%s)"
            cursor.execute(sql, (self.id,self.data_hora, self.codigo_colaborador, self.estado_ticket, self.tipo_ticket))
            connection.commit()
            db.close(connection)