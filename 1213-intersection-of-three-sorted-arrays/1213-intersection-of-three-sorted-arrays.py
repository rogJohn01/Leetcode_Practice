class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        ret = []
        arrsum = arr1+arr2+arr3
        arrsum.sort()
        for  v , c in  Counter(arrsum).items():

            if c >=3: 
                ret.append(v)
        return ret 