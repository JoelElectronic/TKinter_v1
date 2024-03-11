from tkinter import * #importamos la libreria TKINTER con todas sus funciones
root = Tk() #Ventana

root.title("Posición de widgets") #Titulo de la ventana
root.geometry("400x200") #Tamaño de la ventana
root.resizable(0,0)
def logeo():    #Función mensaje
    print("Bienvenido")
def iterador():     #Función mensaje
    print("boton que hara rotar los colores")

# POCISIONAMIENTO METODO GRID
texto1 = Label(root, text="hola, soy texto random")
texto1.grid(row=0, column=0)

texto2 = Label(root, text="hola, soy texto random")
texto2.grid(row=0, column=1)


# POCISIONAMIENTO METODO PLACE

boton_igresar = Button(root, text="Ingresar", command=logeo, bg="coral3")
boton_igresar.place(x=90, y=40)

boton_color = Button(root, text="color", command=iterador, bg="salmon2")
boton_color.place(x=270, y=40)


root.mainloop()