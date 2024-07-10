class StreamChecker:

    def __init__(self, words):
        self.trie = {}
        self.stream = []
        for word in words:
            node = self.trie
            for char in word[::-1]:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = True

    def query(self, letter):
        self.stream.append(letter)
        node = self.trie
        for char in reversed(self.stream):
            if char in node:
                node = node[char]
                if '#' in node:
                    return True
            else:
                break
        return False
words = ["cd", "f", "kl"]
streamChecker = StreamChecker(words)

print(streamChecker.query('a'))