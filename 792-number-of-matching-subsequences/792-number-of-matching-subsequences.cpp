class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        
        vector<vector<int>> alp (26) ; 
        for(int i =0 ; i< s.size(); i++)
            alp[s[i]-'a'].push_back(i) ; 

        int ans = 0 ; 
        for(const auto& w: words){
            int x =-1; 
            bool have = true ; 

            for(char e:w){
                auto it = upper_bound( alp[e-'a'].begin() , alp[e-'a'].end() , x) ;
                if( it == alp[e-'a'].end())  have = false ; 
                else x = *it ; 
            }
            if(have) ans++ ; 
        }
        return ans ; 


        
        
        
    }
};