class Solution {
public:
    string addBinary(string a, string b) {
        
    int asize = a.size() -1 ; 
    int bsize = b.size() -1 ; 

    string ans ; 
    int carry = 0 ; 
    while(asize >=0 || bsize >=0 || carry){
        if(asize>=0){
            carry += a[asize] - '0' ; 
            asize -- ; 
        }
        if(bsize>=0){
            carry += b[bsize] - '0' ; 
            bsize -- ; 
        }
        ans += (carry%2 + '0') ; 
        carry = carry/2 ; 
    }
    reverse(ans.begin() , ans.end()); 
    return ans ; 


    }
};