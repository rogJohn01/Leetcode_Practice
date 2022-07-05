class Solution {
    public int trap(int[] h) {
        
        
        Stack<Integer> st = new Stack<>(); 
        int rain = 0 ; 
        for(int r =0 ; r < h.length ; r++){

            while( !st.isEmpty() && h[st.peek()] < h[r] ){ 
                int btm = st.pop();
                if( st.isEmpty() ) {
                    break ; } 

                int l = st.peek() ; 
                int wid = (r-l -1) ; 

                rain += wid*( Math.min( h[r] , h[l] ) - h[btm]) ;
            }
            st.push(r) ; 
        }
        return rain ; 
    }
}