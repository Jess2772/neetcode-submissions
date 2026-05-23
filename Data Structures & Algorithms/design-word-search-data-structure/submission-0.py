class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur.children[c] = cur.children.get(c, TrieNode())
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.endOfWord
            if word[i] == '.':
                for wildcard in node.children:
                    if dfs(i + 1, node.children[wildcard]):
                        return True
                return False
            elif word[i] not in node.children:
                return False
            else:
                return dfs(i + 1, node.children[word[i]])

        return dfs(0, self.root)
        
