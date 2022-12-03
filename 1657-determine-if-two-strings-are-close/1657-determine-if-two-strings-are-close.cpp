class Solution {
public:
    bool closeStrings(string word1, string word2) {
        
       vector<int> cntr1(26,0) , cntr2(26,0) ;
       set<char> set1 , set2 ; 
        for(char e: word1){
            cntr1[e-'a']++;
            set1.insert(e) ; 
        }
        for(char e: word2){
            cntr2[e-'a']++ ; 
            set2.insert(e); 
        }
        
        sort(begin(cntr1) , end(cntr1)); 
        sort(begin(cntr2) , end(cntr2)); 
        
        return cntr1 == cntr2 && set1 == set2 ; 
        
    }
};