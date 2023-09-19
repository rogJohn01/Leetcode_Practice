class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        
        dp_left = [0]*len(height)
        dp_right = [0]*len(height)


        left_max = 0 
        right_max = 0 
        for h in range(len(height)):

            left_max = max(left_max, height[h])
            dp_left[h] = left_max

        for h in range(len(height)-1 , -1 ,-1):

            right_max = max(right_max , height[h])
            dp_right[h] = right_max

        ans = 0 
        for h in range(len(height)):

            min_wall = min(dp_right[h] , dp_left[h])
            ans +=  max(0 , min_wall - height[h] )
            
        return ans 
    
    
    
    