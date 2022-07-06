class Solution {
    public int numWays(int n, int k) {
        
        if(n==1) return k; 
        if(n==2) return k*k ; 
        
        int tways[] = new int[n+1]; 
        tways[1] = k;
        tways[2] = k*k;
        
        for(int i=3 ; i<=n ; i++){
            tways[i] = (k-1)* (tways[i-1] + tways[i-2]);
        }
        
        return tways[n] ; 
        
    }
}