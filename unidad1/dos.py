from tkinter import Tk, Label, Entry, Frame, Button


ventanaPrincipal = Tk()
ventanaPrincipal.title("Mario shop")  
ventanaPrincipal.geometry("280x300")  


mensajeInicial = Label(ventanaPrincipal, text=" encuentree su teléfono perfecto")
mensajeInicial.pack(pady=10)


marco = Frame(ventanaPrincipal, width=120, height=120)
marco.pack(pady=10)

etiquetaMarca = Label(marco, text="Ingresa la marca:",bg="light blue")
etiquetaMarca.pack()
entradaMarca = Entry(marco)
entradaMarca.pack()

etiquetaReferencia = Label(marco, text="Ingresa la referencia:", bg="light blue")
etiquetaReferencia.pack()
entradaReferencia = Entry(marco)
entradaReferencia.pack()

etiquetaAlmacenamiento = Label(marco, text="Ingresa el almacenamiento en gb:", bg="light blue")
etiquetaAlmacenamiento.pack()
entradaAlmacenamiento = Entry(marco)
entradaAlmacenamiento.pack()

etiquetaColor = Label(marco, text="Ingresa el color:", bg="light blue")
etiquetaColor.pack()
entradaColor = Entry(marco)
entradaColor.pack()

botonBuscar = Button(ventanaPrincipal, text="Buscar", bg="pink")
botonBuscar.pack(pady=15)

ventanaPrincipal.mainloop()
