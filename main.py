from Views.UserView import UserView
from Views.TechnicianView import TechnicianView
from Utils.Constants import *
from Controllers.MainController import MainController


if __name__ == "__main__":
    main_controller = MainController()
    user = main_controller.run()
    

    if user is not None:  # Verificar se o usuário não é None antes de acessar o atributo cargo
        if user.cargo == ROLE_USER:
            user_view = UserView(main_controller.ticket_controller, user)
            user_view.user_menu()
        elif user.cargo == ROLE_TECHNICIAN:
            technician_view = TechnicianView(main_controller.ticket_controller, user)
            technician_view.technician_menu()