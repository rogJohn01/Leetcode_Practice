class Solution {
public:
    vector<int> numsSameConsecDiff(int n, int k) {
        
    
    vector<int> ans;
    for( auto v=1; v<=9 ; v++)
        dfs(v , n-1 , k ,ans) ; 
    return ans; 
} 

void dfs(int v , int n , int k , vector<int> &ans){
    if( n==0)
        ans.push_back(v); 
    else { 
        int dt = v %10; 
        if ( dt +k <=9)
            dfs( v*10+dt+k , n-1,k,ans);
        if( k != 0 && dt >= k) 
            dfs( v*10+dt-k , n-1 , k ,ans); 
    }
}


};