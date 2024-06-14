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
        tipo_ticket = input("Tipo de Ticket (1 para hardware, 2 para software): ")
        if tipo_ticket == '1':
            equipment = input("Equipamento: ")
            avaria = input("Avaria: ")
            self.ticket_controller.create_ticket(self.user.id, 'hardware', equipment=equipment, avaria=avaria)
        elif tipo_ticket == '2':
            software = input("Software: ")
            descricao_necessidade = input("Descrição da necessidade: ")
            self.ticket_controller.create_ticket(self.user.id, 'software', software=software, descricao_necessidade=descricao_necessidade)
        else:
            print("Tipo de ticket inválido!")
            
    def view_tickets(self, colaborador_id):
        tickets = self.ticket_controller.get_tickets_by_user_id(colaborador_id)
        if tickets:
            print("\nMeus Tickets:")
            for ticket in tickets:
                if ticket.tipo_ticket == TICKET_HARDWARE:
                    hardware_tickets = self.ticket_controller.get_hardware_ticket(ticket.id)
                    if hardware_tickets:
                        hardware_ticket = hardware_tickets[0]  # Assume que só há um ticket de hardware por ID
                        print(f"ID: {ticket.id}, Tipo: {ticket.tipo_ticket}, Equipamento: {hardware_ticket.equipment}, Avaria: {hardware_ticket.avaria}, Estado: {ticket.estado_ticket}, Data/Hora: {ticket.data_hora}")
                    else:
                        print(f"ID: {ticket.id}, Tipo: {ticket.tipo_ticket} não encontrado")
                
                elif ticket.tipo_ticket == TICKET_SOFTWARE:
                    software_tickets = self.ticket_controller.get_software_ticket(ticket.id)
                    if software_tickets:
                        software_ticket = software_tickets[0]  # Assume que só há um ticket de software por ID
                        print(f"ID: {ticket.id}, Tipo: {ticket.tipo_ticket}, Software: {software_ticket.software}, Descrição da necessidade: {software_ticket.descricao_necessidade}, Estado: {ticket.estado_ticket}, Data/Hora: {ticket.data_hora}")
                    else:
                        print(f"ID: {ticket.id}, Tipo: {ticket.tipo_ticket} não encontrado")
                
                else:
                    print(f"ID: {ticket.id}, Tipo de ticket inválido: {ticket.tipo_ticket}")
        
        else:
            print("Não há tickets disponíveis para este usuário.")