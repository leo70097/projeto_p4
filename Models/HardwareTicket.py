from Utils.db import Database
from Models.ticket import Ticket
from datetime import datetime

class HardwareTicket(Ticket):
    
    '''
    def __init__ (self,equipamento,avaria,dataAtendimento,descricaoReparacao,pecas,estado):
        super.__init__(id,'porAtender','hardware')
        self.equipamento = equipamento
        self.avaria = avaria
        self.dataAtendimento = dataAtendimento
        self.descricaoReparacao = descricaoReparacao
        self.pecas = pecas
        self.estado = estado
    ''' 

    def __init__ (self, *args):
        if len(args) == 1 and isinstance(args[0], HardwareTicket):
            super().__init__(args[0])           
            self.equipamento = args[0].equipamento
            self.avaria = args[0].avaria
            self.dataAtendimento = args[0].dataAtendimento
            self.descricaoReparacao = args[0].descricaoReparacao
            self.pecas = args[0].pecas
            self.estado = args[0].estado
        elif len(args) == 10:
            super().__init__(args[0], args[1], args[2], args[3])
            self.equipamento = args[4]
            self.avaria = args[5]
            self.dataAtendimento = args[6]
            self.descricaoReparacao = args[7]
            self.pecas = args[8]
            self.estado = args[9]
        else:
            super().__init__(args[0], args[1], args[2], args[3])
            self.equipamento = None
            self.dataAtendimento = datetime.now()
            self.descricaoReparacao = None
            self.pecas = None
            self.estado = 'Aberto'

        
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
                sql = "INSERT INTO hardware_tickets(equipamento,avaria,dataAtendimento,descricaoReparacao,pecas,estado) VALUES (%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql,(ticket_id,self.equipamento,self.avaria,self.dataAtendimento,self.descricaoReparacao,self.pecas,self.estado))
                connection.commit()
                db.close(connection)