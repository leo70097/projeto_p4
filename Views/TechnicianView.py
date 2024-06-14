from Controllers.TicketController import TicketController
from Controllers.StatsController import StatsController
from Utils.Constants import *

class TechnicianView:
    def __init__(self, controller, user):
        self.controller = controller
        self.ticket_controller = TicketController()
        self.user = user
        self.stats_controller = StatsController()

    def technician_menu(self):
        while True:
            print("\nMenu do Técnico")
            print("1. Atender Ticket")
            print("2. Ver Tickets por Atender")
            print("3. Ver Estatísticas")
            print("0. Sair")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.attend_ticket()
            elif choice == '2':
                self.view_tickets()
            elif choice == '3':
                self.show_statistics_menu()
            elif choice == '0':
                break
            else:
                print("Opção inválida, tente novamente.")

    def attend_ticket(self):
        self.view_tickets()
        ticket_id = int(input("ID do Ticket: "))
        tipo_ticket = input("Tipo de Ticket (hardware/software): ")
        
        if tipo_ticket == TICKET_HARDWARE:
            descricao_reparacao = input("Descrição da Reparação: ")
            pecas = input("Peças: ")
            self.controller.update_ticket(ticket_id, tipo_ticket=tipo_ticket, descricao_reparacao=descricao_reparacao, pecas=pecas)
        elif tipo_ticket == TICKET_SOFTWARE:
            descricao_intervencao = input("Descrição da Intervenção: ")
            self.controller.update_ticket(ticket_id, tipo_ticket=tipo_ticket, descricao_intervencao=descricao_intervencao)
        else:
            print("Tipo de ticket inválido!")

    def view_tickets(self):
        tickets = self.controller.get_tickets_by_state('porAtender')
        if tickets:
            print("\n Tickets por Atender:")
            for ticket in tickets:
                if ticket.tipo_ticket == TICKET_HARDWARE:
                    hardwareTicket = self.ticket_controller.get_hardware_ticket(ticket.id)
                    if hardwareTicket:
                        print(f"ID: {ticket.id}, Tipo: {ticket.tipo_ticket}, Equipamento: {hardwareTicket[0].equipment}, Avaria: {hardwareTicket[0].avaria}, Estado: {ticket.estado_ticket}, Data/Hora: {ticket.data_hora}")
                    else:
                        print(f"ID: {ticket.id}, Tipo: {ticket.tipo_ticket}, Equipamento: Não encontrado, Avaria: Não encontrada, Estado: {ticket.estado_ticket}, Data/Hora: {ticket.data_hora}")
                elif ticket.tipo_ticket == TICKET_SOFTWARE:
                    softwareTicket = self.ticket_controller.get_software_ticket(ticket.id)
                    if softwareTicket:
                        print(f"ID: {ticket.id}, Tipo: {ticket.tipo_ticket}, Software: {softwareTicket[0].software}, Descrição da necessidade: {softwareTicket[0].descricao_necessidade}, Estado: {ticket.estado_ticket}, Data/Hora: {ticket.data_hora}")
                    else:
                        print(f"ID: {ticket.id}, Tipo: {ticket.tipo_ticket}, Software: Não encontrado, Descrição da necessidade: Não encontrada, Estado: {ticket.estado_ticket}, Data/Hora: {ticket.data_hora}")



    def show_statistics_menu(self):
        while True:
            print("\nMenu de Estatísticas")
            print("1. Percentual de Tickets Atendidos num Intervalo de Datas")
            print("2. Percentual de Tickets Resolvidos e Não Resolvidos")
            print("3. Média de Tempo de Atendimento por Tipo de Ticket")
            print("4. Voltar")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.show_percent_tickets_atendidos()
            elif choice == '2':
                self.show_percent_tickets_resolvidos_nao_resolvidos()
            elif choice == '3':
                self.show_media_tempo_atendimento()
            elif choice == '4':
                break
            else:
                print("Opção inválida, tente novamente.")


    def show_percent_tickets_atendidos(self):
        start_date = input("Data de início (YYYY-MM-DD): ")
        end_date = input("Data de fim (YYYY-MM-DD): ")
        percent_atendidos = self.stats_controller.percent_tickets_atendidos_intervalo_datas(start_date, end_date)
        print(f"Percentual de Tickets Atendidos: {percent_atendidos:.2f}%")
       
        
    def show_percent_tickets_resolvidos_nao_resolvidos(self):
        resolved_percent, not_resolved_percent = self.stats_controller.percent_tickets_resolvidos_nao_resolvidos()
        print(f"Percentual de Tickets Resolvidos: {resolved_percent:.2f}%")
        print(f"Percentual de Tickets Não Resolvidos: {not_resolved_percent:.2f}%")


    def show_media_tempo_atendimento(self):
        media_tempo_atendimento = self.stats_controller.media_tempo_atendimento_por_tipo()
        for tipo, media in media_tempo_atendimento.items():
            print(f"Média de Tempo de Atendimento para {tipo}: {media:.2f} minutos")
        if not media_tempo_atendimento:
            print("Não há dados disponíveis para calcular a média de tempo de atendimento por tipo de ticket.")
            return