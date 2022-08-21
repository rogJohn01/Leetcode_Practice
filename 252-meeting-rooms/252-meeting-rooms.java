class Solution {
    public boolean canAttendMeetings(int[][] inter) {
        Arrays.sort(inter, (a,b)-> Integer.compare(a[0],b[0]));
        
        for(int i=1; i < inter.length ; i++){
            if(inter[i-1][1] > inter[i][0] )
                return false ; 
        }
        return true ; 
    }
}
