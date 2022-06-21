class Solution {
public:
    int furthestBuilding(vector<int>& height, int bricks, int ladders) {
        
        
    priority_queue<int> pq; 
    for( int i = 0;  i < height.size() -1 ; i++){ 
        int gap = height[i+1] - height[i] ;
        if( gap > 0) {
            pq.push(gap) ; 
            bricks -= gap ; 
            if( bricks < 0) { 
                ladders -- ; 
                bricks += pq.top() ; 
                pq.pop() ; 
                if ( bricks < 0 || ladders < 0) {
                    return i ; } 
            }
        }
    }
    return height.size() -1 ;

        
        
    }
};