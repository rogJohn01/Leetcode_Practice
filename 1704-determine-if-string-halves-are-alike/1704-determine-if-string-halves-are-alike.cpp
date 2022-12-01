class Solution {
public:
    bool halvesAreAlike(string s) {

        int l = s.size() ; 
        int hl = l/2 ; 


        string set = "aeiouAEIOU";

        int left = 0 , right = 0 ; 
        for(int i=0; i <=l ; i++){
            if( i <hl && set.find(s[i]) != string::npos) { 
                left++ ; 
            }else if( i>=hl && set.find(s[i]) != string::npos ){
                right++; 
            }
        }
        return left ==right ; 
    }
};