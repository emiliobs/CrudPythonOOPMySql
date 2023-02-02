import mysql.connector
from mysql.connector import Error

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
                print(f"Error al intentar la conexion: {ex}")

    
    def listarCursos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("Select * From curso Order By Nombre ASC")
                resultado = cursor.fetchall()
                
                return resultado

            except Error as ex:
                print(f"Eror al intentar la conexion: {ex}")
        
            

