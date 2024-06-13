from datetime import datetime, timedelta
from Models.Ticket import Ticket
from Utils.db import Database

class StatsController:

    def percent_tickets_atendidos_intervalo_datas(self, start_date, end_date):
        db = Database()
        connection = db.connect()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT COUNT(*) FROM Ticket WHERE estado_ticket = 'atendido' AND data_hora BETWEEN %s AND %s"
                cursor.execute(query, (start_date, end_date))
                total_tickets = cursor.fetchone()[0]

                query = "SELECT COUNT(*) FROM Ticket WHERE data_hora BETWEEN %s AND %s"
                cursor.execute(query, (start_date, end_date))
                total_tickets_periodo = cursor.fetchone()[0]

                if total_tickets_periodo == 0:
                    percent_atendidos = 0.0
                else:
                    percent_atendidos = (total_tickets / total_tickets_periodo) * 100

                return percent_atendidos

            except Exception as e:
                print(f"Erro ao calcular percentual de tickets atendidos: {e}")
            finally:
                cursor.close()
                connection.close()
        else:
            print("Erro na conexão com o banco de dados.")

    
    def percent_tickets_resolvidos_nao_resolvidos(self):
        db = Database()
        connection = db.connect()
        if connection:
            cursor = connection.cursor()
            query = """
                SELECT 
                    SUM(CASE WHEN estado_ticket = 'atendido' THEN 1 ELSE 0 END) AS resolved,
                    SUM(CASE WHEN estado_ticket = 'porAtender' THEN 1 ELSE 0 END) AS not_resolved,
                    COUNT(*) AS total
                FROM Ticket
            """
            cursor.execute(query)
            result = cursor.fetchone()
            cursor.close()

            if result and result[2] > 0:
                resolved_percent = (result[0] / result[2]) * 100
                not_resolved_percent = (result[1] / result[2]) * 100
                return resolved_percent, not_resolved_percent
            else:
                return 0, 0
        else:
            print("Conexão com o MySQL não está disponível.")
            return 0, 0
    

    def media_tempo_atendimento_por_tipo(self):
        db = Database()
        connection = db.connect()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("""
                    SELECT tipo_ticket, AVG(TIMESTAMPDIFF(MINUTE, Ticket.data_hora, COALESCE(hardwareticket.data_hora_atendimento, softwareticket.data_hora_atendimento))) AS media_tempo
                    FROM Ticket
                    LEFT JOIN HardwareTicket ON Ticket.id = HardwareTicket.id AND tipo_ticket = 'hardware'
                    LEFT JOIN SoftwareTicket ON Ticket.id = SoftwareTicket.id AND tipo_ticket = 'software'
                    GROUP BY tipo_ticket;
                """)
                
                media_tempo_atendimento = {}
                for row in cursor.fetchall():
                    tipo_ticket = row[0]
                    media_tempo = row[1]
                    media_tempo_atendimento[tipo_ticket] = media_tempo or 0.0  # Handle None values
                return media_tempo_atendimento
                   
            except Exception as e:
                print(f"Erro ao calcular média de tempo de atendimento: {e}")
                return {}
            finally:
                cursor.close()
                connection.close()
    