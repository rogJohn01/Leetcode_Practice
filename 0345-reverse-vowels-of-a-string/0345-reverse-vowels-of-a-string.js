/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    
    let vowels =  ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U'];
    let ixs = []; 
    let ss = s.split(''); 
    let vxs = [] ; 
    for(let i =0 ; i < s.length ; i++){
        if( vowels.indexOf(s[i]) > -1){
            ixs.push(i) ; 
            vxs.push(s[i]);
        }
    }
    vxs.reverse(); 
    for(let i=0; i < ixs.length ; i++){
        ss[ixs[i]] = vxs[i] ;
    }
    return ss.join('')


};