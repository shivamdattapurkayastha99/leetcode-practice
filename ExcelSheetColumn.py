def convertToTitle(columnNumber):
    result=[]
    while columnNumber>0:
        columnNumber-=1
        result.append(chr(columnNumber%26+ord('A')))
        columnNumber//=26
    result.reverse()
    return ''.join(result)
print(convertToTitle(1))