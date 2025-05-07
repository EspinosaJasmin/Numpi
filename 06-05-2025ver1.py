import tkinter as tk

def saludar():
    nombre = entrada.get()
    etiqueta_resultado_sal.config(text=f"Hola {nombre}")

ventana = tk.Tk()
ventana.title("Saludo")
ventana.geometry("300x150")

etiqueta_sal = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta_sal.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton_sal = tk.Button(ventana, text="Saludar", command=saludar)
boton_sal.pack()

etiqueta_resultado_sal = tk.Label(ventana, text="")
etiqueta_resultado_sal.pack()

ventana.mainloop()