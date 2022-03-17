class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        
          for i in range(start,start+(2*n),2):
                
                if i ==start:
                    x = i
                else:
                    x ^=i
          return x 