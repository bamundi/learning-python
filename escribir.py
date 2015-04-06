n = 10
matriz = [[0 for i in range(n)] for j in range(n)]

for i in range(len(matriz)):
	arreglo = matriz[i]
	for j in range(len(arreglo)):
		arreglo[j] = i * j

#w = escribir archivo borrando contenido previo
#a = escribir archivo agrefando contenido 
#r = leer archivo 
archivo = open("ejemplo.txt","w")

for arreglo in matriz:
	for j in range(len(arreglo)):
		numero = arreglo[j]
		archivo.write(str(numero)+",")
		archivo.write("\n")
