class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word: str) -> bool:
        def search_in_node(node, word):
            for i, char in enumerate(word):
                if char not in node.children:
                    if char == ".":
                        for child in node.children:
                            if search_in_node(node.children[child], word[i + 1:]):
                                return True
                    return False
                else:
                    node = node.children[char]
            return node.is_end
        return search_in_node(self.root, word)
        
