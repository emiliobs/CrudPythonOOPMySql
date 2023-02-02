import mysql.connector
from mysql.connector import Error


def myConexion():
      conexion = mysql.connector.connect(
       host="localhost",
       user="root",
       password="root",
       database="universidad")
      myCursor =  conexion.cursor()
      myCursor.execute("SELECT * FROM curso ORDER BY nombre ASC")
      resultados = myCursor.fetchall()
      return resultados


def listarCursos(cursos):
	print("Cursos:  ")
	contador = 1
	for curso in cursos:
		print(f"{contador}.  Código: {curso[0]} | Nombre: {curso[1]} ({curso[2]} Créditos)")
		contador += 1
print(" ")