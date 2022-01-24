# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> int:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        #if n==1:
         #   return 1 
        left , right = 0, n 
        while left <= right: # using = is the point!! 
            
            mid = (left+right) //2 
            
            if isBadVersion(mid) ==False:
                left = mid+1
                
            if isBadVersion(mid) ==True:
                if isBadVersion(mid-1) ==False:
                    return mid 
                right = mid -1 
        return mid 