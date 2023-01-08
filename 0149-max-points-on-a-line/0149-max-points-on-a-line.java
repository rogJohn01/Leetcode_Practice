class Solution {
    public int maxPoints(int[][] points) {
        
        
        int pl = points.length ; 
        if(pl==1 ){
            return 1; 
        }
        int ans =2; 
        for(int i=0; i< pl;i++){
            Map<Double, Integer> cnt = new HashMap<>(); 
            for(int j=0; j< pl ; j++){
                if(j != i){
                    cnt.merge(Math.atan2(points[j][1] - points[i][1] , points[j][0] - points[i][0]) , 1 , Integer::sum) ; 
                }
            }
            ans = Math.max(ans, Collections.max(cnt.values())+1) ; 
        }
        return ans ; 
    }
}