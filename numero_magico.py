numero_magico = int(raw_input("Ingresa un numero magico: "))
numero_no_magico = int(raw_input("Adivina el numero magico: "))

while numero_magico != numero_no_magico:
	if numero_magico > numero_no_magico:
		numero_no_magico = int(raw_input("Ingresa un numero mas grande: "))
	else:
		numero_no_magico = int(raw_input("Ingresa un numero mas bajo: "))
print "Adivinaste!"