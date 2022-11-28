class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        

        int[] win = new int[100001];
        int[] loss = new int[100001]; 

        for(int[] mc: matches){
            win[mc[0]]++; 
            loss[mc[1]]++;
        }

        List<List<Integer>> ans = new ArrayList<>(); 
        List<Integer> left = new ArrayList<>(); 
        List<Integer> right = new ArrayList<>();

        for(int i =0; i < win.length ; i++){
            if( win[i] > 0 && loss[i] == 0 ){
                left.add(i); 
            }
            if(loss[i] ==1){
                right.add(i);
            }
        }
        ans.add(left); 
        ans.add(right); 

        return ans; 


    }
}