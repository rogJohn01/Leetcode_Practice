class Solution:
   
        
        
    def reverse_letters(self, s , left, right):
        
        
        while left < right:
            
            s[left], s[right] = s[right] , s[left]
            left +=1
            right -=1
        
        #return s 
    
    def reverse_words(self, s):
        
        start = 0
        end = 0 
        n = len(s)
        
        while start < n:
            
            while end < n and s[end] !=' ':
                
                end +=1 
            
            self.reverse_letters(s, start , end-1 )
            start = end +1 
            end +=1 
        
                
    def reverseWords(self, s: List[str]) -> None:
            """
            Do not return anything, modify s in-place instead.
            """
            self.reverse_letters(s, 0 , len(s)-1)

            self.reverse_words(s)


