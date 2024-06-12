from Controllers.TicketController import TicketController
from Utils.Constants import *

class TicketView:
    
    def __init__(self):
        self.ticket_controller = TicketController()

    def ticket_menu(self):
        while True:
            print("\nMenu de Tickets")
            print("1. Criar Ticket")
            print("2. Ver Tickets por Atender")
            print("3. Ver Tickets Resolvidos")
            print("4. Sair")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.create_ticket()
            elif choice == '2':
                self.view_tickets('porAtender')
            elif choice == '3':
                self.view_tickets('resolvido')
            elif choice == '4':
                break
            else:
                print("Opção inválida, tente novamente.")

    def create_ticket(self):
        tipo_ticket = input("Tipo de Ticket (hardware/software): ")
        if tipo_ticket == 'hardware':
            equipment = input("Equipamento: ")
            issue = input("Avaria: ")
            self.ticket_controller.create_ticket(ROLE_USER, tipo_ticket, equipment=equipment, issue=issue)
        elif tipo_ticket == 'software':
            software = input("Software: ")
            description = input("Descrição da necessidade: ")
            self.ticket_controller.create_ticket(ROLE_USER, tipo_ticket, software=software, description=description)
        else:
            print("Tipo de ticket inválido!")

    def view_tickets(self, state):
        tickets = self.ticket_controller.get_tickets_by_state(state)
        if tickets:
            print("\nTickets:")
            for ticket in tickets:
                print(f"ID: {ticket.id}, Tipo: {ticket.tipo_ticket}, Estado: {ticket.estado_ticket}, Data/Hora: {ticket.data_hora}")
        else:
            print("Não há tickets neste estado.")