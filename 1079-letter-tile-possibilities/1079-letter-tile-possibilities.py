class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        global cnt 

        cnt = 0 
        ret = []
        def dfs(path, cntr ,k):
            global cnt 

            if len(path) ==k: 
                ret.append(''.join(path))
                cnt +=1 


            for c in cntr: 

                if cntr[c] >=1:
                    cntr[c] -=1 
                    dfs(path+[c] , cntr ,k)
                    cntr[c] +=1 

        for k in range(1, len(tiles)+1):

            dfs( [] ,Counter(tiles) ,k ,)
        return len(ret)