
class Solution {
public:


 vector<vector<string>> partition(string s) {
        
     vector<vector<string>> ans ; 
     vector<string> box ; 
     dfs(0,s , box , ans) ; 
     return ans; 
 }

void dfs(int ix , string& s , vector<string>& box , vector<vector<string>>& ans) {

    if(ix == s.size()){
        ans.push_back(box);
        return ; 
    }
    for(int i= ix ; i < s.size() ; i++){
        if(isPal(s,ix,i)){
            box.push_back(s.substr(ix, i-ix+1)) ;
            dfs(i+1 , s, box , ans);
            box.pop_back() ;
        }
    }
}

bool isPal(const string& s , int l , int r){
    while(l <= r){
        if(s[l++] != s[r--])
            return false ; 
    } return true ; 
}

}; 

