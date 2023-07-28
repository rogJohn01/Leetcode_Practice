class Solution {
    public String minRemoveToMakeValid(String s) {
        
        
        
        Stack<Integer> st = new Stack<Integer>() ; 
        
        int bal = 0 ; 
        for(int ix = 0 ; ix < s.length() ; ix++){
            
            char e = s.charAt(ix) ;
            if( e =='('){
                bal ++ ; 
                st.add( ix) ;
            }else if( e== ')' ) {
                if( bal > 0 ){
                    st.pop() ; 
                    bal -- ; 
                }else {
                    st.add(ix ) ; 
                }
                
            }
        }
        
       String ans ="" ;
       Set<Integer> set = new HashSet<Integer>(st) ; 
       for(int i= 0 ; i < s.length() ; i++){
            
           if( ! set.contains(i)){
                ans += s.charAt(i);     

           }
           
       }
        
        return ans ; 
        
        
    }
}