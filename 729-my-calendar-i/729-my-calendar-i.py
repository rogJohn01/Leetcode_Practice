class MyCalendar:

    def __init__(self):
        self.record = [] 

    def book(self, ns: int, ne: int) -> bool:
        
        for cs, ce in self.record: 
            
            if (ns < cs and cs < ne ) or  ( ce < ne and ce > ns ) or (cs <=ns and ne <=ce): 
                return False 
        
        self.record.append([ns,ne])
        return True 


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)