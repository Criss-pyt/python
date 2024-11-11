#Tipado dinamico
'''Ultimo valor asignado a una variable'''
valor = "Criss"
print(valor)
valor = 10
print(valor)
valor = 3.6
print(valor)
valor = True
print(valor)

print(valor)#Al final el valor que imprimira sera el ultimo llamado "True", por ser el ultimo asignado a la variable

#A media vamos actualizando nuestra variable y asignandole un nuevo valor, el valor anterior se va a la memoria... pero

valor2= 15
print(valor2)
print(id(valor2))
valor2 = valor2 + 10
print(valor2)
print(id(valor2))
#Podemos seguir utilizando el valor asignado a la variable, y remplazarlo por uno nuevo
valor2= valor2 + 100
print(valor2)

print(id(valor2))