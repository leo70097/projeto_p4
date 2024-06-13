from aifc import Error
from Models.Ticket import Ticket
from Utils.db import Database

class TechnicianController:
    
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