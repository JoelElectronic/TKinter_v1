from tkinter import *

root = Tk()
def texto (msg) : #funcion para escribir mensajes
    texto = Label(root, text= msg)#asignamos ala variable texto un mensaje
    texto.pack()#mostramos dicho mensaje en la ventana
texto  ("hola bro")


root.title("Interfaz de estados") # colocamos un titulo a la ventana

root.geometry("900x500") # configuramos las dimensiones de nuestra ventana

root.iconbitmap("OIP.ico") #Me permite cargar una imagen en el icono de la ventana. NOTA: la imagen debe estar cargada en la misma carpeta del proyecto

root.resizable(False,False) #Eliminamos la posiblidad de ajustar el tamaño de la ventana

root.config(bg="#808080")


root.mainloop()
