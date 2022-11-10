/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicates = function(s) {
    
    let ans =[] ;
    for(let i=0; i < s.length ; i++){
        
        if( ans && ans[ans.length-1] == s[i]){
            ans.pop();
        } else{
            ans.push(s[i]);
        }
    }
    return ans.join('') ; 
    
};


