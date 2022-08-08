class Solution {
public:
    int reachableNodes(int n, vector<vector<int>>& edges, vector<int>& restricted) {
        
        vector<bool> visit(n ,false) ; 
        vector<int> graph[n] ; 
        for(int i=0; i < edges.size() ; i++){
            graph[ edges[i][0] ].push_back(edges[i][1]);
            graph[ edges[i][1] ].push_back(edges[i][0]); 
        }
        for(auto r:restricted){
            visit[r] = true ; 
        }
        int ans = 0 ; 
        dfs(0 ,graph , ans , visit) ; 
        return ans ; 
        
    }
        
    void dfs(int v , vector<int> graph[] , int &ans , vector<bool> &visit){ 
        visit[v] = true ; 
        ans ++ ; 
        for(auto nv:graph[v]){
            if( visit[nv] == false){
                dfs(nv , graph , ans , visit) ;
            }
        }
}

        
};