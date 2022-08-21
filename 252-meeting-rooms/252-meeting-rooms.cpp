class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& inter) {
            
        sort(inter.begin() ,inter.end() ) ;  
        for(int i=1; i < inter.size() ; i++){
            if( inter[i][0] < inter[i-1][1]) 
                return false ; 
        }
        return true ; 


    }
};