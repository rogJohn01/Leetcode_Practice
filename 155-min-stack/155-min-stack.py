class MinStack:

    def __init__(self):
        self.st = [] 
        self.minSt = [] 

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.minSt:
            self.minSt.append(val)
        elif self.minSt[-1] >=val:
            self.minSt.append(val)

        
    def pop(self) -> None:
        k =self.st.pop()
        if k == self.minSt[-1]:
            self.minSt.pop()
    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        if self.minSt:
            return self.minSt[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()