class Solution {
    public int findMaxLength(int[] nums) {
        
        
        Map<Integer, Integer> map = new  HashMap<>();
        map.put(0,-1);
        int maxlen =0 , cnt =0 ;
        for (int i =0 ; i <nums.length ; i++){
            cnt += (nums[i] ==1 ? 1: -1);
            
            if (map.containsKey(cnt)){
                maxlen = Math.max( maxlen , i-map.get(cnt));
            } else {
                map.put(cnt ,i);
            }
        }
        
        return maxlen; 
        
        
    }
}