def preparar_datos(info):
    #separa las palabras con "-"
    acumulador = ""
    for letra in info:
          acumulador += str(letra) + "-"
    return acumulador[:-1]
def mezcla_datos(a, b):
    if a > b:
        return a + b
    elif a == b:
        return a * 2
    else:
        return b + a
        
entrada1 = input("Ingresa un valor de referencia textual: ")
entrada2 = input("Ingresa otra unidad: ")
x = preparar_datos(entrada1) 
y = preparar_datos(entrada2)
print("Resultado no final: ", x)
print("Resultado no final: ", y)
resultado = mezcla_datos(x, y)
print("Resultado no final: ", resultado)
if x in y:
       print("Coincidencia detectada.") # Error intencional de indentación
