# Sumatorio con recursividad, se vuelve totalmente loco.
# El if nunca permite devolver nada en sumatorioLoco porque no pasa por un return
# El otro es correcto, poniendo un else

def sumatorioLoco(n):
    if n>0:
        valor= n + sumatorioLoco(n-1)
    return valor

def sumatorio(n):
    if n>0:
        valor= n + sumatorio(n-1)
    else:
        return 0
    return valor


print(sumatorio(100))
