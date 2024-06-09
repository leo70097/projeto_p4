from Utils.db import Database
from Models.Ticket import Ticket

class HardwareTicket(Ticket):
    
    def __init__ (self,id,equipamento,avaria,dataAtendimento,descricaoReparacao,pecas,estado):
        super.__init__(id,'porAtender','hardware')
        self.equipamento = equipamento
        self.avaria = avaria
        self.dataAtendimento = dataAtendimento
        self.descricaoReparacao = descricaoReparacao
        self.pecas = pecas
        self.estado = estado
        
        def save(self):
            db = Database()
            connection = db.connect()
            if connection:
                #Save the main ticket
                super().save()
                #Get the last inserted id
                cursor = connection.cursor()
                ticket_id = cursor.lastrowid
                #Save the hardware ticket details
                sql = "INSERT INTO hardware_tickets(id,equipamento,avaria,dataAtendimento,descricaoReparacao,pecas,estado) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql,(ticket_id,self.equipamento,self.avaria,self.dataAtendimento,self.descricaoReparacao,self.pecas,self.estado))
                connection.commit()
                db.close(connection)