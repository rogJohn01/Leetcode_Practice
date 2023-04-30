class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        R = len(mat)
        C = len(mat[0])
        mp = defaultdict(list)
        for r in range(R):
            for c in range(C):
                mp[mat[r][c]] = [r,c]
                
        #print(mp)
        rows = [0]*(R+1)
        cols = [0]*(C+1)
        for i in range(len(arr)):
            a = arr[i]
            r, c = mp[a]
            rows[r] +=1 
            cols[c] +=1 
            if rows[r] == C or cols[c] ==R: 
                return i 
        
        #print("rows", rows)
        #print("cols", cols)
        return 0 
            