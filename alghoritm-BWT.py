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


for i in range(len(strList)):

    for j in range(len(strList) - 1 - i):

        if strList[j] > strList[j + 1]:

            temp = strList[j]
            strList[j] = strList[j + 1]
            strList[j + 1] = temp
        
for elemento in strList:
    ris += elemento[-1]
print("stringa con implementazione dell'algoritmo: ", ris)

