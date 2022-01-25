class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        
        
        if len(arr) <3:
            return False 
        maxIndex = arr.index(max(arr))
        if maxIndex == len(arr)-1 or maxIndex ==0:
            return False 
        for i in range(len(arr)):
            
            if i>0 and arr[i] == arr[i-1]:
                return False 
            
            if i !=0 and i<maxIndex and arr[i] < arr[i-1]:
                return False 
            if i> maxIndex and arr[i] > arr[i-1]:
                return False 
        return True 
        
        