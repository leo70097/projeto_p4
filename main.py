from Views.UserView import UserView
from Views.TicketView import TicketView
from Utils import Constants
from Controllers.TicketController import TicketController


def main_menu():
    user_view = UserView()
    return user_view.user_menu()


def ticket_menu():
    ticket_view = TicketView()
    return ticket_view.ticket_menu()

def main():
    ticket_controller = TicketController() #Inicializa o TicketController
    while True:
        user = main_menu()
        if user:
            # Aqui você pode adicionar a lógica para redirecionar para as funcionalidades do sistema de acordo com o tipo de usuário
            if user.role == Constants.ROLE_USER :
                print("Bem-vindo, utilizador!")
                ticket_menu()
                # Adicione lógica para funcionalidades de utilizador aqui
            elif user.role == Constants.ROLE_TECHNICIAN :
                print("Bem-vindo, técnico!")
                # Adicione lógica para funcionalidades de técnico aqui
            break

if __name__ == "__main__": 
    main()