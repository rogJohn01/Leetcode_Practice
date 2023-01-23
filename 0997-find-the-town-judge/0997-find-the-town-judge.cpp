class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
       
        vector<int> cntr(n+1,0) ;
        for(auto&t :trust){
            cntr[t[0]] -- ; 
            cntr[t[1]] ++ ; 
        } 
        for(int i=1 ; i<=n ; i++){
            if(cntr[i] == n-1) return i ; 
        } return -1 ; 

        //logic ! we are just searching for the town judge. we don't care about the value of follower ; 
    }
};