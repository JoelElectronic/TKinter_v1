from tkinter import *
root = Tk()


def ipm ():
    print("Acabas de presionar un boton")

def ipm_w():
    texto= Label(root, text=("Acabas de presionar un boton"))
    texto.pack()

root.geometry("500x600") #tamaño de la ventana

boton1 = Button(root, text="Minimizar", command=root.iconify, bg="DodgerBlue3")# texto del boton, comado que ejecutara el boton y el color del boton
boton1.pack(side=LEFT) #Mostramos el boton y lo ubicamos del lado izquierdo

boton2 = Button(root, text="imprimir", command=ipm_w, bg="SkyBlue1")
boton2.pack(side=RIGHT) #Mostramos el boton y lo ubicamos del lad derecho

root.mainloop()
