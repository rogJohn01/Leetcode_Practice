class Solution {
public:
    bool canPlaceFlowers(vector<int>& fl, int n) {
        
          int cnt =0;
      for(int i =0; i<fl.size(); i++){

        if (fl[i]==0 ){

          bool el = (i==0) || (fl[i-1] == 0);
          bool er = (i == fl.size()-1) || (fl[i+1] ==0);

          if( el && er ){

            cnt ++; 
            fl[i] =1;
            if(cnt >=n) return cnt;
          }  
        }
        
      }
      return cnt >=n;   
        
        
        
        
    }
};