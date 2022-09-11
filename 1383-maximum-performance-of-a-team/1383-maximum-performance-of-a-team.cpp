class Solution {
public:
    int maxPerformance(int n, vector<int>& speed, vector<int>& efficiency, int k) {
        
        
    vector<pair<int,int>> engs(n); 
    for(int i=0; i< n; i++) {
        engs[i] = { efficiency[i], speed[i]};
    }
    sort( rbegin(engs) , rend(engs)) ; 
    long ssum = 0 , ans = 0 ; 
    priority_queue <int, vector<int> , greater<int>> heap ; 
    for(auto& [e,s]: engs) { 
        heap.emplace(s); 
        ssum +=s ; 
        if ( heap.size() >k) { 
            ssum -= heap.top() ; 
            heap.pop() ; 
        }
        ans = max(ans ,ssum*e); 
    }
    return ans %(int)(1e9+7); 


    }
};