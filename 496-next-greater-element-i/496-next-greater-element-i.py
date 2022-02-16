class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if not nums2:
            return None 
        
        dic = {}
        ret = [] 
        stack = [] 
        stack.append(nums2[0])
        
        for i in range(1, len(nums2)):
            while stack and stack[-1] < nums2[i]:
                dic[stack[-1]] = nums2[i]
                stack.pop()
            stack.append((nums2[i]))
        
        for ele in stack: 
            
            dic[ele] = -1 
            
        for i in range(len(nums1)):
            ret.append(dic[nums1[i]])
        return ret