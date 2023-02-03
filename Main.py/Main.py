# from BD.conexion import DAO
# import  conexion
from mysql.connector import Error
import funciones


def menuPrincipal():
    continuar = True

    while (continuar):

        opcionCorrecta = False

        while (not opcionCorrecta):

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
    match opcion:
        case 1:
            try:
                cursos = funciones.listarCursoById()

                if (cursos != ""):
                    funciones.listarCursos()
                    print("")
                else:
                    print("No hay Cursos Registrado!")
                    print("")
            except Error as ex:
                print(f"Listar Cursos, Ocurrió un Error: {ex}")
                print(" ")
        case 2:
            curso = funciones.pedirDatosRegistro()
            try:
                funciones.registrarCurso(curso)
                funciones.listarCursos()

            except:
                print("Registrar Curso, Ocurrió un Error!")
                print(" ")
        case 3:
            try:
                cursos = funciones.listarCursoById()
                # print(cursos)
                if (cursos != ""):
                    curso = funciones.pedirDatosActualizar(cursos)

                    if curso:
                        funciones.actualizarCursos(curso)
                        funciones.listarCursos()
                        print()
                    else:
                        print("Código de curso a actualizar no encontrado.....")
                        print()
                else:
                    print("No se econtro el curso!")
                    print()
            except Error as ex:
                print(f"Actualizar. Ocurrió un Error: {ex}")
                print()
        case 4:
            try:
                cursos = funciones.listarCursoById()
                if (cursos != 0):
                    codigoEliminar = funciones.pedirDatosEliminacion(cursos)
                    if not (codigoEliminar == ""):
                        funciones.eliminarCurso(codigoEliminar)
                    else:
                        print(
                            "Código del curso no encontrado y Ingrese un Código valido")
                else:
                    print("No se encontraron Cursos.")
            except:
                print("Eliminar, Ocurrio un Error!")
            print("")
        case 5:
            print("¡Gracias por usar este Sistema!-:")
            print(" ")
        case _:
            print("Sorry!, Opción no Valida!")


menuPrincipal()
