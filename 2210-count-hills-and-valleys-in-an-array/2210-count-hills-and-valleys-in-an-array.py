class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
            cnt = 0 
            ln = len(nums)
            for i in range(1,  ln):

                if nums[i] == nums[i-1]: 
                    continue 

                lp = i-1 ; rp = i+1 
                while  lp>=0 and nums[lp] ==nums[i]:
                    lp -=1 
                if lp < 0:
                        continue 
                while rp < ln  and nums[i] == nums[rp]:
                    rp +=1 
                if rp >= ln:
                    continue

                if nums[lp] < nums[i] and nums[i] > nums[rp]:
                    cnt +=1 
                elif nums[lp] > nums[i] and nums[i] < nums[rp]:
                    cnt +=1 

            return cnt 

