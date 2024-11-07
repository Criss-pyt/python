#Cuenta de restaurante

monto= float(input ("¿Cual es el monto de su cuenta?"))
porcentaje= float(input ("¿Cuanto porcentaje de propina quisiera dar ?"))


total= monto * (porcentaje / 100)

print(f"El total a pagar de su comida es de : $",  (total + monto))

