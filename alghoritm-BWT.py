str = input("write some string: ")
print(f"your string: {str}")

strBWT = str + "$"
strLenght = len(str)

#print(strBWT)

"""
for char in str:
    print(char)
"""

for char in strBWT :
    print(char[::-1])