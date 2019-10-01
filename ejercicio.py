def metodoUno(a):
	return a ** 2
# Segundo método
def metodoDos(b):
	return b + 1
# Tercer método
def metodoTres(c):
	return c + 100
# Cuarto método
def metodoCuatro(d):
	return d * 3
# Presentación de resultados
print(metodoUno(3))
print(metodoDos(metodoUno(4)))
print(metodoTres(metodoDos(metodoTres(5))))
print(metodoCuatro(metodoTres(metodoDos(metodoUno(2)))))