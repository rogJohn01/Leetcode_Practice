class Solution {
public:
    bool wordPattern(string pattern, string s) {
        
        map<char , int> pat2 ; 
        map<string, int> word2 ; 
        istringstream in(s); 

        int i =0 , pl = pattern.size() ; 
        for(string word; in >> word ; i++){
            if( i==pl || pat2[pattern[i]] != word2[word])
                return false ; 
            pat2[pattern[i]] = word2[word] = i+1 ; 
        }
        return i ==pl ; 
    }
};