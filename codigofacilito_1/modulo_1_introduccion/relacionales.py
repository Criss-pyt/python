numero_uno = 10
numero_dos = 20

#Siempre devuelven resultados tipo booliano
#Son operadores racionales

"""
    > mayor que 
    < menor que
    >= mayor o igual que 
    <= menor o igual que
    == igual
    != diferente
"""

resultado = numero_uno > numero_dos
print(resultado)

resultado = numero_uno < numero_dos
print(resultado)

resultado = numero_uno >= numero_dos
print(resultado)

resultado = numero_uno <= numero_dos
print(resultado)

resultado = numero_uno != numero_dos
print(resultado)

resultado = numero_uno == numero_dos
print(resultado)

print()

#Comparacion de datos tipo string

nombre_uno = "Criss"
nombre_dos = "Jose"

resultado = nombre_uno == nombre_dos
print(resultado) 

resultado = nombre_uno != nombre_dos
print(resultado) 

#evalua en un orden alfabeticamente, lexicografio, puede ser sensible a mayusculas y minusculas
#atravez de el codigo ASCII 
resultado = nombre_uno < nombre_dos
print(resultado) 