
class TrieNode():
    def __init__(self) -> None:
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.word = True

    def search(self, word: str) -> bool:
        l = len(word)
        
        def dfs(i, node: TrieNode):
            curr = node

            for j in range(i, l):
                if word[j] == ".":
                    for child in curr.children.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if word[j] not in curr.children:
                        return False
                    curr = curr.children[word[j]]
            return curr.word
        return dfs(0, self.root)
                



# Your WordDictionary object will be instantiated and called as such:
word = "apple"
obj = WordDictionary()
obj.addWord(word)
param_2 = obj.search(".pp..")
print(param_2)
