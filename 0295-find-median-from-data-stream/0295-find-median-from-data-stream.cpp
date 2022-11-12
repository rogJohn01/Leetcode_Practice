class MedianFinder {
public:
    
    priority_queue<int> mxHeap; 
    priority_queue<int ,vector<int> , greater<int>> mnHeap;
    
    
    MedianFinder() {
        
    }
    
    void addNum(int num) {
       mxHeap.push(num) ;
       mnHeap.push(mxHeap.top()); 
       mxHeap.pop();
       if(mnHeap.size() > mxHeap.size() ) {
            mxHeap.push(mnHeap.top()) ;
            mnHeap.pop();
       }
    }
    
    double findMedian() {
        if(mxHeap.size() > mnHeap.size() ) {
            return mxHeap.top();
        } return (mxHeap.top() + mnHeap.top()) / 2.0 ; 
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */