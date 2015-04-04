N1 = int(raw_input("ingresa el primer valor: "))
N2 = int(raw_input("ingresa el segundo valor: "))
N3 = int(raw_input("ingresa el segundo valor: "))

if N1 > N2:
	if N1 > N3:
		if N2 > N3:
			print str(N1)+ "..."+ str(N2)+ "..."+ str(N3)
		else:
			print str(N1)+ "..."+ str(N3)+ "..."+ str(N2)
	else:
		print str(N3)+ "..."+ str(N1)+ "..."+ str(N2)
else:
	if N2 > N3:
		if N1 > N3:
			print str(N2)+ "..."+ str(N1)+ "..."+ str(N3)
		else:
			print str(N2)+ "..."+ str(N3)+ "..."+ str(N1)
	else:
		print str(N3)+ "..."+ str(N2)+ "..."+ str(N1)


