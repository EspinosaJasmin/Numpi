import tkinter as tk

def saludar():
    nombre = entrada_sal.get()
    etiqueta_resultado_sal.config(text=f"Hola {nombre}")

def edd():
   edad = entrada_edad.get()
   etiqueta_resultado_edad.config(text=f"Tu tienes {edad} años <3")

ventana = tk.Tk()
ventana.title("Mi primer App Grafica")
ventana.geometry("400x200")

etiqueta_sal = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta_sal.pack()

entrada_sal = tk.Entry(ventana)
entrada_sal.pack()

boton_sal = tk.Button(ventana, text="Mostrar Saludo", command=saludar)
boton_sal.pack()

etiqueta_resultado_sal = tk.Label(ventana, text="")
etiqueta_resultado_sal.pack()

etiqueta_edad = tk.Label(ventana, text="ingresa tu edad:")
etiqueta_edad.pack()

entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

boton_edad = tk.Button(ventana, text="Mostrar edad", command=edd)
boton_edad.pack()

etiqueta_resultado_edad = tk.Label(ventana, text="")
etiqueta_resultado_edad.pack()

ventana.mainloop()