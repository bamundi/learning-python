#Array = Lista en Python
#Estructura de Datos
#Contiene multiples valores que estan indexados

arregloejemplo = [1,2,35,10,1,2000,"Hola mundo",3.2]

arreglo = [10,9,8,10,7,10,8]

print "Mi primera calificacion fue "+ str(arreglo[0])

arreglo[6] = 8 #reasignar un valor al array

print arreglo

print arreglo[2:5] #imprimir un rango de valores del array

#imprimir todos los valores del array 
for x in arreglo: 
	print x

#imprimir lenght del array
print len(arreglo) 

#imprimir elementos de un arreglo segun la cantidad de ellos
print "imprimir elementos de un arreglo segun la cantidad de ellos"
for x in xrange(len(arreglo)):
	print "En la posicion "+ str(x) +" se encuentra " + str(arreglo[x])

	#promedio de calificaciones
suma_calificaciones = 0
for x in xrange(len(arreglo)):
	suma_calificaciones = suma_calificaciones + arreglo[x]
	y = float(suma_calificaciones) / len(arreglo) 
print "La suma de todas las calificaciones es " + str(suma_calificaciones)
print "Y el promedio es " + str(y)
