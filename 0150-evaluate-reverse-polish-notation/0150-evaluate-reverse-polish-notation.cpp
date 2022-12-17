class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        
        stack<long long> st ; 
        for(auto& t:tokens){
            if( t=="+" || t=="-" || t== "*" || t =="/"){
                long long a = st.top() ; st.pop() ; 
                long long  b = st.top() ; st.pop() ; 
                if(t=="+") st.push(b+a) ;
                if(t=="-") st.push(b-a) ; 
                if(t=="*") st.push(b*a) ; 
                if(t=="/") st.push(b/a) ;
            }else {
                st.push(stol(t));
            }
        }
        return st.top() ; 


    }
};