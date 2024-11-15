lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]
'''
#Forma ascendente
lista.sort()
#Forma descendente
lista.sort(reverse=True)

print(lista)
'''
'''
lista.sort()
print(lista[0]) #menor
print(lista[-1]) # mayor
'''
'''
#minimo - maximo
print(min(lista))
print(max(lista))
'''
'''
#Ver si esta en la lista 
print(5 in lista)
#Ver si no esta en la lista
print(11 not in lista)
'''

print(5 in lista)

#Retorna el indice donde se encuentra el elemento
index = lista.index(5)

print(index)

