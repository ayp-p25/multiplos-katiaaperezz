"""
Multiplos
"""

# Entradas
numero_1 = int(input("Introduzca un número:"))
numero_2 = int(input("Introduzca otro número:"))
if numero_2 != 0:
# Proceso
    if numero_1 % numero_2 == 0 :
        resultado = "El número " + str(numero_1) + " es múltiplo del " + str(numero_2) + "."
    elif numero_2 % numero_1 == 0:
        resultado = "El número " +  str(numero_2) + " es múltiplo del " + str(numero_1) + "."
    else:
        resultado = "Ninguno de los números es múltiplo del otro"
else: 
    resultado = "Error, intente con otro número."
# Salidas
print(resultado)
