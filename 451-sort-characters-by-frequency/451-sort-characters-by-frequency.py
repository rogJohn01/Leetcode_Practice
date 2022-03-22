class Solution:
    def frequencySort(self, s: str) -> str:
        
        temp = []
        for v, k in Counter(s).most_common():

                while k:
                    temp.append(v)
                    k -=1
        return ''.join(temp)