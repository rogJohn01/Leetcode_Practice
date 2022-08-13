class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        
        final Map<String, Integer> cntr = new HashMap<>() ; 
        for(final String w:words)
            cntr.put(w , cntr.getOrDefault(w, 0)+1 ) ; 
        
        final List<Integer> ixs = new ArrayList<>() ; 
        final int n = s.length() , num = words.length , len = words[0].length() ; 
        for(int i=0 ; i < n -num*len +1 ; i++){
            final Map<String,Integer> seen = new HashMap<>() ; 
            int j = 0; 
            while(j < num) { 
                final String word = s.substring(i+j*len, i+(j+1)*len); 
                if(cntr.containsKey(word)) { 
                    seen.put( word , seen.getOrDefault(word,0) +1 ); 
                    if(seen.get(word) > cntr.getOrDefault(word,0)) {
                        break ; 
                    }
                } else {
                    break ; 
                }
                j++ ; 
            }
            if(j== num){
                ixs.add(i) ; 
            }
        }
        return ixs ; 

        
        
    }
}