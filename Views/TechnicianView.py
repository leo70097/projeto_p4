from Controllers.TicketController import TicketController

class TechnicianView:
    def __init__(self, controller, user):
        self.controller = controller
        self.user = user

    def technician_menu(self):
        while True:
            print("\nMenu do Técnico")
            print("1. Atender Ticket")
            print("2. Ver Tickets por Atender")
            print("3. Sair")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.attend_ticket()
            elif choice == '2':
                self.view_tickets()
            elif choice == '3':
                break
            else:
                print("Opção inválida, tente novamente.")

    def attend_ticket(self):
        ticket_id = int(input("ID do Ticket: "))
        tipo_ticket = input("Tipo de Ticket (hardware/software): ")
        if tipo_ticket == 'hardware':
            descricao_reparacao = input("Descrição da Reparação: ")
            pecas = input("Peças: ")
            self.controller.update_ticket(ticket_id, tipo_ticket=tipo_ticket, descricao_reparacao=descricao_reparacao, pecas=pecas)
        elif tipo_ticket == 'software':
            descricao_intervencao = input("Descrição da Intervenção: ")
            self.controller.update_ticket(ticket_id, tipo_ticket=tipo_ticket, descricao_intervencao=descricao_intervencao)
        else:
            print("Tipo de ticket inválido!")

    def view_tickets(self):
        tickets = self.controller.get_tickets_by_state('porAtender')
        if tickets:
            for ticket in tickets:
                print(f"Ticket ID: {ticket.id}, Tipo: {ticket.tipo_ticket}, Estado: {ticket.estado_ticket}, Data/Hora: {ticket.data_hora}")
        else:
            print("Não há tickets por atender.")
        