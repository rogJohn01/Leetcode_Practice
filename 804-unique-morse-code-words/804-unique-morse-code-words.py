class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        cv = {} 
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for i in range(97,123):
            cv[chr(i)] = morse[i-97]
        
        box = set() 
        for word in words: 
            t = ''
            for w in word: 
                t += cv[w]
            box.add(t)
        
        return len(box)