class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = True  # Mark end of word

    def search(self, word: str) -> bool:
        def search_in_node(word, node) -> bool:
            for i, char in enumerate(word):
                if char == '.':
                    return any(search_in_node(word[i + 1:], node[child]) for child in node if child != '$')
                if char not in node:
                    return False
                node = node[char]
            return '$' in node

        return search_in_node(word, self.trie)
word_dict = WordDictionary()
word_dict.addWord("apple")
word_dict.addWord("banana")

print(word_dict.search("apple"))  # Output: True
print(word_dict.search("app.e"))  # Output: True (matches "apple")
print(word_dict.search("b.nana")) # Output: True (matches "banana")
print(word_dict.search("app"))    # Output: False
