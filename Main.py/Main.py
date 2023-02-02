from BD.conexion import DAO

def menuPrincipal():
			continuar = True

			while(continuar):

				opcionCorrecta = False

				while(not opcionCorrecta):
					
					print("=======  MENÚ PRINCIPAL  =======")
					print("1.- Listar Cursos.")
					print("2.- Registar Curso.")
					print("3.- Actualizar Curso.")
					print("4.- Eliminar Cursos.")
					print("5.- Salir.")
					print("=====  FIN MENÚ PRINCIPAL  =====")
					print()
					opcion = int(input("Seleccione una opción: "))
					print()

					if opcion < 1 or opcion > 5:

								print("Opción incorrecta, ingrese nuevamente un Opción.....")	   
								print()
				
					elif opcion == 5:

						continuar = False
						print("¡Gracias por usar este Sistema!-:")
						print()

						break

					else:
							opcionCorrecta = True
							ejecutarOpciones(opcion)	


def ejecutarOpciones(opcion):
		
	dao = DAO()
	match opcion:
		case 1:
			print("Listar Cursos!")
		case _:
			print("Sorry, esta opcion no existe!")


menuPrincipal()




