lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust"]

#[start:end]
#[start:] Obtenemos los ultimos elementos de la lista apartir de ese numero creando una sub lista
#[:end] Obtenemos los primeros elementos de la lista hasta ese numero 
#[start:end:skip] Se puede generar sublista haciendo saltos como uno si y otro no 

sub_lista = lista_cursos[1:5:2]
print(sub_lista)