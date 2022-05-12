   class Solution {
    public:
        int candy(vector<int>& ratings) {
            const int len = ratings.size();
            if(len<=1) return len;
            
            int i, pPos, res=1, peak=1; // peak: # candies given to the i-1 child
            bool neg_peak = false; // flag to indicate if it is a local dip
            for(i=1; i<len;i++)
            {
                if(ratings[i] >= ratings[i-1]) 
                {   // it is increasing
                    if(neg_peak) 
                    {  // it is a local dip, we need to make sure i-1 has one candy
                        res -= (peak-1) * (i-pPos - (peak>0));
                        peak = 1;
                        neg_peak = false;
                    }
                   // update child i candy number, if equal, set to 1
                    peak = (ratings[i] == ratings[i-1])? 1:++peak;
                    res += peak;
                }
                else
                { // decreasing, just give one less candy, if it is the starting point of a decrease, update pPos
                    if(!neg_peak) {pPos = i-1; neg_peak = true;}
                    res += --peak;
                }
            }
// don't forget to update res, if the last one is a local dip
            return !neg_peak? res : res - (peak-1) * (i-pPos - (peak>0));
    
        }
    };