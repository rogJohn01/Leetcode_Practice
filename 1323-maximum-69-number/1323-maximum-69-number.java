class Solution {
    public int maximum69Number (int num) {
        
        String str = "" + num;
        return Integer.parseInt(str.replaceFirst("6","9"));
    }
}