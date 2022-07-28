class Solution {
    public boolean isAnagram(String s, String t) {
        

        if(s.length() != t.length()) return false ; 

        int[] cntr = new int[26] ; 
        for(int i=0; i< s.length(); i++){
            cntr[s.charAt(i)-'a'] ++; 
            cntr[t.charAt(i)-'a'] --;
        }
        for(int c:cntr){
            if(c!=0){
                return false ; 
            }}
        return true ; 


        
    }
}