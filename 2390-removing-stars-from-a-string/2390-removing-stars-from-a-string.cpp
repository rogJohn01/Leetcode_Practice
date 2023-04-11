class Solution {
public:
    string removeStars(string s) {
        
        vector<char> st; 
        for(auto e:s){
            if(e !='*'){
                st.push_back(e) ;
            }else {
                st.pop_back(); 
            }
            
        }
        string ans ="";
        for(int i=0 ; i < st.size(); i++){
            ans += st[i] ; 
        }
        return ans ; 
        
    }
};