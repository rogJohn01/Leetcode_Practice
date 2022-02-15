class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        path = [] 
        for i in range(1, len(tiles)+1):
    
            path.extend(list(permutations(tiles , i)))
        return len(set(path))