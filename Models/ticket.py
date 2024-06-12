from aifc import Error
from Utils.db import Database
from datetime import datetime
from Utils.Constants import *


class Ticket:
    def __init__(self, id, colaborador_id, estado_ticket, data_hora, tipo_ticket):
        self.id = id
        self.colaborador_id = colaborador_id
        self.estado_ticket = estado_ticket
        self.data_hora = data_hora
        self.tipo_ticket = tipo_ticket