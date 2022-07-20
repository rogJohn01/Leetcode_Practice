class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        dic = defaultdict(list)
        for i,e in enumerate(s): 
            dic[e].append(i) 

        ans = 0 
        for w in words: 

            ss = False ; cur = -1 ; i = 0 
            while True: 
                if w[i] in dic:
                    idxs = dic[w[i]]
                    have = False 
                    for ix in idxs: 
                        if ix > cur:
                            cur = ix
                            have = True 
                            break 
                    if not have: 
                        break 

                else: 
                    break 
                i +=1 
                if i >= len(w):
                    ss = True 
                    break 

            if ss: ans +=1
                
        return ans 
