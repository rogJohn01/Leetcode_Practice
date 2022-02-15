class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
            
            def converter(nums):
                nl = [] 
                for n in nums:
                    if n==1:
                        nl.append(0)
                    else:
                        nl.append(1)
                return nl 

            ml = [] 
            for im in image:
                ml.append( converter( im[::-1] ))
            return ml 
