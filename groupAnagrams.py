from collections import defaultdict
def groupAnagrams(strs):
    anagrams=defaultdict(list)
    for s in strs:
        sorted_str=''.join(sorted(s))
        anagrams[sorted_str].append(s)
    return list(anagrams.values())
strs=["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))