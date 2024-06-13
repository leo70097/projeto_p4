from Utils.Constants import *

class UserView:
    
    def __init__(self, ticket_controller, user):
        self.ticket_controller = ticket_controller
        self.user = user

    def user_menu(self):
        while True:
            print("\nMenu do Usuário")
            print("1. Criar Ticket")
            print("2. Ver Tickets")
            print("3. Sair")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.create_ticket()
            elif choice == '2':
                self.view_tickets()
            elif choice == '3':
                break
            else:
                print("Opção inválida, tente novamente.")

    def create_ticket(self):
        tipo_ticket = input("Tipo de Ticket (hardware/software): ")
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

    def view_tickets(self):
        tickets = self.ticket_controller.get_tickets_by_state('porAtender')
        if tickets:
            for ticket in tickets:
                print(f"Ticket ID: {ticket.id}, Tipo: {ticket.tipo_ticket}, Estado: {ticket.estado_ticket}, Data/Hora: {ticket.data_hora}, ")
        else:
            print("Não há tickets por atender.")