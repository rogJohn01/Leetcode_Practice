class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        stack = [] 
        al = [] 
        for n1 in nums1:
            
            stack.append(n1)
            mode = False 
            mode2 = True 
            for i, n2 in enumerate(nums2):
                
                if stack[-1] == n2:  
                    mode =True 
                    
                if mode and stack[-1] < n2:
                    al.append(n2)
                    mode2 = False 
                    break 
            if mode and mode2:
                al.append(-1)
            
        return al 