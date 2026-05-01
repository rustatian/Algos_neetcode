class TrieNode:
    def __init__(self) -> None:
        self.childrends = {}
        self.eow = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.childrends:
                node.childrends[ch] = TrieNode()
            node = node.childrends[ch]
        node.eow = True
        return None


    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.childrends:
                return False
            node = node.childrends[ch]
        return node.eow
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.childrends:
                return False
            node = node.childrends[ch]
        return True