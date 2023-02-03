# from BD.conexion import DAO
# import  conexion
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
                funciones.listarCursos()
                print("")
            except:
                print("Listar Cursos, Ocurrió un Error!")
                print(" ")
        case 2:
            curso = funciones.pedirDatosRegistro()
            try:
                funciones.registrarCurso(curso)

            except:
                print("Registrar Curso, Ocurrió un Error!")
                print(" ")
        case 3:
            return "I'm a teapot"
        case 4:
            try:
                cursos = funciones.listarCursoById()
                if len(cursos) > 0:
                    codigoEliminar = funciones.pedirDatosEliminacion(cursos)
                    if not (codigoEliminar == ""):
                        funciones.eliminarCurso(codigoEliminar)
                    else:
                        print("Código del curso no encontrado.")
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
