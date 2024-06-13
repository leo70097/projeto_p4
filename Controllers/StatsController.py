from datetime import datetime, timedelta
from Models.Ticket import Ticket
from Utils.db import Database

class StatsController:

    def percent_tickets_atendidos_intervalo_datas(self, start_date, end_date):
        db = Database(self.db_config)
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

    

    