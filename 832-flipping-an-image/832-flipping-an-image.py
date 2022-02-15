class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
            
            def converter(nums):
                 return [ 1^n for n in nums]
            ml = [] 
            for im in image:
                ml.append( converter( im[::-1] ))
            return ml 
