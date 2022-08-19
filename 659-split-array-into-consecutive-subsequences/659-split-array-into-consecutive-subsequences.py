class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        

        left = Counter(nums)
        right = defaultdict(int)

        for n in nums: 
            if not left[n]: continue 
            left[n] -=1 
            if right[n-1] > 0: 
                right[n-1] -=1 
                right[n] +=1 
            elif left[n+1] and left[n+2]: 
                left[n+1] -=1 
                left[n+2] -=1 
                right[n+2] +=1 
            else: 
                return False 
        return True 
