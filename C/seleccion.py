import time
def llenarLista():
	archivo = "lista.txt"
	try:
	    f = open(archivo,"r")
	except IOError:
	    f.close()
	    exit()
	contenido = f.readlines()
	f.close()
	l= []
	for numero in contenido:
	   l += numero.split() #Le quita los espacios
	l = map(int, l)
	return l

def seleccionar(Arreglo):
	comparaciones=0

	for i in range (0, len(Arreglo)):
		indiceMenor=i
		for j in range(i+1, len(Arreglo)):
			comparaciones+=1
			if (Arreglo[j] < Arreglo[indiceMenor]):
				indiceMenor = j;
		if (i != indiceMenor):
			aux = Arreglo[i];
			Arreglo[i] = Arreglo[indiceMenor];
			Arreglo[indiceMenor] = aux ;
	print "comparaciones: ", comparaciones
	return Arreglo

lista= llenarLista()
print "la lista era: ", lista
start= time.time()
ordenado= seleccionar(lista)
end= time.time()
ejecucion= end-start

print "El tiempo de ejecucion fue: ", ejecucion*(10**6), "micro segundos"
print "la lista ordenada es: ", ordenado

