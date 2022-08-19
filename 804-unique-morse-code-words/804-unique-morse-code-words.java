class Solution {
    public int uniqueMorseRepresentations(String[] words) {

        String[] morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."}; 
        HashSet<String> box = new HashSet<>(); 
        for(String w:words){
            StringBuilder t = new StringBuilder(); 
            for(int i =0 ; i < w.length() ; i++){
                t.append( morse[w.charAt(i) - 'a']) ; }
            box.add( t.toString()) ;
        }
        return box.size() ; 
    }
}