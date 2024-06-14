from aifc import Error
from datetime import datetime
from Models.HardwareTicket import HardwareTicket
from Models.SoftwareTicket import SoftwareTicket
from Models.Ticket import Ticket
from Utils.db import Database

class TicketController:
    
    @staticmethod
    def create_ticket(colaborador_id, tipo_ticket, **kwargs):
        db = Database()
        connection = db.connect()
        if connection:
            cursor = connection.cursor()
            data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            estado_ticket = 'porAtender'
            try:
                cursor.execute("INSERT INTO Ticket (colaborador_id, estado_ticket, data_hora, tipo_ticket) VALUES (%s, %s, %s, %s)",
                               (colaborador_id, estado_ticket, data_hora, tipo_ticket))
                ticket_id = cursor.lastrowid
                if tipo_ticket == 'hardware':
                    cursor.execute("INSERT INTO HardwareTicket (id, colaborador_id, equipment, avaria) VALUES (%s, %s, %s, %s)",
                                   (ticket_id, colaborador_id, kwargs.get('equipment'), kwargs.get('avaria')))
                elif tipo_ticket == 'software':
                    cursor.execute("INSERT INTO SoftwareTicket (id, colaborador_id, software, descricao_necessidade) VALUES (%s, %s, %s, %s)",
                                   (ticket_id, colaborador_id, kwargs.get('software'), kwargs.get('descricao_necessidade')))
                connection.commit()
                print("Ticket criado com sucesso!")
            except Error as e:
                print(f"Erro ao criar ticket: {e}")
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def update_ticket(ticket_id, **kwargs):
        db = Database()
        connection = db.connect()
        if connection:
            cursor = connection.cursor()
            data_hora_atendimento = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            estado_ticket = 'atendido'
            try:
                if kwargs.get('tipo_ticket') == 'hardware':
                    cursor.execute("UPDATE HardwareTicket SET descricao_reparacao = %s, pecas = %s, data_hora_atendimento = %s WHERE id = %s",
                                (kwargs.get('descricao_reparacao'), kwargs.get('pecas'), data_hora_atendimento ,ticket_id))
                elif kwargs.get('tipo_ticket') == 'software':
                    cursor.execute("UPDATE SoftwareTicket SET descricao_intervencao = %s, data_hora_atendimento = %s WHERE id = %s",
                               (kwargs.get('descricao_intervencao'), data_hora_atendimento, ticket_id))
                cursor.execute("UPDATE Ticket SET estado_ticket = %s WHERE id = %s",
                           (estado_ticket, ticket_id))
                connection.commit()
                print("Ticket atualizado com sucesso!")
            except Error as e:
                print(f"Erro ao atualizar ticket: {e}")
            finally:
                cursor.close()
                connection.close()
                
    @staticmethod
    def get_tickets_by_user_id(colaborador_id):
        db = Database()
        connection = db.connect()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("SELECT * FROM Ticket WHERE colaborador_id = %s", (colaborador_id,))
                tickets = []
                for row in cursor.fetchall():
                    ticket = Ticket(*row)
                    tickets.append(ticket)
                return tickets
            except Error as e:
                print(f"Erro ao obter tickets: {e}")
                return []
            finally:
                cursor.close()
                connection.close()
                
    @staticmethod
    def get_tickets_by_state(state):
        db = Database()
        connection = db.connect()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("SELECT * FROM Ticket WHERE estado_ticket = %s", (state,))
                tickets = []
                for row in cursor.fetchall():
                    ticket = Ticket(*row)
                    tickets.append(ticket)
                return tickets
            except Error as e:
                print(f"Erro ao obter tickets: {e}")
                return []
            finally:
                cursor.close()
                connection.close()
                
    @staticmethod
    def get_hardware_ticket(ticketId):
        db = Database()
        connection = db.connect()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("SELECT id, colaborador_id, equipment, avaria, descricao_reparacao, pecas, data_hora_atendimento FROM HardwareTicket WHERE id = %s",(ticketId,))
                hardwares = []
                for row in cursor.fetchall():
                    id, colaborador_id, equipment, avaria, descricao_reparacao, pecas, data_hora_atendimento = row
                    hardware = HardwareTicket(id, colaborador_id, equipment, avaria, descricao_reparacao, data_hora_atendimento, pecas)
                    hardwares.append(hardware)
                return hardwares
            except Error as e:
                print(f"Erro ao obter tickets: {e}")
                return []
            finally:
                cursor.close()
                connection.close()
                
    @staticmethod
    def get_software_ticket(ticket_id):
        db = Database()
        connection = db.connect()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("SELECT id, ticket_id, software, descricao_necessidade, descricao_intervencao, colaborador_id FROM SoftwareTicket WHERE id = %s", (ticket_id,))
                rows = cursor.fetchall()
                software_tickets = []
                for row in rows:
                    id, ticket_id, software, descricao_necessidade, descricao_intervencao, colaborador_id = row
                    ticket = SoftwareTicket(ticket_id, colaborador_id, software, descricao_necessidade, descricao_intervencao)
                    software_tickets.append(ticket)
                return software_tickets
            except Error as e:
                print(f"Erro ao obter tickets de software: {e}")
                return []
            finally:
                cursor.close()
                connection.close()





