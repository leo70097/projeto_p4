from Controllers.TicketController import TicketController

class TecnicoView:
    
    @staticmethod
    def tecnico_menu():
        
        while True:
            print("\n=== Menu Técnico ===")
            print("1. Ver Tickets") #(Só os tickets "por Atender")
            print("2. Ver Mapas")
            print("0. Sair")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                TecnicoView.view_tickets()
            elif choice == '2':
                TecnicoView.view_maps()
            elif choice == '0':
                break
            else:
                print("Opção inválida!")
            


    @staticmethod
    def view_tickets():
        tickets = TicketController.get_tickets()
        if tickets: 
            print("\n=== Tickets por Atender ===")
            for ticket in tickets:
                print (ticket)
            else:
                print("Nao há Tickets por atender")


    @staticmethod
    def view_maps():
        """
        Visualiza os mapas estatísticos.
        """
        print("\n=== Mapas Estatísticos ===")
        # Lógica para gerar e exibir os mapas
        