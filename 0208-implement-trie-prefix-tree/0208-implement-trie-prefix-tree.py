

class Tnode:
    def __init__(self):
        self.children = {} 
        self.isWord = False 




class Trie:

    def __init__(self):
        self.root = Tnode() 

    def insert(self, word: str) -> None:
        node  = self.root 
        for w in word:
            if w not in node.children:
                node.children[w] = Tnode()
            node = node.children[w]
        node.isWord = True 
    


    def search(self, word: str) -> bool:
        node = self.root 
        for w in word: 
            if w not in node.children: 
                return False 
            node = node.children[w]
        return node.isWord 


    def startsWith(self, prefix: str) -> bool:
        node = self.root 
        for w in prefix: 
            if w not in node.children:
                return False 
            node = node.children[w]
        return True 



