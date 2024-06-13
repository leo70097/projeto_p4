from Views.MainView import MainView
from Controllers.UserController import UserController
from Controllers.TechnicianController import TechnicianController
from Controllers.TicketController import TicketController

class MainController:
    
    def __init__(self):
        self.main_view = MainView(self)
        self.user_controller = UserController()
        self.technician_controller = TechnicianController()
        self.ticket_controller = TicketController()

    def run(self):
        user = self.main_view.main_menu()
        return user

    def register(self, nome, password, cargo):
        if cargo == 'utilizador':
            self.user_controller.register(nome, password, cargo)
        elif cargo == 'tecnico':
            self.user_controller.register(nome, password, cargo)
        else:
            print("Cargo inválido.")

    def login(self, nome, password):
        user = self.user_controller.login(nome, password)
        if user:
            return user
        else:
            user = self.user_controller.login(nome, password)
            if user:
                return user
            else:
                print("Nome ou senha incorretos.")
                return None
