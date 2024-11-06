#Cuenta de restaurante

monto= input ("¿Cual es el monto de su cuenta?")
porcentaje= input ("¿Cuanto porcentaje de propina quisiera dar ?")
print(monto)
print(porcentaje)

cuenta_total=(monto * (porcentaje / 100))
print(cuenta_total)

print(f"El total a pagar de su comida es de (cuenta_total)")

