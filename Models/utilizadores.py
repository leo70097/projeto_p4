from Utils.db import Database

class Utilizadores:
    
    def __init__(self,username,password,role):
        self.username = username
        self.password = password
        self.role = role
        
        
        def save(self):
            db = Database()
            connection = db.connect()
            if connection :
                cursor = connection.cursor()
                sql = "INSERT INTO utulizadores (username,password,roles) VALUES (%s,%s,%s)"
                cursor.execute(sql,(self.username,self.password,self.role))
                connection.commit()
                db.close(connection)            