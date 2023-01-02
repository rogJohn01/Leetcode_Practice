class Solution {
public:
    bool detectCapitalUse(string word) {
        
        
        for(int i=2; i <  word.length(); i++){
            
             if( isupper(word[0]) >0 && isupper(word[1]) >0    && isupper(word[i]) ==0 )
                 return false ; 

            else if( isupper(word[0]) > 0 && isupper(word[1])==0 && isupper(word[i]) > 1 )
                return false ; 
        
         else if( isupper(word[0])==0 && isupper(word[1]) ==0 && isupper(word[i]) > 0  )
                return false;         
       
        }
        if(word.length() >=2 && isupper(word[0]) == 0 && isupper(word[1]) >0 ) return false; 


        return true; 
        
        
        
    }
};