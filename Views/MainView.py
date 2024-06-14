
class MainView:
    
    def __init__(self, controller):
        """
        Inicializador da classe MainView.

        Args:
            controller: Objeto controlador que gerencia as operações do sistema.
        """
        self.controller = controller

    def main_menu(self):
        """
        Exibe o menu principal e permite ao usuário escolher entre registrar, fazer login ou sair do sistema.
        """
        while True:
            print("\nBem-vindo ao Ticket2Help")
            print("1. Registrar")
            print("2. Login")
            print("3. Sair")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.register()
            elif choice == '2':
                return self.login()  # Retorna o usuário após o login
            elif choice == '3':
                break
            else:
                print("Opção inválida, tente novamente.")

    def register(self):
        """
        Método para registrar um novo usuário no sistema.
        Solicita nome, senha e tipo de usuário (utilizador ou técnico) e chama o método de registro do controlador.
        """
        nome = input("Nome: ")
        password = input("Senha: ")
        while True:
            escolha = input("Escolha uma opção (1 para usuário, 2 para técnico): ")
            cargo = 'utilizador' if escolha == '1' else ('tecnico' if escolha == '2' else None)
            
            if cargo:
                break
            else:
                print("Opção inválida. Escolha apenas 1 ou 2.")
        print(f"Cargo selecionado: {cargo}")
        self.controller.register(nome, password, cargo)
        print("Usuário registrado com sucesso!")

    def login(self):
        """
        Método para realizar login de um usuário no sistema.
        Solicita nome e senha, chama o método de login do controlador e retorna o usuário autenticado.
        """
        nome = input("Nome: ")
        password = input("Senha: ")
        user = self.controller.login(nome, password)
        if user:
            print(f"Bem-vindo, {user.nome}!")
            return user  # Retorna o usuário após o login
        else:
            print("Nome ou senha incorretos, tente novamente.")