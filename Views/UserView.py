from Utils.Constants import *

class UserView:
    
    def __init__(self, ticket_controller, user):
        self.ticket_controller = ticket_controller
        self.user = user

    def user_menu(self):
        while True:
            print("\nMenu de User")
            print("1. Criar Ticket")
            print("2. Ver os seus Tickets")
            print("3. Sair")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.create_ticket()
            elif choice == '2':
                self.view_tickets(self.user.id)
            elif choice == '3':
                break
            else:
                print("Opção inválida, tente novamente.")

    def create_ticket(self):
        tipo_ticket = 'hardware' if input("Tipo de Ticket (1 para hardware, 2 para software): ") == '1' else 'software'
        if tipo_ticket == 'hardware':
            equipment = input("Equipamento: ")
            avaria = input("Avaria: ")
            self.ticket_controller.create_ticket(self.user.id, tipo_ticket, equipment=equipment, avaria=avaria)
        elif tipo_ticket == 'software':
            software = input("Software: ")
            descricao_necessidade = input("Descrição da necessidade: ")
            self.ticket_controller.create_ticket(self.user.id, tipo_ticket, software=software, descricao_necessidade=descricao_necessidade)
        else:
            print("Tipo de ticket inválido!")
            
    def view_tickets(self, colaborador_id):
        tickets = self.ticket_controller.get_tickets_by_user_id(colaborador_id)
        if tickets:
            print("\nMeus Tickets:")
            for ticket in tickets:
                if ticket.tipo_ticket == TICKET_HARDWARE :
                    hardwareTicket =  self.ticket_controller.get_hardware_ticket(ticket.id)
                    print(f"ID: {ticket.id}, Tipo: {ticket.tipo_ticket}, Equipamento: {hardwareTicket[0].equipment}, Avaria: {hardwareTicket[0].avaria}, Estado: {ticket.estado_ticket}, Data/Hora: {ticket.data_hora}")
                elif ticket.tipo_ticket == TICKET_SOFTWARE:
                    softwareTicket =  self.ticket_controller.get_software_ticket(ticket.id)
                    print(f"ID: {ticket.id}, Tipo: {ticket.tipo_ticket}, Software: {softwareTicket[0].software}, Descrição da necessidade: {softwareTicket[0].descricao_necessidade}, Estado: {ticket.estado_ticket}, Data/Hora: {ticket.data_hora}")