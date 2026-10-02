""" Ejemplo de arreglo Bidimensional """

""" matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Mostra Matriz")
for fila in matriz:
    print(fila)

print("Mostrar fila 0")
print(matriz[0]) 

print("Mostrar Mostar arreglo de fila 1 columna 2")
print(matriz[1][2])  

print("elimina el elemento 3 de la primera fila")
matriz[0].pop(2)  
print(matriz) """

""" Ejemplo de Colas """
from collections import deque 

cola=deque(["Ana", "Carlos"])

cola.append("Andres")
cola.append("Jorge")

atendido=cola.popleft()
print(f"se atendio a: {atendido}")

print("cola restante:",cola) 


atendido=cola.popleft()
print(f"se atendio a: {atendido}")

print("cola restante:",cola) 

