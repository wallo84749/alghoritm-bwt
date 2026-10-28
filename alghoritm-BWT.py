str = input("write some string: ")

ris = ""
strBWT = str + "$"
strList = []
strLenght = len(str)

"""
ciao$
iao$c
ao$ci
o$cia
$ciao
"""

print(strBWT)
for i in range(strLenght):
    rmFrstElm = strBWT[i + 1:]
    strElms = str[:i + 1]
    BWT_elms = rmFrstElm  + strElms
    strList.append(BWT_elms)
print(strList)