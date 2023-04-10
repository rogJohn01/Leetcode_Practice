class Solution {
public:
    bool isValid(string s) {
     
    
    stack<char> st ; 
    unordered_map<char, char> mp = {{')', '('}, {'}', '{'}, {']', '['}};

    for(char e:s){
        if(e=='(' || e=='{' || e=='['){
            st.push(e) ;
        } else {
            if( !st.empty() && (st.top() == mp[e]) ){
                st.pop() ; 
                continue ;
            } else {
                return false;
            }
        }
    } return st.empty() ; 


    }
};