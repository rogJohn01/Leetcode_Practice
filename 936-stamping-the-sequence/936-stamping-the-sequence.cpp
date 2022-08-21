class Solution {
public:
    vector<int> movesToStamp(string stamp, string target) {

        vector<int> ans ; 
        auto totstamp = 0 , tnstamp = -1 ; 
        while(tnstamp) { 
            tnstamp = 0 ; 
            for(int sl = stamp.size() ; sl > 0 ; sl--)
                for(auto i=0 ; i <= stamp.size()-sl ; i++){
                    auto nstamp = string(i,'*')+ stamp.substr(i,sl)+string(stamp.size() -sl-i , '*') ; 
                    auto pos = target.find(nstamp); 
                    while(pos != string::npos){
                        ans.push_back(pos) ; 
                        tnstamp += sl ; 
                        fill(begin(target)+pos, begin(target)+pos+ stamp.size(),'*') ; 
                        pos = target.find(nstamp) ; 
                    }
                }
            totstamp += tnstamp ; 
        }
        reverse(begin(ans) ,end(ans));
        return totstamp == target.size() ? ans : vector<int>(); 
        
        
    }
};