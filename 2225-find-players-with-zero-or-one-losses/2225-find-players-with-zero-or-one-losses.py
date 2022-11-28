class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        

        dic = defaultdict(int)
        nums = set() 
        for a, b in matches: 
            dic[b] += 1 
            nums.add(a) 
            nums.add(b)
        print(dic) 

        left = [] 
        right = [] 
        for i in nums: 

            if dic[i] ==1: 
                right.append( i)
            elif dic[i] ==0: 
                left.append(i)
        
        left.sort() 
        right.sort() 
        ans = [] 
        ans.append(left)
        ans.append(right) 

        return ans 