class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        al = [] 
        for n1 in nums1:
            
            mode = False 
            mode2 = True 
            for n2 in nums2:
                
                if n1 == n2:  
                    mode =True 
                    
                if mode and n1 < n2:
                    al.append(n2)
                    mode2 = False 
                    break 
            if mode and mode2:
                al.append(-1)
            
        return al 