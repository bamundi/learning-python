#Python ya viene con una funcion para sacar el factorial
#solo debemos llamarla
from math import factorial
print factorial(6)

#Podemos crear nuestra propia funcion NO recursiva
def my_factorial(n):
	factorial_total =1
	while n > 1:
		factorial_total *= n
		n -= 1
	return factorial_total

print my_factorial(6)

#Podemos crear una funcion SI recursiva

def mi_factorial(n):
	if n > 1:
		return n * mi_factorial(n-1)
	return 1

print mi_factorial(7)