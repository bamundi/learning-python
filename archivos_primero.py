# R = archivos de lectura, read
archivo = open("ejemplo.txt","r")
matriz = []

#Split nos ayuda a definir que caracter queremos que separe nuestors elementos
for linea in archivo:
	arreglo_con_cadenas = linea.split(",")
	arreglo = []
	for j in range(len(arreglo_con_cadenas)):
		numero_sin_caracteres = int(arreglo_con_cadenas[j])
		arreglo.append(numero_sin_caracteres)
	matriz.append(arreglo)

numero_uno = int(raw_input("Dame el primer numero a multiplicar: "))
numero_dos = int(raw_input("Dame el segundo numero a multiplicar: ")) 

print "El resultado de "+ str(numero_uno)+ " x "+ str(numero_dos)+ " es: "+ str(matriz[numero_uno][numero_dos])
	