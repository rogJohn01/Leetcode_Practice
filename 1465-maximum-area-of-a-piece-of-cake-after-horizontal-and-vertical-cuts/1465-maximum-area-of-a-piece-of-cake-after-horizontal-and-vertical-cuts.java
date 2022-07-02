class Solution {
    public int maxArea(int h, int w, int[] hcut, int[] vcut) {
        
        


        Arrays.sort(hcut) ;
        Arrays.sort(vcut) ; 
        int maxh = Math.max( hcut[0] , h- hcut[hcut.length-1] ) ;
        int maxv = Math.max( vcut[0] , w - vcut[vcut.length-1] ) ; 

        for( int i=1; i < hcut.length ; i++)
            maxh = Math.max( maxh, hcut[i] -hcut[i-1] ) ; 
        for(int j=1 ; j < vcut.length ; j++)
            maxv = Math.max( maxv , vcut[j] - vcut[j-1] ) ; 

        return (int)((long)maxh * maxv % 1000000007); 
        
        
    }
}