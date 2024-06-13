from datetime import datetime
from Utils.Constants import *
from Models.Ticket import Ticket
from Utils.db import Database   

class SoftwareTicket(Ticket):
    
    def __init__(self, id, colaborador_id, software, descricao_necessidade, descricao_intervencao=None):
        super().__init__(id, colaborador_id, TICKET_PENDING, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), TICKET_SOFTWARE)
        self.software = software
        self.descricao_necessidade = descricao_necessidade
        self.descricao_intervencao = descricao_intervencao