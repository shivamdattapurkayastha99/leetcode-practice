from typing import List

class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        self.generate_combinations(characters, combinationLength, 0, [])
        self.index = 0
    
    def generate_combinations(self, characters, length, start, current):
        if len(current) == length:
            self.combinations.append("".join(current))
            return
        
        for i in range(start, len(characters)):
            current.append(characters[i])
            self.generate_combinations(characters, length, i + 1, current)
            current.pop()
    
    def next(self) -> str:
        combination = self.combinations[self.index]
        self.index += 1
        return combination
    
    def hasNext(self) -> bool:
        return self.index < len(self.combinations)

iterator = CombinationIterator("abc", 2)
print(iterator.next())   
print(iterator.hasNext())  
print(iterator.next())   
print(iterator.hasNext())  
print(iterator.next())   
print(iterator.hasNext())  
