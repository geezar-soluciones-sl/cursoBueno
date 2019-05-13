# Ejemplo recursividad: Un contador hacia atrás.
# Recursividad es una función que se llama a sí misma.
# SIEMPRE cuidado de que no se hagan llamadas hasta el infinito (en este caso el if)

def retroContador(entrada):
    print(entrada,",",end="")
    if entrada>0:
        retroContador(entrada-1)
    
retroContador(10)

          

