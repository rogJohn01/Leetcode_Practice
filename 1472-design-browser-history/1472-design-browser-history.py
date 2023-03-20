
class ddlNode:   # think node as a struct in golang ! 
    def __init__(self , url):
        self.date = url 
        self.prev = None 
        self.next = None 

    

class BrowserHistory:
    
    def __init__(self, homepage: str):
        self.ll_head = ddlNode(homepage)
        self.current = self.ll_head 

    def visit(self, url: str) -> None:
        node = ddlNode(url)
        self.current.next  = node  # below 3lines are about swapping | the structure similar to trie! 
        node.prev = self.current 
        self.current = node  

    def back(self, steps: int) -> str:
        
        while steps and self.current.prev: 
            self.current = self.current.prev 
            steps -=1 
        return self.current.date


    def forward(self, steps: int) -> str:

        while steps and self.current.next: 
            self.current = self.current.next
            steps -=1 
        return self.current.date 


        