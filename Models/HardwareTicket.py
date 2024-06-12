from Utils.Constants import *
from Utils.db import Database
from Models.Ticket import Ticket
from datetime import datetime

class HardwareTicket(Ticket):
                
    def __init__(self, id, colaborador_id, equipment, avaria, descricao_reparacao=None, pecas=None, estado_atendimento='porAtender'):
        super().__init__(id, colaborador_id, 'porAtender', datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'hardware')
        self.equipment = equipment
        self.avaria = avaria
        self.descricao_reparacao = descricao_reparacao
        self.pecas = pecas
        self.estado_atendimento = estado_atendimento