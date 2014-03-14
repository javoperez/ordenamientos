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

def intercambiar(Arreglo):
	aux=[]
	comparaciones=0
	for i in range (0, len(Arreglo)-1):
		for j in range (i+1, len(Arreglo)):
			comparaciones+=1
			if (Arreglo[i]>Arreglo[j]):
				aux = Arreglo[i];
				Arreglo[i] = Arreglo[j];
				Arreglo[j]= aux ;
				
	print "comparaciones :", comparaciones
	return Arreglo
	

lista= llenarLista()
#print "la lista era: ", lista

start= time.time()
ordenado= intercambiar(lista)
end=time.time()
ejecucion= end-start
print "El tiempo de ejecucion fue: ", ejecucion*(10**6), "micro segundos"

print "queda ordenada asi: ", ordenado



