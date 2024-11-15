lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust"]
lista_cursos2 = ["C", "C++", "Docker"]
print(len(lista_cursos))
#Permite añadir  un nuevo elemento al final de la lista
lista_cursos.append("MongoDB")
lista_cursos.append("C#")
lista_cursos.append("JavaScript")
#Permite añadir un elemento a partir de un indice en concreto
lista_cursos.insert(1, ("Rails"))
lista_cursos.insert(0, ("PyGame"))
#Añade los elementos de la lista 2 a la lista numero 1 sin modificarla
lista_cursos.extend(lista_cursos2)

print(lista_cursos)
print(lista_cursos2)
print(len(lista_cursos))
#Elimina un elemento de la lista
lista_cursos.remove("MongoDB")
#Elimina el elemento a e eliminar por medio de un indice
del lista_cursos[0]
#Elimina toda la lista
lista_cursos.clear()

print(len(lista_cursos))
print(lista_cursos)