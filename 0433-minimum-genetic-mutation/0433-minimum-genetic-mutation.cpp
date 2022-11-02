class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
        
        queue<string> q;
        unordered_set<string> seen;
        q.push(start);
        seen.insert(start);
        
        int mut = 0;
        while (!q.empty()) {
            int nodesInQueue = q.size();
            
            for (int j = 0; j < nodesInQueue; j++) {
                string node = q.front();
                q.pop();

                if (node == end) {
                    return mut;
                }
                
                for (char c: "ACGT") {
                    for (int i = 0; i < node.size(); i++) {
                        string next = node;
                        next[i] = c;
                        if (!seen.count(next) && find(bank.begin(), bank.end(), next) != bank.end()) {
                            q.push(next);
                            seen.insert(next);
                        }
                    }
                }
            }
            
            mut++;
        }
        
        return -1;
    }
};