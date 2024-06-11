from datetime import datetime
from Models.Ticket import Ticket
from Utils.Constants import *
from Utils.db import Database


class TicketController:
    
    @staticmethod
    def create_ticket(tipo_ticket):
        ticket = Ticket(tipo_ticket)
        ticket.save()
        print("Ticket criado com sucesso!")

    
    @staticmethod
    def get_tickets():
        try: 
            db = Database()
            connection = db.connect()
            if connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM ticket WHERE estadoTicket = 'porAtender'")
                tickets = []
                for data_hora, codigo_colaborador, estado_ticket, tipo_ticket in cursor.fetchall():
                    ticket = Ticket(tipo_ticket)
                    ticket.data_hora = data_hora
                    ticket.codigo_colaborador = codigo_colaborador
                    ticket.estado_ticket = estado_ticket
                    ticket.tipo_ticket = tipo_ticket
                    tickets.append(ticket)
                return tickets
        except Exception as e:
            print("Erro ao obter Tickets")
        finally:
            connection.close()
