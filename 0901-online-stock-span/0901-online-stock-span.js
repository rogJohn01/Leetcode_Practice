
var StockSpanner = function(prices) {
    this.st = [] ; 
};

/** 
 * @param {number} price
 * @return {number}
 */
StockSpanner.prototype.next = function(price) {
    let ans = 1; 
    while( this.st.length >0 && price >= this.st[this.st.length-1][0]) {
        ans += this.st[this.st.length-1][1] ; 
        this.st.pop()
    }
    this.st.push([price, ans])
    
    return ans; 
};

/** 
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */