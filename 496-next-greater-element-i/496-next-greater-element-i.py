class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        al = [] 
        for n1 in nums1:
            
            stack = [] 
            for n2 in nums2:
                
                if n1 ==n2:
                    stack.append(n1)
                
                elif stack and stack[-1] < n2:
                    al.append(n2)
                    stack.pop()
                    break 
            
            if  stack:
                al.append(-1)
        return al 