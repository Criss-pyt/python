calificacion = 10
color = None
'''
if calificacion >= 7:
    color = 'Verde' 
else:
    color = 'Rojo'
'''
#Estas lineas de codigo se pueden comrpimir en una sola como a continuacion
#Se usa el equivalente de color ternario

color = 'Verde' if calificacion >= 7 else 'Rojo'

print(calificacion, color)
