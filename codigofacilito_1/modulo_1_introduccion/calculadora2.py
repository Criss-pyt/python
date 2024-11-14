print("Esta sera una calculadora, favor ingresar los datos a calcular : ")
print()

primer_valor = float(input("Ingresa el primer valor : "))

valor_operacion = input("Ingrese el valor de la operacion : ")
segundo_valor = float(input("Ingresa el segundo valor : "))

if valor_operacion == "+":
    print(primer_valor + segundo_valor)
elif valor_operacion == "-":
    print(primer_valor - segundo_valor)
elif valor_operacion == "*":
    print(primer_valor * segundo_valor)
elif valor_operacion == "/":
    print(primer_valor / segundo_valor)
else:
    print("Error")
