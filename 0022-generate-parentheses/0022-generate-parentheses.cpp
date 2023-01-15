class Solution {
public:
    
    vector<string> ans; 
    
    void backtrack(int open,int close , int x, string s ){
        
        if(s.length() ==2*x)
            ans.push_back(s) ; 
        if(open < x){
            backtrack(open+1,close,x,s+"(");
        } 
        if(x>=open && open > close){
            backtrack(open,close+1,x , s+")") ; 
        }
        
        
    }
    
    vector<string> generateParenthesis(int n) {
        backtrack(0,0,n,"");
        return ans; 
        
        
    }
};