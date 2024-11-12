###Operadores Logicos###
#Permite convinar 2 o mas valores boolianos
#El resultado es un valor booleano

#"""
#   and: si todos los valores son True, muestra True
#   or : si uno de los valores es True, muestra True
#   not: negacion, como: si es True, muestra False y viceversa
#"""
# and, or, not

print("Operador logico and")

resultado_final = True and True and True
print(resultado_final)

#Con un operador que de false, el resultado sera false 
resultado_final = True and True and False
print(resultado_final)

print("Operador logico or")
resultado_final = True or True or True
print(resultado_final)

#Con un operador que de false, el resultado sera false 
resultado_final = False or False or True
print(resultado_final)

print("Operador logico not")
resultado_final = not True
print(resultado_final)

resultado_final = not False 
print(resultado_final)

print("Agrupacion de operadores logicos")

resultado_final = True and (True and False)
print(resultado_final)

resultado_final = True and (False or True)
print(resultado_final)

print("Combinando operadores relacionales y logicos")

resultado_final = 20 > 10 and True
print(resultado_final)

resultado_final = 300 < 10 or (False or True)
print(resultado_final)

#Combianando operadores relacionales y logicos con variables
print("Combianando operadores relacionales y logicos con variables")
numero_uno = 10
numero_dos = 20

resultado_final = numero_uno > numero_dos and numero_uno < numero_dos
print(resultado_final)

#Parentesis para las operaiones y hacer mas lejible el codigo
resultado_final = (numero_uno > numero_dos) and (numero_uno < numero_dos)
print(resultado_final)