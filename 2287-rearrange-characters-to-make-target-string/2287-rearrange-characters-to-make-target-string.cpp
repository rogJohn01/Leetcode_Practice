class Solution {
public:
    int rearrangeCharacters(string s, string target) {
     
        unordered_map<char ,int> scntr ; 
        for(auto e:s){
            scntr[e] ++ ; } 

        unordered_map<char , int> tcntr ; 
        for(auto e:target){
            tcntr[e] ++ ; } 

        int minv = INT_MAX ; 
        for(auto o:tcntr ) { 
            int tmp = scntr[o.first] / o.second  ; 
            if ( tmp < minv)  minv = tmp ;  
        } 
        return minv ; 


    }
};