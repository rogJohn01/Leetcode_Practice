class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        
        
        
        vector<int> arr1(26) ; 
        for(auto e:s1){
            //cout << (int)e -'a' << " " ; 
            arr1[(int)e -'a'] ++ ;  
        }

        vector<int> arr2(26) ; 
        for(int i =0  ;  i < s2.size() ; ++i){
            arr2[(int)s2[i]-'a'] ++ ; 

            if( i >= s1.size() ){
                arr2[(int)s2[i-s1.size()] -'a'] -- ; 
            }

            if(arr1 ==arr2) return true  ; 
        }
        return false  ; 


    }
};