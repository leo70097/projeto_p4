from Utils.db import Database

class Users:
    
    def __init__(self,username,password,role):
        self.username = username
        self.password = password
        self.role = role
        
    def save(self):
            db = Database()
            connection = db.connect()
            if connection :
                cursor = connection.cursor()
                sql = "INSERT INTO utilizadores (username,password,role) VALUES (%s,%s,%s)"
                cursor.execute(sql,(self.username,self.password,self.role))
                connection.commit()
                db.close(connection)            