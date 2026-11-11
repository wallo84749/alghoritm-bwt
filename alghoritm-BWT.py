def quickSort(lista):
    if len(lista) <= 1:
        return list
    
    pivot = list[-1]

    left = []
    right = []

    for elemento in lista[:-1]:
        if elemento < pivot:
            left.append(elemento)
        else:
            right.append(elemento)

    return quickSort(left) + [pivot] + quickSort(right)

str = input("write some string: ")

ris = ""
strBWT = str + "$"
strList = [strBWT]
strLenght = len(strBWT)

for i in range(strLenght - 1):
    
    rmFrstElm = strBWT[i + 1:]
    strElms = strBWT[:i + 1]
    BWT_elms = rmFrstElm  + strElms
    strList.append(BWT_elms)

print("rotazione completa dell'algoritmo: ", strList)  


strList = quickSort(strList)

for elemento in strList:
    ris += elemento[-1]
    
print("stringa con implementazione dell'algoritmo: ", ris)

