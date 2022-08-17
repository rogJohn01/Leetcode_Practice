class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        
        vector<string> morse ={".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.." } ; 
        unordered_set<string> box ; 
        for(auto word:words){
            string code ;
            for(auto w:word){
                code += morse[w-'a'] ;}
            box.insert(code) ; 
            }
        return box.size() ; 
        }
        
    
};