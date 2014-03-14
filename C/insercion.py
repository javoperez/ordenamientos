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

def insertar(Arreglo):
	aux=[]
	comparaciones=0
	for i in range(1, len(Arreglo)):

		j= i
		aux=Arreglo[i]
		
		if (aux>Arreglo[j-1]):
			comparaciones+=1
		
		while(j>0 and aux<Arreglo[j-1]):
			comparaciones+=1
			Arreglo[j] = Arreglo[j-1]
			j=j-1

		Arreglo[j]=aux
	print "comparaciones: ", comparaciones
	return Arreglo


lista= llenarLista()
print "la lista era", lista
start= time.time()
ordenado= insertar(lista)
end= time.time()
ejecucion= end-start
print "el ordenamiento es: ", ordenado
print "El tiempo de ejecucion fue: ", ejecucion*(10**6), "micro segundos"