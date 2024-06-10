from datetime import datetime
from Models.Ticket import Ticket
from Utils.Constants import *

class TicketController:
    
    @staticmethod
    def create_ticket(tipo_ticket):
        ticket = Ticket(tipo_ticket)
        ticket.save()
        print("Ticket criado com sucesso!")