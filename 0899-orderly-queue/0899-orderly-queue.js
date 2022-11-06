/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var orderlyQueue = function(s, k) {
    
    if(k==1){
        let first = s.split('').sort()[0];
        let ans = [] ;
        for(let i=0; i< s.length ;i++){
            if(s[i]==first){
                ans.push( s.slice(i) +s.slice(0,i));
            }
        }
        return ans.sort()[0];
    }
    else {
        return s.split('').sort().join('') ; 
    }   
};