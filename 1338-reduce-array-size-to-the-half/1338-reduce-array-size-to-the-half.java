class Solution {
    public int minSetSize(int[] arr) {
        

        int al = arr.length ; 
        HashMap<Integer,Integer> cntr = new HashMap<>(); 
        for(int a:arr) cntr.put(a, cntr.getOrDefault(a,0)+1 ) ; 

        int[] count= new int[al+1] ; 
        for(int freq: cntr.values()) count[freq]++ ; 

        int ans =0 , tmp  = 0 , freq = al ; 
        while( tmp < al/2){
            ans ++ ; 
            while(count[freq] ==0) freq -- ; 
            tmp += freq ; 
            count[freq] -- ; 
        }
        return ans ; 
    }
}