from collections import Counter
def frequencySort(s):
    count=Counter(s)
    sorted_chars=sorted(count.items(),key=lambda item:(-item[1],item[0]))
    result=''.join(char*freq for char,freq in sorted_chars)
    return result
s="tree"
print(frequencySort(s))