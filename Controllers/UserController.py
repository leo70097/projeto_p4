from Models.Users import Users
from Utils.db import Database

class UserController :
    
    def create_user (self,username,password,role):
        user = Users(username,password,role)
        user.save()
        
        
    def login(self, username, password):
        db = Database()
        connection = db.connect()
        if connection:
            cursor = connection.cursor(dictionary= True)
            sql = "SELECT * FROM utilizadores WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, password))
            user_data = cursor.fetchone()
            connection.close()
            if user_data:
                return Users(user_data['username'], user_data['password'], user_data['role'])
        else:
            return None
            
        