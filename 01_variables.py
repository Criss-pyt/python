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

#Imputs

first_name = imput ("What is your name: ")
age = imput ("How old are you? ")

print(first_name)
print(age)
