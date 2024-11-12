#Valores de entrada que provienen de diferentes lugares 
#El dia de hoy arenderemos a ingresar por via teclado
'''
nombre_completo = input("Ingresa tu nombre completo : ") # Siempre regresara tipo de dato 'str'
#Input recibe como argumento de forma opcional un mensaje
#siempre colocar un mensaje para poder ingresar el valor

print(nombre_completo)
print(type(nombre_completo))


edad_player =input("ingresa tu edad: ")
edad_player = int(edad_player)

print(edad_player)
print(type(edad_player))

altura = input("Ingresa tu altura : ")
#foat permite crear un nuevo flotante a partir de un string
altura = float(altura)

print(altura)
print(type(altura))

autorizacion_programa = input("Autorizas el programa? (si/no)")
autorizacion_programa = autorizacion_programa == 'si'
#Si la respuesta fuese 'no' resultado sera False
print(autorizacion_programa)
'''

''' son muchas lineas 
de codigo, por lo cual se puede hacer
mas simplificado haciendo lo siguiente :'''

nombre_completo = input("Ingresa tu nombre completo : ") # Siempre regresara tipo de dato 'str'

edad_player =int(input("ingresa tu edad: "))

altura_player = float(input("Ingresa tu altura : "))

autorizacion_programa = input("Autorizas el programa? (si/no) : ") == 'si'

print(nombre_completo)
print(edad_player)
print(altura_player)
print(autorizacion_programa)