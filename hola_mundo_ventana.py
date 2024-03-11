from tkinter import *

root = Tk() #creamos una ventana
texto = Label(root, text="Hola mundo en tkinter")#creamos una etiqueta
texto.pack()#mostramos la etiqueta en la ventana

root.mainloop() #comando necesario para mantener abierta la ventana
