from Utils.db import Database

class Utilizadores:
    
    def __init__(self,id,username,password,role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
        
        
        def save(self):
            db = Database()
            connection = db.connect()
            if connection :
                cursor = connection.cursor()
                sql = "INSERT INTO utulizadores (id,username,password,roles) VALUES (%s, %s,%s)"
                cursor.execute(sql,(self.id,self.username,self.password,self.role))
                connection.commit()
                db.close(connection)
            