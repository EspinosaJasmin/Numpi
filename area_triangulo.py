import tkinter as tk

def calcular_area():
    try:
        base_str = entrada_base.get()
        altura_str = entrada_altura.get()
        base = float(base_str)
        altura = float(altura_str)
        area_triangulo = (base * altura) / 2
        etiqueta_resultado_area.config(text=f"El área es: {area_triangulo:.2f}")
        if area_triangulo > 100:
            etiqueta_tamano_area.config(text="El área es grande.")
        else:
            etiqueta_tamano_area.config(text="El área es pequeña.")
    except ValueError:
        etiqueta_resultado_area.config(text="Por favor, ingresa números ")
        etiqueta_tamano_area.config(text="")


ventana = tk.Tk()
ventana.title("Calculadora de Área de Triángulo")
ventana.geometry("300x300")
ventana.configure(background='yellow')


etiqueta_base = tk.Label(ventana, text="Ingresa la base:")
etiqueta_base.pack(pady=5)
etiqueta_base.configure(background="light gray")
entrada_base = tk.Entry(ventana)
entrada_base.pack(pady=5)
entrada_base.configure(background='light gray')


etiqueta_altura = tk.Label(ventana, text="Ingresa la altura:")
etiqueta_altura.pack(pady=5)
etiqueta_altura.configure(background='light gray')
entrada_altura = tk.Entry(ventana)
entrada_altura.pack(pady=5)
entrada_altura.configure(background='light gray')


boton_calcular = tk.Button(ventana, text="Calcular Área", command=calcular_area)
boton_calcular.pack(pady=10)
boton_calcular.configure(highlightbackground="yellow", highlightthickness=0)


etiqueta_resultado_area = tk.Label(ventana, text="")
etiqueta_resultado_area.pack(pady=5)
etiqueta_resultado_area.configure(background='yellow')


etiqueta_tamano_area = tk.Label(ventana, text="")
etiqueta_tamano_area.pack(pady=5)
etiqueta_tamano_area.configure(background='yellow')


ventana.mainloop()