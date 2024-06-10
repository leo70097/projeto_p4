from Controllers.TicketController import TicketController

class TicketView:
    
    @staticmethod
    def ticket_menu():
        while True:
            print("\n=== Gestão de Tickets ===")
            print("1. Criar Ticket")
            print("0. Voltar")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                tipo_ticket = input("Tipo de Ticket: ")
                TicketController.create_ticket(tipo_ticket)
            elif choice == '0':
                break
            else:
                print("Opção inválida!")