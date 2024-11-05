 ### Operadores Aritmeticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3) # Modulo = solo deja el numero restante de la division en las veces que puede tener el numero grande o principal 
print(10 // 3) # Division de numero entero (Operador de Division entera) solo muestra las veces que cabe dentro de ek numero que se divide 
print( 2 ** 3) #Operador de exponencia (potencia) multiplica su valor por la potencia asignada 
print(2 ** 3 + 3 - 7 / 1 // 4)

print("Hola" + "Python" + "¿Que tal?")
print("Hola " + str(5))
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

###Orden de operadores matematicos###
'''
print(2 ** 3) + (3 - 7) / (1 // 4))
       8          -4        4
             8 + -4        4/4            
                             =1

print(2 ** 3 + 3 - 7 / 1 // 4)
         8          7  
                       1
             11
                 10
print( (2 ** 3) + 3 - ((7 / 1) // 4))
                 print(2 ** 3 + 3 - 7 / 1 // 4)
'''
#print(2 ** 3 + 3 - 7 / 1 // 4)

print( (2 ** 3) + 3 - ((7 / 1) // 4))

### Operadores Comparativos ###

'''
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 = 4)
print(3 =/ 4)
print(3 > 4 = 2) 
'''

'''
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa") #Ordenacion alfabetica
print(len("aaaa") <= len("abaa") #Cuenta caracteres
print("Hola" = "Hola")
print("Hola" =/ "Python")
'''

###Operadores Logicos### 

print(3 > 4 and "Hola" > "Python")
print(3 >4 or "Hola > Python")
print(not(3 > 4))

### F string ###
a = 5
b = 10
r = a + b 
print( "resultado :" + str(r))

print( f"resultado :{r}")

