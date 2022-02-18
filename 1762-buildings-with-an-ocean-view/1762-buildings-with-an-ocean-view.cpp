class Solution {
public:
    vector<int> findBuildings(vector<int>& heights) {
        
        int n = heights.size();
        vector<int> ans;
        stack<int> st; 
        
        for(int i = n-1 ; i >=0; --i){
            
            while( !st.empty() && heights[st.top()] < heights[i]){
                st.pop();
            }
            
            if(st.size() ==0) {
                ans.push_back(i);
            }
            
            st.push(i);

        }       
        reverse(ans.begin(), ans.end());
        return ans ; 
        
        
        
        
    }
};