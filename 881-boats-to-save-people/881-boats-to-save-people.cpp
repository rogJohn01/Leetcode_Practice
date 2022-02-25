class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        
        int l,r;
        sort(people.rbegin(), people.rend());
        for(l =0 , r = people.size()-1; l<=r; ++l){
            if(people[l]+ people[r] <= limit) r--;
        }
        return l;
        
    }
};