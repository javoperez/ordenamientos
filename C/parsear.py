archivo = "lista.txt"
try:
    f = open(archivo,"r")
except IOError:
    f.close()
    exit()
contenido = f.readlines()
f.close()
lista= []
for numero in contenido:
   lista += numero.split() #Le quita los espacios
lista = map(int, lista)
print lista
