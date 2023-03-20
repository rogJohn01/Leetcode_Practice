class Tnode:
    def __init__(self):
        self.children = {} 
        self.isWord = False 


class WordDictionary:
    def __init__(self):
        self.root = Tnode()

    def addWord(self ,word): 
        node = self.root 
        for w in word: 
            if w not in node.children: 
                node.children[w] = Tnode() 
            node = node.children[w]
        node.isWord= True 
    
    def search(self, word):

        def dfs(node , ix):

            if ix == len(word):
                return node.isWord 

            if word[ix] == ".":
                for child in node.children:
                    if dfs(node.children[child] , ix+1) :
                        return True 
            
            if word[ix] in node.children: 
                return dfs(node.children[word[ix]] , ix+1)

            return False 
        
        return dfs(self.root , 0 )
