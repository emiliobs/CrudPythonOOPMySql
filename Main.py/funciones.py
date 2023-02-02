import mysql.connector
from mysql.connector import Error

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="universidad")
# myCursor =  conexion.cursor()
# myCursor.execute("SELECT * FROM curso ORDER BY nombre ASC")
# resultados = myCursor.fetchall()
# return resultados


def listarCursos():
	print("\nCursos: \n ")
	contador = 1
	myCursor = conexion.cursor()
	myCursor.execute("SELECT * FROM curso ORDER BY nombre ASC")
	cursos = myCursor.fetchall()
	for curso in cursos:
		print(f"{contador}.  Código: {curso[0]} | Nombre: {curso[1]} ({curso[2]} Créditos)")
		contador += 1


print(" ")


def registrarCurso(curso):
	try:
			myCurso = conexion.cursor()
			sql = "INSERT INTO curso (codigo, nombre, creditos) VALUES ('{0}', '{1}', {2})"
			myCurso.execute(sql.format(curso[0], curso[1], curso[2]))
			conexion.commit()
			print("Curso Registrado!\n")
	except Error as ex:
				  print(f"Eror al intentar la Conexión: {ex}")

def pedirDatosRegistro():
	codigo  = input("Ingrese Código: ")
	nombre = input("Ingrese Nombre: ")
	creditos = int(input("Ingrese Créditos: "))

	curso = (codigo, nombre, creditos)
	return curso
