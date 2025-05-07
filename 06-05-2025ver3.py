import tkinter as tk


def saludar():
    nombre = entrada_sal.get()
    etiqueta_resultado_sal.config(text=f"Hola {nombre}")

def edades():
    edad = entrada_edad.get()
    etiqueta_resultado_edad.config(text=f"Tu tienes {edad} años <3")


ventana = tk.Tk()
ventana.title("Mi primera App grafica")
ventana.geometry("500x300")
ventana.configure(background='blue')

etiqueta_sal = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta_sal.pack()
etiqueta_sal.configure(background='white')

entrada_sal = tk.Entry(ventana)
entrada_sal.pack()
entrada_sal.configure(background='yellow')

boton_sal = tk.Button(ventana, text=" Mostrar saludo", command=saludar)
boton_sal.pack()

etiqueta_resultado_sal = tk.Label(ventana, text="")
etiqueta_resultado_sal.pack()
etiqueta_resultado_sal.configure(background='blue')

etiqueta_edad = tk.Label(ventana, text="ingresa tu edad:")
etiqueta_edad.pack()
etiqueta_edad.configure(background='blue')

entrada_edad = tk.Entry(ventana)
entrada_edad.pack()
entrada_edad.configure(background='yellow')

boton_edad = tk.Button(ventana, text="Mostrar edad", command=edades)
boton_edad.pack()

etiqueta_resultado_edad = tk.Label(ventana, text="")
etiqueta_resultado_edad.pack()
etiqueta_resultado_edad.configure(background='blue')


etiqueta = tk.Label(ventana, text="¡Realizadoo por!-> Jasmin Espinosa")
etiqueta.pack()
etiqueta.configure(background='blue')

ventana.mainloop()
