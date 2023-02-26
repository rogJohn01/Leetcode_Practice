/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    
    let minv = prices[0] ; 
	let profit = 0 ; 
	for(let i=0 ; i < prices.length ;  i++){
		if(prices[i] < minv ){
			minv = prices[i]
		} else if ( prices[i] - minv  > profit ){
			profit = prices[i] - minv ; 
		}
	} return profit ; 


};