class Solution:
    def minimumCardPickup(self, nums: List[int]) -> int:
        q = defaultdict(list)
        for i, n in enumerate(nums): 
            q[n].append(i)
        dup = False 
        ans = float('inf') 
        minv =  float('inf') 
        for k ,v in q.items():
            if len(v) >=2:
                dup = True 
                minv = float('inf')
                for i in range(1,len(v)):
                    tv = v[i] - v[i-1]
                    if tv < minv:
                        minv = tv 
            ans = min( ans , minv) 


        return ans+1 if dup else -1 