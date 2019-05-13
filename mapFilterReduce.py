from functools import reduce

def romanos(x):
    return None

lista = [4,7,11]

listaDobles = map(lambda x: x*2, lista)

listaRomanos = map (romanos, lista)

listaPares = filter(lambda x: x%2==0, lista)

# HAcemos el sumaTodos de otros ejercicios con un Reduce
sumatorio=reduce(lambda x,y : x+y, lista)
#Ojo con este, el primero lo coge tal cual pero no lo doble, porque l reduce es as´.
# Coger x como el primero y actuar sobre el resto
sumatorioDoble = reduce(lambda x,y: x + y*2, lista)


print(lista)
print(list(listaRomanos))
print(list(listaPares))
print(sumatorio)
print(sumatorioDoble)

