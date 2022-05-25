class Solution {
public:
    vector<string> removeAnagrams(vector<string>& words) {
        
   
    for(int i=1 ; i < words.size() ; i++) { 
        string x = words[i-1];
        sort( x.begin() , x.end() ); 
        string y = words[i]; 
        sort(y.begin()  , y.end() ) ; 
        if( x==y){ 
            words.erase( words.begin()+ i) ; 
            i --;  }
    }
    return words ; 



        
        
        
    }
};