from Models import Ticket
from Utils.db import Database

class SoftwareTicket(Ticket):
    
    def __init__ (self,id,software,avaria,dataAtendimento,descricaoIntervencao,estado):
        super.__init__(id,'porAtender','software')
        self.software = software
        self.avaria = avaria
        self.dataAtendimento = dataAtendimento
        self.descricaoIntervencao = descricaoIntervencao
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
                #Save the software ticket details
                sql = "INSERT INTO software_tickets (id,software,avaria,dataAtendimento,descricaoIntervencao,estado) VALUES (%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql,(ticket_id,self.software,self.avaria,self.dataAtendimento,self.descricaoIntervencao,self.estado))
                connection.commit()
                db.close(connection)