class Solution {
public:
    int maximum69Number (int num) {
        
        int x = num; 
        int six = -1 ; 
        int digit = 0; 

        while (x >0){
            if(x % 10 ==6){
                six = digit; 
            }
            x /=10 ; 
            digit++; 
        }

        return six == -1 ? num : num + 3*(int)pow(10, six) ; 
    }
};