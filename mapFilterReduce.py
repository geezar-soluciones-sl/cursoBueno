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
# EN RESUMEN: REDUCE NO HACE LA FUNCION SOBRE EL PRIMER ELEMENTO
sumatorioDobleMal = reduce(lambda x,y: x + y*2, lista)

# PARA CORREGIR EL REDUCE, HACEMOS COPIA DE LA LISTA CON UN 0 EN EL PRIMER ELEMENTO
listaParaReduce=lista[:]
listaParaReduce.insert(0,0)
sumatorioDobleCorrecto= reduce(lambda x,y: x + y*2, listaParaReduce)


# Saco resultados para que se vean en fase de pruebas
print(lista)
print(list(listaRomanos))
print(list(listaPares))
print(sumatorio)
print(sumatorioDobleMal)
print(sumatorioDobleCorrecto)

