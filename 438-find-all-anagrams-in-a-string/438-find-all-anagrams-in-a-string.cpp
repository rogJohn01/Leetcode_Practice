class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        
        

      int sl = s.length();
      int pl = p.length();

      if (s.size() < p.size()) return {};

      vector<int> palpha(26,0);
      vector<int> window(26,0);

      for(int i=0; i <pl ; i++){
        palpha[p[i] -'a'] ++;
        window[s[i]- 'a'] ++;
      }
      vector<int> ret;
      if(palpha == window) ret.push_back(0);

      for(int i=pl ; i <sl ; i++){
        window[s[i-pl] - 'a'] --;
        window[s[i] -'a'] ++;

        if ( palpha == window){
          ret.push_back(i-pl+1);
        }
      }
        
    return ret; 

    }
};