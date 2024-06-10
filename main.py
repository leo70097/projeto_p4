from Views.UserView import UserView
from Utils import Constants


def main_menu():
    user_view = UserView()
    return user_view.user_menu()


def main():
    while True:
        user = main_menu()
        if user:
            # Aqui você pode adicionar a lógica para redirecionar para as funcionalidades do sistema de acordo com o tipo de usuário
            if user.role == Constants.ROLE_USER :
                print("Bem-vindo, utilizador!")
                # Adicione lógica para funcionalidades de utilizador aqui
            elif user.role == Constants.ROLE_TECHNICIAN :
                print("Bem-vindo, técnico!")
                # Adicione lógica para funcionalidades de técnico aqui

if __name__ == "__main__": 
    main()