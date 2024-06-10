from Utils.Constants import *
from Controllers.UserController import UserController

class UserView:
    
    @staticmethod
    def user_menu():
        controller = UserController()
        while True:
            print("\n=== Gerenciamento de Utilizadores ===")
            print("1. Criar Utilizador")
            print("2. Login")
            print("0. Voltar")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                username = input("Username: ")
                password = input("Password: ")
                role = ''
                while role not in ['utilizador', 'tecnico']:
                    role = input("Função (utilizador/tecnico): ").lower()
                    if role not in ['utilizador', 'tecnico']:
                        print("Função inválida! Escolha 'utilizador' ou 'tecnico'.")
                
                if role == ROLE_TECHNICIAN:
                    codigo = input("Insira o código de técnico: ")
                    if codigo != TECHNICIAN_CODE :
                        print("Código inválido! Registado como 'utilizador'.")
                        role = ROLE_USER
                
                controller.create_user(username, password, role)
                print(SUCCESS_USER_CREATED.format(role))
            
            elif choice == '2':
                username = input("Username: ")
                password = input("Password: ")
                user = controller.login(username, password)
                if user:
                    print(SUCCESS_LOGIN)
                    return user
                else:
                    print(ERROR_INVALID_CREDENTIALS)
            elif choice == '0':
                break
            else:
                print(INVALID_OPTION)