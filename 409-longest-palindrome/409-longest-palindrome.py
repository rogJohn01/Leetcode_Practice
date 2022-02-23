class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        
            cnt = 0 
            once = False 
            
            if len(Counter(s)) ==1:
                return list(Counter(s).values())[-1]
    
            for k , v in Counter(s).items():
                if v % 2 ==0: 
                    cnt +=v 
                if v ==1 and not once:
                    cnt +=1
                    once = True 
                elif v >2 and v % 2 !=0: 
                    cnt += v-1
                    if not once:
                        cnt +=1 
                        once = True 
            return cnt 