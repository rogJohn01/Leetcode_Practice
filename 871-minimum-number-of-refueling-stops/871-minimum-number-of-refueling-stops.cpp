class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        

        int ln = stations.size() ; 
        priority_queue<int> pq; 
        int cur = startFuel ; 
        int i = 0 , ans = 0 ; 
        while(cur < target){
            while( i < ln && cur >= stations[i][0]){
                pq.push(stations[i][1] ) ; 
                i ++ ; 
            }
            if(pq.empty()) return -1; 
            cur += pq.top(); 
            pq.pop() ;
            ans ++ ;
        }
        return ans ; 


        
        
    }
};