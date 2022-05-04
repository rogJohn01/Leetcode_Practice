class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
            count = 0
            dic = defaultdict(int)
            for a in nums:
                
                b = k - a
                if dic[b]:
                    count +=1 
                    dic[b] -=1 
                
                
                else:
                   dic[a] +=1 
            
            return count 