from tkinter import *
from tkinter import messagebox as MessageBox


class VentanaEjemplo:

    def __init__(self, ventana):

        self.ventana = ventana
        ventana.title("Datos")
        ventana.config(background="light blue")

        self.frame = Frame(ventana, width=500, height=400,
                           background="light blue")
        self.frame.pack()

        self.codigo = Label(self.frame, text="Código acceso:", background="light green", font=(
            "Comic Sans Ms", 12), width=10, anchor='e')
        self.codigo.place(x=10, y=40)

        self.nombre = Label(self.frame, text="Nombre:", background="light green", font=(
            "Comic Sans Ms", 12), width=10, anchor='e')
        self.nombre.place(x=10, y=100)

        self.telefono = Label(self.frame, text="Telefono:", background="light green", font=(
            "Comic Sans Ms", 12), width=10, anchor='e')
        self.telefono.place(x=10, y=160)

        self.correo = Label(self.frame, text="Correo:", background="light green", font=(
            "Comic Sans Ms", 12), width=10, anchor='e')
        self.correo.place(x=10, y=210)

        self.codigoT = Entry(self.frame, background="white", font=(
            "Comic Sans Ms", 12), width=15, justify="center")
        self.codigoT.place(x=120, y=40)

        self.nombreT = Entry(self.frame, background="white", font=(
            "Comic Sans Ms", 12), width=15, justify="center")
        self.nombreT.place(x=120, y=100)

        self.telefonoT = Entry(self.frame, background="white", font=(
            "Comic Sans Ms", 12), width=15, justify="center")
        self.telefonoT.place(x=120, y=160)

        self.correoT = Entry(self.frame, background="white", font=(
            "Comic Sans Ms", 12), width=15, justify="center")
        self.correoT.place(x=120, y=210)

        self.enviar = Button(self.frame, text="Enviar",
                             cursor="hand2", comman=self.verificar)
        self.enviar.place(x=30, y=290)

        self.abrirImagen = Button(
            self.frame, text="Abrir Imagen", cursor="hand2")
        self.abrirImagen.place(x=150, y=290)

        self.abrirVentana = Button(
            self.frame, text="Abrir ventana", cursor="hand2")
        self.abrirVentana.place(x=280, y=290)

    def verificar(self):

        pass

        MessageBox.showinfo("saludo", "Hola mundo")


root = Tk()
miVentana = VentanaEjemplo(root)
root.mainloop()
