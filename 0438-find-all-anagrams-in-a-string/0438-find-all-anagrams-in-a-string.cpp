class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
    
        
    int  pl = p.size() ; 
    vector<int> rec1(26 , 0 ) ; 
    vector<int> rec2(26 , 0 ) ; 
    vector<int> ans ;  
    for(auto e:p ){
        rec1[(int)e -'a'] ++ ;        
    } 

    for(int i=0 ; i < s.size() ; i++){

        rec2[(int)s[i]-'a'] ++ ; 

        if(i >= pl){
            rec2[(int)s[i-pl]-'a' ]-- ; 
        }
        if(rec1 == rec2){
            ans.push_back(i-pl+1) ; 
        }
    }
    

    return ans ; 


    }
};