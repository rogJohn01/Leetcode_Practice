class Solution {
public:
    string frequencySort(string s) {
        
        unordered_map<char, int > freq ; 
        priority_queue<pair<int,char>> mxheap ; 
        for(char e:s){
            freq[e]++;
        }
        for(auto it: freq){
            mxheap.push({ it.second , it.first }); 
        }
        string ans = "";
        while(! mxheap.empty()){
            ans += string(mxheap.top().first , mxheap.top().second ) ;
            mxheap.pop();
        }
        return ans; 
    
    }
};