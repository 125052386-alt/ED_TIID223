#declaramos un arreglo de 5 pocisiones
numeros=[10,20,30,40,50]

#Impirmimos la pocisiones 3 del arreglo numeros(30)0
print(numeros[2])

#reasignamos el valor de la posicion 3 en arreglo numeros
numeros[3]=15
print(numeros)

#Agregamos un valor nuevo al final del arreglo
numeros.append(60);
print(numeros)

#Eliminamos la posicion 1 del arreglo numeros
numeros.pop(1)
print(numeros)

#eliminas el valor numero 30 del arrglo numeros
numeros.remove(30)
print(numeros)

frutas=["Mango","Manzana","Uva","Pera","Maracuya"]

frutas.remove("Uva")
print(frutas)

frutas.pop(3)
print(frutas)

frutas.append("kiwi")
print(frutas)

frutas[2]="Fresa"
print(frutas)

arreglo=[]

tamaño=int(input("Ingrese el tamaño del arreglo: "))

""" for i in range(tamaño):
    valor=int(input("Ingrese el valor de la pocision "+str(i)+": "))
    arreglo.append(valor)
print(arreglo) """

valor1 = int(input("Ingrese el valor 1: "))
arreglo.append(valor1)
print(arreglo)