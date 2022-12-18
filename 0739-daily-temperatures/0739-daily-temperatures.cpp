class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        
        int tl = temperatures.size() ; 
        int diff ;  
        vector<int> ans(tl,0) ; 
        stack<int> st ; 
        for(int i=0 ; i<tl ; i++){

            while( !st.empty() && temperatures[st.top()] < temperatures[i]){
                diff = i -  st.top() ; 
                ans[st.top()] = diff ; 
                st.pop() ; 
            }
            st.push(i) ; 
        }

        return ans ; 
    }
};