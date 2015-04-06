n = 11
matriz = [[0 for i in range(n)] for j in range(n)]

for i in range(len(matriz)):
	arreglo = matriz[i]
	for j in range(len(arreglo)):
		arreglo[j] = i * j

numero_uno = int(raw_input("Dame el primer numero a multiplicar: "))
numero_dos = int(raw_input("Dame el segundo numero a multiplicar: ")) 

print "El resultado de "+ str(numero_uno)+ " x "+ str(numero_dos)+ " es: "+ str(matriz[numero_uno][numero_dos])
	