class Solution {
public:

void dfs(int node, vector<int> &vis, vector<int> adj[], int &nodes, int &edges){
    vis[node]=1;
    nodes++;
    edges+=adj[node].size();
    for(auto x:adj[node]){
        if(!vis[x]){
            dfs(x,vis,adj,nodes,edges);
        } 
    }
}

    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        if(edges.size()==0) return n;
        int components=0;
        vector<int> vis(n,0);
        vector<int> adj[n];
        for(auto x:edges){
            adj[x[0]].push_back(x[1]);
            adj[x[1]].push_back(x[0]);
        }
        int errors=0;
        for(int i=0;i<n;i++){
            if(!vis[i]){
                components++;
                int nodes=0;
                int edges=0;
                dfs(i,vis,adj,nodes,edges);
                if(edges!=(nodes*(nodes-1))) errors++;
            }
        }
        return components-errors;
    }
};