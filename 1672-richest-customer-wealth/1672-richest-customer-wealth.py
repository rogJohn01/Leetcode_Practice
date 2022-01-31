class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        allmaxv= 0 
        for acc in accounts:
            allmaxv = max( sum(acc) , allmaxv)
        return allmaxv
    
        