# Variables 

my_string_variable= "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable )
print(type(my_int_to_str_variable ))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variable, str(my_int_variable), my_bool_variable)
print("Este es el valor de:",my_bool_variable)

# Algunas funciones de el sistema 
print(len(my_string_variable))
# len = contar 

# Variables en una sola linea ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", "MoureDev", 35
print("Me llamo:", name, surname, ". Mi edad es:" , age, ". Y mi alias es:", alias )

#Inputs
'''
name = input ("¿Cual es tu nombre? ")
age = input ("¿Cuantos años tienes? ")
print(name)
print(age)
'''

# Cambiamos su tipo 
name = 35
age = "Brais"
print(name)
print(age)

# ¿Forzamos el tipo ?
address: str = "Mi direccion"
address = 32 
address = True
address = 5
address = 1.2
print(type(address))


