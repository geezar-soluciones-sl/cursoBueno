def maxLista(l):
    if len(l)==0:
        return 0
    max=0
    
    for i in range (0,len(l)):
        if l[i]>max:
            max=l[i]    
    return max

def minLista(l):
    if len(l)==0:
        return 0
    min=l[0]
    
    for i in range (0,len(l)):
        if l[i]<min:
            min=l[i]
    
    return min

def medLista(l):
    if len(l)==0:
        return 0
    med=0    
    for i in range (0,len(l)):
        med += l[i]
    
    return med/len(l)

if __name__ == "__main__":
    lista=[4,7,11]
    print("Máximo: ",maxLista(lista))
    print("Mínimo: ",minLista(lista))
    print("Media: ",medLista(lista))
