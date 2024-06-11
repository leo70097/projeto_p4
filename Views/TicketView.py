from Controllers.TicketController import TicketController

class TicketView:
    
    @staticmethod
    def ticket_menu():
        while True:
            print("\n=== Gestão de Tickets ===")
            print("1. Criar Ticket")
            print("2. Listar Tickets")
            print("0. Voltar")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                #tipo_ticket = input("Tipo de Ticket: ")
                #TicketController.create_ticket(tipo_ticket)
                TicketView.criar_ticket()
            elif choice == '2':
                break
            elif choice == '0':
                break
            else:
                print("Opção inválida!")


    @staticmethod
    def criar_ticket():
        while True:
            print("\n=== Criar Ticket ===")
            print("1. Hardware")
            print("2. Software")
            print("0. Voltar")
            choice = input("Escolha o tipo de ticket: ")

            if choice == '1':
                tipo_ticket = 'Hardware'
                TicketController.create_ticket(tipo_ticket)
                break
            elif choice == '2':
                tipo_ticket = 'Software'
                TicketController.create_ticket(tipo_ticket)
                break
            elif choice == '0':
                break
            else:
                print('Opção invalida!')