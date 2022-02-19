class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        
        
        
            n = len(s)
            from collections import deque
            nums = [e for e in range(n+1)]
            deque = deque(nums)


            ans = [] 
            for e in s:

                if e=='I':
                    ans.append( deque.popleft())
                elif e=='D':
                    ans.append(deque.pop())
            if len(nums) !=0:
                ans.append(deque[-1])
            return ans
