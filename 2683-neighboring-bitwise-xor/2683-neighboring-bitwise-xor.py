class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        N = len(derived)
        ori = [0]*(N+1)
        
        for i in range(N):
            
            if i == N-1: 
                if derived[i] != ori[0]^ori[i]:
                    return False 
            
            if derived[i] ==1: 
                ori[i+1] = 1^ori[i]
            else: 
                ori[i+1] = ori[i]
                
        return True 