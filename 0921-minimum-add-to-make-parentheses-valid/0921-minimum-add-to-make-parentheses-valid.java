class Solution {
    public int minAddToMakeValid(String s) {
        
        
        
        int bal = 0 , ans = 0 ; 
        for(char e:s.toCharArray()){
            
            if(e=='(') bal ++ ; 
            
            if(e==')'){
                if(bal > 0) bal -- ; 
                else{
                    ans ++ ; 
                }
            }
        }
        ans += bal ; 
        return ans ; 
        
        
    }
}