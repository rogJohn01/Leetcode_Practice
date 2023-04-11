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
        for(auto e:st){
            ans += e ; 
        }
        return ans ; 
        
    }
};