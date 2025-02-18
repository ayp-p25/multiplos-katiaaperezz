"""
Multiplos
"""
try:
# Entradas
    numero_1 = int(input("Introduzca un número:"))
    numero_2 = int(input("Introduzca otro número:"))
#Proceso
    if numero_2 != 0:
        if numero_1 % numero_2 == 0:
            resultado = "El número " + str(numero_1) + " es múltiplo del " + str(numero_2) 
        elif numero_2 % numero_1 == 0:
            resultado = "El número " +  str(numero_2) + " es múltiplo del " + str(numero_1) 
        else:
            resultado = "Ninguno de los números es múltiplo del otro"
    else: 
        resultado= "El número " + str(numero_2) + " es múltiplo del " + str(numero_1) 
        
except ValueError:
      resultado = "Introduzca otro valor."
# Salidas
print(resultado)
