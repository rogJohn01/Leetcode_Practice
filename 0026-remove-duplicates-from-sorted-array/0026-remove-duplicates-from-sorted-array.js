/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    
    let p =0 ; 
    for(i=0; i< nums.length; i++){
        if(nums[i] != nums[i+1]){
            nums[p] = nums[i] ; 
            p++ ; 
        }
    }
    return p
 
};