import time

def leerdatos():	
	archivo = "lista.txt"
	try:
	    f = open(archivo,"r")
	except IOError:
	    f.close()
	    exit()
	contenido = f.readlines()
	f.close()
	Array= []
	for numero in contenido:
	   Array += numero.split() #Le quita los espacios
	Array = map(int, Array) #Convierte los strings a enteros
	return Array


def burbuja(l): 
	""" sale del ciclo de pasadas, en cuanto detecta 
	que al final de una pasada no se realizaron 
	intercambios.""" 
	interruptor=1 
	pasada=1 
	comparaciones= 0
	while pasada<len(l) and interruptor==1:
		interruptor=0 
		for i in range(0,len(l)-pasada): 
			comparaciones+=1
			if l[i] > l[i+1]: 
				l[i], l[i+1] = l[i+1], l[i] 
				interruptor=1 
		pasada += 1 
		
	print "comparaciones: ", comparaciones
	return l 



lista=leerdatos()
#print "la lista era", lista
start= time.time()
x= burbuja(lista)
end= time.time()
ejecucion= end-start
print "La lista quedo asi: ", x
print "El tiempo de ejecucion fue: ", ejecucion*(10**6), "micro segundos"

