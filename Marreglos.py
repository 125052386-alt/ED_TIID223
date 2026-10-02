
""" Consultar Un elemento """
""" numeros=[10,20,30,40,50]
print(numeros[2]) """

""" Modificar Un elemento """
""" numeros=[10,20,30,40,50]
numeros[2]=100
print(numeros) """


""" Agregar Un elemento """
""" numeros=[10,20,30,40,50]
numeros.append(60)
print(numeros) """

""" Agregar mas de 1 elemento """
""" numeros=[10,20,30,40,50]
numeros.append([60,70])
print(numeros) """

""" numeros=[10,20,30,40,50]
numeros.append(60)
numeros.append(70)
print(numeros) """

""" numeros=[10,20,30,40,50]
numeros.append([60,70])
print(numeros[5])
 """


""" numeros=[10,20,30,40,50]
numeros.append([60,70])
print(numeros[5][0]) """


""" Insert"""
""" numeros=[10,20,30,40]
numeros.insert(2,25)
print(numeros) """

""" numeros=[10,20,30,40]
numeros=numeros+[50]
print(numeros) """

""" numeros=[10,20,30,40]
numeros=numeros+[50,60,70]
print(numeros) """

""" numeros=[10,20,30]
otros_numeros=[40,50,60]
numeros.extend(otros_numeros)
print(otros_numeros)
"""  """
numeros=[10,20,30]
numeros[len(numeros):]=[40]
print(numeros) """

""" calificaciones=[70,85,90,65]
calificaciones.insert(2,80)
print(calificaciones) """


""" colores=["azul","amarillo","rosa"]
colores.append("verde")
colores.append("Morado")
colores.append("Rojo")
print(colores)
colores.append("Negro")
print(colores[6]) """

numeros=[10,20,30,40]
numeros.insert(2,95)
numeros.append(50)
numeros.append(67)
""" print(numeros) """
""" print(numeros[2]) """
""" print(numeros[6]) """
for i in range(len(numeros)):
    print("Posición", i, "es", numeros[i])
