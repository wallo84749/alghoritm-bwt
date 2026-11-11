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

print(strList)  