import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable
	# x = PrettyTable()

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
			print(
					f"{contador}.- Código: {curso[1]} | Nombre: {curso[2]} => ({curso[3]} Créditos)")
			contador += 1

		print(" ")
		# x.field_names =['Código', 'Nombre','Créditos']
	#   for curso in cursos:
	#     x.add_row([curso[1], curso[2], curso[3]])
	#   print(x)
	# print()

def registrarCurso(curso):
		try:
				myCurso = conexion.cursor()
				sql = "INSERT INTO curso (codigo, nombre, creditos) VALUES ('{0}', '{1}', '{2}')"
				myCurso.execute(sql.format(curso[0], curso[1], curso[2]))
				conexion.commit()
				print("Curso Registrado!\n")
		except Error as ex:
    			print(f"Eror al intentar la Conexión: {ex}")
       
       
       
def pedirDatosRegistro():
  codigoCorrecto = False
  while (not codigoCorrecto):
    codigo = input("Ingrese Código: ")
    if len(codigo) == 5:
      codigoCorrecto = True
    else:
      print("Código incorrecto: Debe tener 5 dígitios.")
  nombre = input("Ingrese Nombre: ")
  creditoCorrecto = False
  while(not creditoCorrecto):
    creditos = input("Ingrese Créditos: ")
    if creditos.isnumeric():
      if  (int(creditos) > 0):
        creditoCorrecto = True
        creditos = int(creditos)
      else:
        print("Los créditos deben ser mayor a 0.") 
    else:
      print("Créditos incorrectos: Debe ser un número únicamente y Mayor a 0.")
  curso = (codigo, nombre, creditos)
  return curso 
