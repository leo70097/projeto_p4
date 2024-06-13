from Utils.Constants import *
from Utils.db import Database
from Models.Ticket import Ticket
from datetime import datetime

class HardwareTicket(Ticket):
                
    def __init__(self, id, colaborador_id, equipment, avaria, descricao_reparacao=None, data_hora_atendimento=None, pecas=None):
        super().__init__(id, colaborador_id, TICKET_PENDING, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), TICKET_HARDWARE)
        self.equipment = equipment
        self.avaria = avaria
        self.descricao_reparacao = descricao_reparacao
        self.pecas = pecas
        self.data_hora_atendimento = data_hora_atendimento