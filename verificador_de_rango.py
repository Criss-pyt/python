#comando float: ayuda a poder convertir los numeros a decimales 
#comando imput: ''''ayuda a poder realizar un problema matematico 
#convirtiendo el numero de la cadena de texto ingresada por el input

numero = float(input("Pon un numero aleatorio:"))
numero_ganador = 15

if 5 <= numero <= 25: print("El numero esta en el rango")
else: print("El numero no esta en el rango")

if(numero) == (numero_ganador) :print("Felicidades eres el ganador")
else :print("Perdistes")