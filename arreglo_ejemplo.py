# arreglo = []
# x = int(raw_input("Ingrese su primera nota: "))
# y = int(raw_input("Ingrese su segunda nota: "))
# z = int(raw_input("Ingrese su tercera nota: "))
# arreglo.insert(0,x)
# arreglo.insert(1,y)
# arreglo.insert(2,z)

# suma_valores = 0
# for i in xrange(len(arreglo)):
# 	suma_valores = suma_valores + arreglo[i]
# print "La suma de tus notas es: " + str(suma_valores)
# print "El promedio de tus notas es: " + str(float(suma_valores) / len(arreglo))



calificacion = 0
calificaciones = []
i = 1

print "*** Para salir ingresa numero negativo ***"
while calificacion >=0:
	calificacion = int(raw_input("Dame la calificacion " + str(i)+ ": "))
	if calificacion >=0:
		calificaciones.append(calificacion)
	i = i + 1

suma = 0
for cal in calificaciones:
	suma = suma + cal
print "Tu promedio es: "+ str(suma/len(calificaciones))
