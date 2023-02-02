import mysql.connector

 # DAO = Data Access Object:
class DAO(): 
    
    def _ini_(self):
        try:
            self.conexion = mysql.connector.connect(
                  host = 'localhost',
                  port = '3306',
                  user = 'root',
                  password = 'root',
                  db = 'universidad'
                )
        except Error as ex:
                print(f"Eror al intentar la conexión: {ex}")
            

