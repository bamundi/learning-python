calificacion = 0
calificaciones = []
i = 1

def agregar_calificacion(arreglo,elemento):
	if elemento >=0:
		arreglo.append(elemento)



print "*** Para salir ingresa numero negativo ***"
while calificacion >=0:
	calificacion = int(raw_input("Dame la calificacion " + str(i)+ ": "))
	agregar_calificacion(calificaciones, calificacion)
	i = i + 1

suma = 0
for cal in calificaciones:
	suma = suma + cal
print "Tu promedio es: "+ str(suma/len(calificaciones))
